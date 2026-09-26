"""Local pattern scan with location-only findings and a line-numbered masked view."""
import argparse, json, re
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument('directory', help='Approved repository root')
parser.add_argument('--view', metavar='FILE', help='Show a UTF-8 file with matched spans masked; path relative to root')
parser.add_argument('--mask-line', type=int, action='append', default=[], metavar='N',
                    help='With --view, mask a whole line flagged by an external scanner; repeat as needed')
args = parser.parse_args()
if args.mask_line and not args.view:
    parser.error('--mask-line requires --view')
if any(n < 1 for n in args.mask_line):
    parser.error('--mask-line must be positive')
root=Path(args.directory).resolve()
if not root.is_dir(): parser.error('Expected a directory')
skip={'.git','node_modules','.venv','venv','__pycache__','.candidate'}
rules = {
    'credential-shaped': re.compile(
        r'\b(?:sk_(?:live|test|proj)_|sk-(?:ant-|proj-)?|AIza|xox[abp]-|github_pat_|gh[opsu]_|AKIA)[A-Za-z0-9_\-]{12,}'
    ),
    'private-key-marker': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'assigned-secret': re.compile(
        r"(?i)\b[A-Z_][A-Z0-9_\-]*(?:KEY|SECRET|TOKEN|PASSWORD)[A-Z0-9_\-]*\b\s*[:=]\s*(?:['\"][^'\"]{16,}['\"]|[^\s'\"#;]{16,})"
        r"|(?i:)(?<![\w-])(?:KEY|SECRET|TOKEN|PASSWORD)\s*[:=]\s*(?:['\"][^'\"]{16,}['\"]|[^\s'\"#;]{16,})"
    ),
    'inline-credentials': re.compile(r'(?i)\b[a-z][a-z0-9+.-]*://[^\s/:@]+:[^\s/@]+@[^\s/]+'),
    'client-exposed': re.compile(
        r'\b(?:NEXT_PUBLIC_|VITE_|EXPO_PUBLIC_|REACT_APP_)(?:[A-Z0-9_]*(?:KEY|SECRET|TOKEN)[A-Z0-9_]*)\b', re.I
    ),
}
def read_text(file):
    if file.stat().st_size > 2_000_000:
        raise ValueError('File exceeds the view/scan limit')
    raw = file.read_bytes()
    if b'\x00' in raw:
        raise ValueError('Binary file')
    return raw.decode('utf-8')


def masked_line(line):
    # Collect spans on the original text: sequential substitutions can hide an
    # overlapping match before it has been fully redacted.
    spans = sorted((m.start(), m.end(), rule)
                   for rule, pattern in rules.items() for m in pattern.finditer(line))
    groups = []
    for start, end, rule in spans:
        if groups and start < groups[-1][1]:
            groups[-1][1] = max(end, groups[-1][1])
            groups[-1][2].add(rule)
        else:
            groups.append([start, end, {rule}])
    parts = []
    cursor = 0
    for start, end, labels in groups:
        parts.append(line[cursor:start])
        parts.extend('[REDACTED:' + rule + ']' for rule in sorted(labels))
        cursor = end
    parts.append(line[cursor:])
    return ''.join(parts)


if args.view:
    file = root / args.view
    try:
        relative = file.resolve().relative_to(root)
        if any(p in skip for p in relative.parts):
            raise ValueError('Excluded directory')
        # Refuse symlinks in the selected path, including parent directories.
        current = root
        for part in file.absolute().relative_to(root).parts:
            current = current / part
            if current.is_symlink() or (hasattr(current, 'is_junction') and current.is_junction()):
                raise ValueError('Linked path')
        lines = read_text(file).splitlines()
        if any(n > len(lines) for n in args.mask_line):
            raise ValueError('External finding line is outside file')
    except (OSError, UnicodeError, ValueError):
        parser.error('Cannot safely view this file: check root, links, size, encoding and line numbers')
    for n, line in enumerate(lines, 1):
        masked = '[REDACTED:external-scan]' if n in args.mask_line else masked_line(line)
        print(f'{n}: {masked}')
    raise SystemExit(0)

findings = []
scanned = skipped = 0
for file in root.rglob('*'):
    if any(p in skip for p in file.relative_to(root).parts) or not file.is_file() or file.is_symlink():
        continue
    try:
        text = read_text(file)
        scanned += 1
    except (OSError, UnicodeError, ValueError):
        skipped += 1
        continue
    for n, line in enumerate(text.splitlines(), 1):
        for rule, pattern in rules.items():
            if pattern.search(line):
                findings.append({'rule': rule, 'file': file.relative_to(root).as_posix(), 'line': n})
print(json.dumps({'scanned_files': scanned, 'skipped_files': skipped, 'findings': findings,
                  'limitation': 'Pattern fallback; not Git history or proof of absence.'}, indent=2))
raise SystemExit(1 if findings else 0)
