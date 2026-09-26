# Secure Launch

An agent skill for the last security pass before you go live. It reads your project, makes a short checklist for what you actually use, explains what is already in place, and verifies the local fixes you approve.

**Day-one exposure first.** A typical SaaS gets roughly 12–15 grouped launch items, not an encyclopedia. Routine CSP rollout, logging hygiene, contacts, CI pinning and automated updates normally belong in the first week. Deeper platform assurance can wait until needed; a reachable issue is promoted when exposure justifies it.

## What it covers

- Secrets and client bundles; separate development/production data and credentials.
- Account/admin access, tenant isolation and applicable Supabase/Firebase rules.
- Auth, AI and public/write endpoint budgets; forms and bot resistance; trustworthy client IPs behind proxies.
- Authentic webhooks, approved redirects, production debug settings and baseline headers.
- Provider/CDN and email-domain authentication handoffs, including SPF/DKIM/DMARC when email is sent.
- Conditional supply-chain, cloud, desktop, agent-skill/MCP and AI checks.

Mobile coverage is a **starter set, not full MASVS (OWASP’s mobile application security standard) coverage or verification**. Platform tooling and specialist review may be needed.

## Install

This repository is local-only and has no remote yet. These Skills CLI commands are **prospective**, not working publication claims. After approving and publishing a repository, replace `<published-repository-url>` with its actual URL:

```sh
npx skills@latest add <published-repository-url> --skill secure-launch --agent claude-code --global
npx skills@latest add <published-repository-url> --skill secure-launch --agent codex --global
```

For an approved local installation, copy the complete `secure-launch/` folder to your agent's skill directory. No automatic installation is performed by this project. The Markdown runtime has no mandatory service or package dependency; the optional redacted pattern scanner uses Python's standard library.

## Try it

```text
Use secure-launch before I launch this app. Read the repo first, tailor a short
security checklist, and show the files and local checks for each proposed fix.
Ask for plan approval before making changes; keep provider and DNS work with me.
```

## How it works

Inspect → classify → prioritize → approve the plan → approve reserved items separately → make small local changes → verify and hand off.

Each item shows one friendly action status plus a separate evidence state. “I'll add this” is a plan, not a completed fix. Loading the skill does not authorize deployment, live scanning or secret access. Payment/auth/session/database/IaC changes and CSP enforcement have item-specific approval gates. A CDN or bot provider is not automatically purchased or configured.

The skill pairs with Lean Engineering for ownership and small verified changes, and Efficiency Skill for appropriate bounded delegation. It remains self-contained when neither is installed. The main owner retains security judgment; no reviewer swarms.

## Honest limits

The Express SaaS case (login rate limit and webhook signature fix) has discovery-only evidence because Codex’s Windows sandbox blocks Node test workers; those fixes have not been verified.

This is a launch-readiness pass, **not a penetration test or compliance certificate**. Local tests cannot prove production DNS, TLS, storage policies or provider settings. No automated checklist proves an app secure. Audits depend on tool/advisory availability and can miss unknown vulnerabilities; the fallback pattern scan can miss secrets and report harmless placeholders. Nothing is a pass unless the named check ran.

## Sources and evaluation

[Research](RESEARCH.md) · [Approved priorities and coverage](COVERAGE-MATRIX.md) · [Runtime sources](secure-launch/references/sources.md) · [Evaluation protocol and results](evals/README.md) · [Changelog](CHANGELOG.md).

Primary guidance is dated and distinguishes stable standards from drafts and inaccessible pages. Original guidance cites sources without copying their prose or code. Four synthetic Codex cases run once each; results, including failures and limitations, are recorded under `evals/` and are not a production-security claim.

## Repository

`secure-launch/SKILL.md` is the runtime entry point; `references/` contains profiles, modules, stack pointers, source records and the reporting contract. `agents/openai.yaml` is optional interface metadata. `evals/` contains synthetic fixtures and evidence. `SITE-ENTRY-DRAFT.json` is a draft only; it does not edit the site.

## License

[MIT](LICENSE) for this project's original material. Linked standards and third-party resources retain their own licenses.

## 0.1.0 evaluation status

Four Codex sessions attempted once: **1 PASS, 2 PARTIAL, 1 BLOCKED**. The local skill is built, but the behavioral suite did not fully pass. See [the full results and limits](evals/RESULTS-2026-09-27.md). Nothing has been published or installed globally.
