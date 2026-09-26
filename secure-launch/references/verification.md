# Local proof without external effects

Before executing project commands, complete the scan-first discovery below, then inspect scripts/import paths and define the approved fixture/repo root, synthetic identities, local listen addresses, commands and time/request limits. Bind temporary servers to loopback on an unused port. Remove inherited production credentials from the test process; do not print environment values. Disable or mock every external SDK, telemetry, mailer, webhook callback and model client. Restrict egress where the harness supports it; disclose instruction-only isolation instead of claiming OS enforcement.

## Discovery and scans

Run the secret scan **before any project source or repository file-content read**, including manifests and scripts used to plan later commands. Scanner help and this skill's trusted runtime are not project source. Keep a guard list of flagged paths, lines and rule IDs only. Scan the current working tree, including untracked source; a history-only scan is insufficient. If scanning is unavailable or fails, stop source reads and report the gap. A finding exit (normally 1) differs from a scanner execution error.

Read flagged files only through `python <skill-dir>/scripts/redacted_scan.py <repo-root> --view FILE`; never use `cat`, `type`, `Get-Content`, or content-mode `grep`/`rg` on them. Search key names across the repository only with `rg -l` or masked output, including searches before classification. Never print raw diffs containing flagged lines. Keep this guard in force during later verification too; rescan changed files before displaying them.

The view prints `line-number: text`, replacing matched spans with `[REDACTED:<rule>]` and preserving other text. Overlapping matches are masked together with their rule markers. For findings from gitleaks that the fallback may not recognize, add `--mask-line N` for **every flagged line** (repeat the flag for a range); these whole lines become `[REDACTED:external-scan]`. If a finding lacks usable current-file line numbers, do not display that file. Secret-value files, skipped/unscanned files, oversized/binary files and unsupported encodings are not cleared for raw reading; keep them unread or obtain a safe supported scan. Masking is limited to known patterns/flagged lines and cannot guarantee absence of unknown secret formats.

- List tracked secret-like filenames with `git ls-files -- .env '.env.*' '*.pem' '*.key'`; this displays paths, not file contents. Do not print `git diff` lines that may contain secrets.
- If gitleaks is installed, check its local help for the installed version and enable complete redaction with `--redact` before using it; retain only paths, line numbers and rule IDs from its redacted report. Do not auto-install a scanner.
- Otherwise, the bundled `scripts/redacted_scan.py <directory>` is a documented limited pattern fallback. It processes files locally and emits only rule ID, file and line. It does not validate credentials, prove absence, or inspect Git history. It skips VCS/dependency directories. A finding requires owner interpretation; public keys/placeholders may be intentional.
- Inspect the package manager and authoritative lockfile before choosing `npm audit`, `pnpm audit`, `pip-audit` or `osv-scanner`. These may need a remote advisory source. Use an available supported offline mode/cache or ask for the specific metadata-sharing exception; no registry/network access is implied by “local verification”. No forced audit fix or new scanner install.

## Behavior checks

Use the narrowest project test command; record its exact working directory and actual output. The following are check shapes to adapt, not commands to execute against an arbitrary running service:

| Check | Local positive and negative proof |
| --- | --- |
| Headers/debug | Read response headers and a controlled error from the inspected local app; do not display sensitive body content. Production TLS/CDN state stays unverified. |
| Rate limits | Set a low fixture threshold and send at most the approved request cap (e.g. 20), each with a short timeout. Record status codes; stop at 429 or the cap. Check a separate identity and spoofed forwarding input. Never traffic-test production. |
| Access/tenants | Fake signed-out subject is denied; user A can read A's seeded record but not B's; role-restricted actions also reject ordinary users. Do not replace real auth with a test header in production code. |
| Cookies/CSRF | Inspect Set-Cookie names/flags without values, test intended same-site flow and rejected cross-site state changes. Use a synthetic local HTTPS setup where Secure behavior is material. |
| CORS | Test approved and unapproved origins on the private endpoint; browser preflight is not a substitute for authorization. Public noncredentialed endpoints may intentionally permit '*'. |
| Webhooks | Mock provider SDKs or sign fake fixtures locally; valid events succeed, altered and replayed events do not repeat side effects. Payments need per-item approval first. |
| Client secrets | Build with an unmistakably synthetic canary; search browser artifacts with redacted output. Confirm presence before and absence after the approved change; exclude server-only output. Never build using real keys. |
| Forms/redirects | Mock challenge service success/failure/replay; reject unapproved redirect origins and encoded bypasses; valid forms/redirects continue working. |
| Infra/email | Offline syntax/policy review and documented user steps. Local source does not prove remote DNS, storage, CDN or email authentication works. |

A zero-test run, empty scan or 200 from an unrelated route is not acceptance evidence. Investigate the command/target, then report the gap if budget prevents further work. Honor a user's once-only evaluation rule: preserve failure and do not rerun the trial. Fixture development checks and a trial's focused RED/GREEN are distinct from rerunning a behavioral evaluation.

## Stop and report

Stop the affected action at an approval boundary, possible secret output, unexpected external endpoint, unknown effect or exhausted request/time budget. Continue independent approved work where possible. Preserve failures and distinguish local evidence, static config inspection and user-confirmed provider state. Do not certify security or compliance.
