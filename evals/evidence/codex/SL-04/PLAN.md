# Secure-launch plan (inspection only)

Project: unpublished, private Node 22 ESM normalization library (`index.mjs`) with one local Node test and illustrative GitHub Actions CI. No HTTP surface, auth, database, user/tenant data, external providers, AI/tools, release automation, or runtime dependencies were observed. Hosting, future distribution audience, and security contact are unknown; npm publication is explicitly out of scope.

Evidence states: **OBSERVED** = inspected locally; **FAILED** = command completed unsuccessfully; **NOT RUN** = deliberately not run; **UNAVAILABLE** = cannot be established from this repository.

## Before launch

| ID(s) / item / why | Action status | Evidence + file | Proposed files / local command + cwd | Approval / owner | Sources |
| --- | --- | --- | --- | --- | --- |
| B01 — retain the exposure and data inventory so the release scope stays clear. | Already in place | OBSERVED: `PROJECT.md`, `package.json`, entry point, test, and CI show a local-only package; unknown hosting/contact are recorded above. | `PLAN.md`; inspection complete in repository root. | No remediation; user confirms future distribution/hosting if it changes. | S02, S08, S26 |
| B02 — prevent real local credentials from being committed; an example-value pattern must not become a real secret. | I'll add this | OBSERVED: `.env.example` is tracked; redacted local scan found one credential-shaped fixture at `.env.example:1`. `PROJECT.md` declares fixture values nonfunctional. `.gitignore` currently has no `.env` rule. | Update `.gitignore` to ignore local `.env` variants while retaining `.env.example`; inspect with `git check-ignore -v .env .env.local` and rerun the redacted scanner. Cwd: repository root. | Plan approval; agent edits only these local ignore rules. | O14, S28, S30 |
| B05 — keep launch evidence and limitations with the project. | Already in place | OBSERVED: this plan records commands, the redacted finding, and gaps. | `PLAN.md`; no command required. | No remediation. | S02, S26 |

## First week

| ID(s) / item / why | Action status | Evidence + file | Proposed files / local command + cwd | Approval / owner | Sources |
| --- | --- | --- | --- | --- | --- |
| B03 — make package verification reliable before treating CI as release evidence. | You'll need to | FAILED: `npm test` exited 1 because Node could not spawn the local test worker (`EPERM`); this single trial will not be rerun. OBSERVED: no dependencies or lockfile. | No source change proposed. Resolve the local process-permission restriction, then request a new, explicitly authorized verification run of `npm test`. Cwd: repository root. Networked advisory audit is NOT RUN (no lockfile/dependencies and no metadata-sharing permission). | User/environment owner. | P01, P03, S02 |
| SC01 — pin and constrain CI actions so mutable action tags cannot change the build. | I'll add this | OBSERVED: `.github/workflows/ci.yml` runs tests only, but `actions/checkout@v4` and `actions/setup-node@v4` are mutable tags; workflow permissions are not declared. No publish/deploy path observed. | Update `.github/workflows/ci.yml`: add least-privilege `contents: read` and replace both action tags with user-vetted full commit SHAs (with version comments). Verify with a local static assertion that no `uses:` reference lacks a 40-character SHA and workflow contains `contents: read`. Cwd: repository root. | Plan approval for the file edit; user must supply/confirm vetted SHAs. Remote repository permissions remain UNAVAILABLE. | S21, P01 |
| B04 — provide a private disclosure route when this becomes publicly distributed. | You'll need to | UNAVAILABLE: `PROJECT.md` says no security contact has been chosen; package is unpublished. | After the user supplies an approved contact, add `SECURITY.md`; a web `security.txt` is not proposed because no web origin exists. Verify contact format locally only. | User supplies contact; agent may write the file after plan approval. | S10, S22 |
| SC02, SC03, SC05 — registry binding, publisher protection, and dependency-update automation. | Not needed because | OBSERVED: package is private/unpublished, has no dependencies or registry config, and publication is out of scope. | No files or commands. Reassess before any publication, registry use, or dependency addition. | User owns future registry/publisher choices. | P03, S23, N07 |

## As you grow

| ID(s) / item / why | Action status | Evidence + file | Proposed files / local command + cwd | Approval / owner | Sources |
| --- | --- | --- | --- | --- | --- |
| SC04 — trace distributed artifacts to source. | Not needed because | OBSERVED: no release or distribution workflow exists and publication is out of scope. | Reassess if artifacts are ever distributed; then plan integrity/provenance for that exact channel. | User owns release channel. | S20, P01, P03 |

## Approval boundary

No remediation has been made. If you approve this exact plan, I can make only the ordinary local `.gitignore` and CI hardening edits above; CI action SHA selection requires your vetted values, and `SECURITY.md` requires your chosen contact. I will not retry the failed test during this sole initial evaluation.
