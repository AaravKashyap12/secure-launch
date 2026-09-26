"""Once-only local scanner regression check; synthesize all credential values at runtime."""
import json
import secrets
import subprocess
import sys
import tempfile
from pathlib import Path

scanner = Path(__file__).resolve().parents[1] / 'secure-launch/scripts/redacted_scan.py'
cases = []
values = []
for prefix in ['sk-', 'sk-proj-', 'sk-ant-', 'AIza', 'xoxa-', 'xoxb-', 'xoxp-', 'github_pat_', 'gho_', 'ghp_', 'ghs_', 'ghu_', 'sk_live_', 'AKIA']:
    value = prefix + secrets.token_hex(16)
    cases.append((value, {'credential-shaped'})); values.append(value)
for name in ['KEY', 'SECRET', 'TOKEN', 'PASSWORD', 'API_KEY', 'MY_SECRET', 'SERVICE_TOKEN', 'DB_PASSWORD']:
    for quote in ['', "'", '"']:
        value = secrets.token_hex(12)
        cases.append((name + '=' + quote + value + quote, {'assigned-secret'})); values.append(value)
for prefix in ['NEXT_PUBLIC_', 'VITE_', 'EXPO_PUBLIC_', 'REACT_APP_']:
    value = 'sk-proj-' + secrets.token_hex(16)
    cases.append((prefix + 'API_KEY=' + value, {'client-exposed', 'assigned-secret', 'credential-shaped'})); values.append(value)
for scheme in ['postgres', 'postgresql', 'mysql', 'mongodb+srv', 'redis']:
    password = secrets.token_hex(12)
    value = scheme + '://fixture:' + password + '@example.invalid/db'
    cases.append(('DATABASE_URL=' + value, {'inline-credentials'})); values.extend([value, password])
marker = '-----BEGIN ' + 'PRIVATE KEY-----'
cases.append((marker, {'private-key-marker'})); values.append(marker)
# Multiple disjoint spans plus overlaps exercise masking on original offsets.
first, second = 'sk-ant-' + secrets.token_hex(16), 'ghp_' + secrets.token_hex(16)
cases.append(('prefix ' + first + ' middle ' + second + ' suffix', {'credential-shaped'}))
values.extend([first, second])
cases.extend([('API_KEY=short', set()), ('PUBLIC_COLOR=blue', set()), ('', set()), ('  // plain source comment  ', set())])
with tempfile.TemporaryDirectory(prefix='secure-launch-scanner-') as folder:
    Path(folder, '.env').write_text('\n'.join(line for line, _ in cases), encoding='utf-8')
    result = subprocess.run([sys.executable, str(scanner), folder], capture_output=True, text=True, encoding='utf-8')
    assert result.returncode == 1, 'scanner must return finding exit 1'
    assert not any(value in result.stdout + result.stderr for value in values), 'value leaked in scanner output'
    data = json.loads(result.stdout)
    for number, (_, expected) in enumerate(cases, 1):
        found = {f['rule'] for f in data['findings'] if f['line'] == number}
        assert expected <= found and (expected or not found), f'case {number}: wrong rule coverage'
    assert all(set(f) == {'rule', 'file', 'line'} for f in data['findings']), 'finding contains extra fields'
    assert {f['rule'] for f in data['findings']} == {'credential-shaped', 'assigned-secret', 'client-exposed', 'inline-credentials', 'private-key-marker'}
    view = subprocess.run([sys.executable, str(scanner), folder, '--view', '.env'], capture_output=True, text=True, encoding='utf-8')
    assert view.returncode == 0, 'masked view must return exit 0'
    assert not any(value in view.stdout + view.stderr for value in values), 'value leaked in masked view'
    viewed = view.stdout.splitlines()
    assert len(viewed) == len(cases), 'view lost source lines'
    for number, ((original, expected), rendered) in enumerate(zip(cases, viewed), 1):
        assert rendered.startswith(f'{number}: '), f'line {number}: missing line number'
        if expected:
            assert all('[REDACTED:' + rule + ']' in rendered for rule in expected), f'line {number}: missing rule mask'
        else:
            assert rendered == f'{number}: {original}', f'line {number}: unflagged text changed'
    assert viewed[-5].startswith(f'{len(cases)-4}: prefix [REDACTED:credential-shaped] middle '), 'disjoint spans lost surrounding text'
    assert viewed[-5].endswith('[REDACTED:credential-shaped] suffix'), 'disjoint suffix lost'
    # External scanner-only findings must not leak through the fallback's narrower rules.
    external_value = secrets.token_hex(12)
    Path(folder, 'external.txt').write_text('opaque: ' + external_value + '\nunchanged', encoding='utf-8')
    external = subprocess.run([sys.executable, str(scanner), folder, '--view', 'external.txt', '--mask-line', '1'], capture_output=True, text=True, encoding='utf-8')
    assert external.returncode == 0 and external_value not in external.stdout + external.stderr, 'external finding leaked'
    assert external.stdout.splitlines() == ['1: [REDACTED:external-scan]', '2: unchanged'], 'external line mask incorrect'
    refused = subprocess.run([sys.executable, str(scanner), folder, '--view', '../outside.txt'], capture_output=True, text=True, encoding='utf-8')
    assert refused.returncode == 2 and not refused.stdout, 'out-of-root view must refuse without source output'
print(f'PASS: {len(cases)} synthetic cases; all 5 rules fired; scan/view leaked no generated values; line numbers and unflagged text preserved; overlap/disjoint masks, external-line mask and root boundary passed.')
