"""Limited local pattern scan: output locations/rule IDs only, never matched values."""
import argparse, json, re
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument('directory');args=parser.parse_args()
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
findings=[];scanned=0;skipped=0
for file in root.rglob('*'):
    if any(p in skip for p in file.relative_to(root).parts) or not file.is_file() or file.is_symlink(): continue
    try:
        if file.stat().st_size>2_000_000: skipped+=1;continue
        raw=file.read_bytes()
        if b'\x00' in raw[:4096]: skipped+=1;continue
        text=raw.decode('utf-8');scanned+=1
    except (OSError,UnicodeError): skipped+=1;continue
    for n,line in enumerate(text.splitlines(),1):
        for rule,pattern in rules.items():
            if pattern.search(line):findings.append({'rule':rule,'file':file.relative_to(root).as_posix(),'line':n})
print(json.dumps({'scanned_files':scanned,'skipped_files':skipped,'findings':findings,'limitation':'Pattern fallback; not Git history or proof of absence.'},indent=2))
raise SystemExit(1 if findings else 0)
