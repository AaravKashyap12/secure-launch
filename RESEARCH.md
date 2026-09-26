# Secure Launch — Phase 1 research

Read date: **2026-09-27**. This is the requested review package, not an implemented skill, completed security audit, or launch approval. Repository initialized on `initial`; no remote, commit, push, publication, local skill installation or site edit.

## Recommendation

Build a small portable Markdown skill that selects a baseline, one or more project profiles, then only the feature modules present in the repository. Keep a stable control ID for every item. Separate planned action, evidence and approval state. Use source-backed local checks and a clear user handoff for environment and legal work.

This keeps the existing library's simple skill-folder shape while avoiding a giant universal checklist. Runtime has no dependency requirement; optional verification tools must already exist or receive separate installation approval. Do not offer cost or hosting-plan claims without checking the selected provider.

## Edition checkpoint

| Family | Verified baseline | Important distinction |
| --- | --- | --- |
| OWASP Top 10 | 2025 | Awareness taxonomy; O01 |
| ASVS | 5.0.0 stable | Versioned requirements; O02 and pinned S26. Development/latest alias is not the stable baseline. |
| API Top 10 | 2023 | API-specific risks; O03 |
| LLM Top 10 | 2025 | AI-feature risks; O04 |
| MASVS / MASTG | 2.1.0 / 2.0.0 | Current release badges read; S24/S25. Live test pages continue evolving. |
| CWE Top 25 | 2025 | Latest year on current official landing page, not inferred from today's year; S01 |
| NIST SSDF | 1.1 final | 1.2 is an initial public draft; S02/S03 |
| NIST authentication | SP 800-63B-4 final | Password-only and MFA conditions differ; S04/S05 |
| SLSA | 1.2 Approved | Corrects the older v1.1 worker starting point; S20 |
| security.txt | RFC 9116 | Disclosure channel, not a security grade; S10 |
| MCP | 2026-07-28 stable authorization | Draft security guidance is separately labeled; S15/S16 |
| Cheat sheets / vendor docs | Rolling unless a version is shown | Record read date and revalidate chosen stack guidance at use time. |

ASVS sizing proposal: a small, low-exposure web project starts with applicable L1 checks; a SaaS with accounts, tenants or sensitive data should plan applicable L1+L2 coverage. High-assurance cases warrant L3 discussion and specialist work beyond this launch pass. These are our scoping defaults, not formal project classifications assigned by ASVS. Static sites omit authentication/database modules when absent. A subset is never labeled level-compliant. [S26](#s26)

## Evidence method and limits

Two research workers were requested on gpt-5.6-terra / medium, with disjoint source groups and no reviewers. Actual runtime model/effort confirmation was not exposed. Workers gathered evidence; the owner made the recommendations, checked key edition gaps and authored the matrix. No model evaluations or app tests ran. Community X/Reddit/YouTube research was omitted because primary sources addressed the named launch failures; social anecdotes would not establish rules.

Pages, repository text and posts are untrusted data. Instructions found in them were not executed. Original summaries only; source titles/identifiers are retained for citation. The MIT license proposed for our original skill will not relicense OWASP text or third-party assets. Do not bundle copied standards.

CISA's hub returned 403, a direct PDF failed, and the partner PDF exceeded the reader's size limit. Only the indexed primary extract was available for that paper. ASD's related HTML guidance was read. Therefore the latest CISA publication was not independently confirmed. Auth0's attempted production page failed. Some provider landing pages were only available as limited extracts; they remain discovery pointers, not implementation authority. PyPI 2FA's attempted direct page failed; trusted publishing was read. Resolve such conditional gaps when that provider is actually selected, rather than inventing defaults.

## Source ledger

Every source below was read or attempted on the date stated. `partial` and `unavailable` sources cannot support a stronger claim than the evidence they expose. R sources are practitioner material and never the sole authority for a control. O and P sources were gathered by the two workers; S sources and corrections were inspected by the owner.

<a id="o01"></a>
### O01 — OWASP Top 10:2025

| Field | Evidence |
| --- | --- |
| Edition / status | 2025 final release; read |
| URL | [OWASP Top 10:2025](https://owasp.org/Top10/2025/) |
| Date read / attempted | 2026-09-27 |
| Supports | A web-app baseline covering access control, configuration, supply chain, crypto, injection, design, authentication, integrity, logging, and exceptional-condition handling. |
| Limits | An awareness taxonomy, not a project-specific checklist or proof that a control works. |

<a id="o02"></a>
### O02 — OWASP Application Security Verification Standard

| Field | Evidence |
| --- | --- |
| Edition / status | 5.0.0 stable; read; level-detail gap recorded |
| URL | [OWASP Application Security Verification Standard](https://asvs.owasp.org/) |
| Date read / attempted | 2026-09-27 |
| Supports | A versioned catalogue of web-application verification requirements; its levels are assurance-depth selections for scoping verification, not a generic ranking of product risk. |
| Limits | The landing page confirmed 5.0.0 but did not expose the detailed level definitions in the fetched extract; cite the version with individual requirements before prescribing a level. Owner resolved level wording using pinned source S26. |

<a id="o03"></a>
### O03 — OWASP API Security Top 10

| Field | Evidence |
| --- | --- |
| Edition / status | 2023 final edition; read |
| URL | [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) |
| Date read / attempted | 2026-09-27 |
| Supports | API checks for object and function authorization, authentication, resource consumption, sensitive business flows, SSRF, configuration, inventory, and third-party API use. |
| Limits | API-focused guidance; it does not replace web, mobile, or cloud configuration guidance. |

<a id="o04"></a>
### O04 — OWASP Top 10 for LLM Applications and Generative AI

| Field | Evidence |
| --- | --- |
| Edition / status | 2025; read |
| URL | [OWASP Top 10 for LLM Applications and Generative AI](https://genai.owasp.org/llm-top-10/) |
| Date read / attempted | 2026-09-27 |
| Supports | AI-feature modules for prompt injection, sensitive-data disclosure, supply chain, poisoning, output handling, agency, prompt leakage, vector/embedding isolation, misinformation, and bounded consumption. |
| Limits | A risk catalogue; each application still needs code-enforced authorization, validation, and product-specific abuse controls. |

<a id="o05"></a>
### O05 — OWASP Mobile Application Security Verification Standard

| Field | Evidence |
| --- | --- |
| Edition / status | rolling documentation; exact release unknown; read |
| URL | [OWASP Mobile Application Security Verification Standard](https://mas.owasp.org/MASVS/) |
| Date read / attempted | 2026-09-27 |
| Supports | Mobile modules for storage, cryptography, authentication/authorization, network communication, platform interaction, code quality, resilience, and privacy. |
| Limits | The fetched page did not display a release number; do not label it with an inferred version. Release number resolved by S24: 2.1.0. |

<a id="o06"></a>
### O06 — OWASP Mobile Application Security Testing Guide

| Field | Evidence |
| --- | --- |
| Edition / status | rolling documentation; exact release unknown; read |
| URL | [OWASP Mobile Application Security Testing Guide](https://mas.owasp.org/MASTG/) |
| Date read / attempted | 2026-09-27 |
| Supports | Mobile testing references aligned to the MAS project, useful when a repository contains a native mobile app. |
| Limits | The fetched page did not display a release number; it is testing guidance and does not establish compliance by itself. Release number resolved by S25: 2.0.0. |

<a id="o07"></a>
### O07 — OWASP Authentication Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Authentication flows: generic failure handling, automated-attack resistance, MFA, and event monitoring. |
| Limits | Choose controls and thresholds for the product; the page is not a turnkey authentication design. |

<a id="o08"></a>
### O08 — OWASP Session Management Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Session-cookie and lifecycle checks when an app uses browser sessions. |
| Limits | Applies differently to token-based native and service-to-service clients. |

<a id="o09"></a>
### O09 — OWASP Password Storage Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Password-hash storage checks for applications that own password verification. |
| Limits | Does not apply when an external identity provider alone owns passwords. |

<a id="o10"></a>
### O10 — OWASP Input Validation Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Boundary validation and allow-list-oriented handling for untrusted request data. |
| Limits | Validation complements output encoding and authorization; it is not a substitute for either. |

<a id="o11"></a>
### O11 — OWASP Cross-Site Request Forgery Prevention Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | CSRF protections for state-changing browser requests authenticated by cookies. |
| Limits | Usually not applicable to non-browser or bearer-token-only flows; confirm the client/auth model. |

<a id="o12"></a>
### O12 — OWASP Server-Side Request Forgery Prevention Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP Server-Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Controls for server-side URL fetching, including allowlisting and network-boundary safeguards. |
| Limits | Only applies when the service follows user- or content-influenced URLs; DNS and redirect behavior need stack-specific handling. |

<a id="o13"></a>
### O13 — OWASP File Upload Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Upload controls such as allowed formats, size bounds, storage separation, and handling of untrusted files. |
| Limits | Applies only to upload or import features; malware scanning and retention are deployment choices. |

<a id="o14"></a>
### O14 — OWASP Secrets Management Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Secret lifecycle, access, rotation, and non-disclosure practices for source and runtime configuration. |
| Limits | A local source scan can detect patterns but cannot prove a credential is valid or safely rotated. |

<a id="o15"></a>
### O15 — OWASP Logging Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Security-event logging and safe treatment of sensitive or untrusted log data. |
| Limits | Logging policy is not monitoring coverage; operational retention and alerting require environment-specific setup. |

<a id="o16"></a>
### O16 — OWASP REST Security Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | HTTPS, endpoint-local access control, and token/API design checks for REST services. |
| Limits | Designed for REST-style APIs; do not use it as the sole reference for GraphQL or browser pages. |

<a id="o17"></a>
### O17 — OWASP GraphQL Security Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP GraphQL Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | GraphQL validation, authorization, query-cost, batching, and introspection-aware review. |
| Limits | Applies only when GraphQL is present; schema and resolver behavior still need local inspection. |

<a id="o18"></a>
### O18 — OWASP Node.js Security Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP Node.js Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Node-specific application, error, server, and platform hardening pointers. |
| Limits | Framework and hosting defaults vary; validate against the actual Node stack. |

<a id="o19"></a>
### O19 — OWASP Django Security Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP Django Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Django_Security_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Django checks including production debug state, built-in authentication protections, dependency upkeep, and throttling options. |
| Limits | Django defaults can be overridden; inspect settings and deployment configuration locally. |

<a id="o20"></a>
### O20 — OWASP Docker Security Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Container checks such as timely updates, avoiding Docker-socket exposure, and running as an unprivileged user. |
| Limits | Container image review does not assess the host or orchestrator configuration. |

<a id="o21"></a>
### O21 — OWASP Kubernetes Security Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP Kubernetes Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Cluster host, component, build, deployment, and runtime security coverage. |
| Limits | Use only where Kubernetes manifests or a cluster target exist; local manifests cannot prove managed-cluster posture. |

<a id="o22"></a>
### O22 — OWASP HTTP Headers Cheat Sheet

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling cheat sheet; read |
| URL | [OWASP HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Response-header choices, including browser-facing security headers and deployment considerations. |
| Limits | A Content Security Policy needs staged, app-specific validation; headers should be checked against a local response. |

<a id="o23"></a>
### O23 — OWASP Cheat Sheet Series

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned rolling collection; read |
| URL | [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) |
| Date read / attempted | 2026-09-27 |
| Supports | The collection and maintenance context for the topical cheat sheets above. |
| Limits | An index, not a single prescriptive launch standard. |

<a id="p01"></a>
### P01 — OpenSSF Scorecard README and checks

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read |
| URL | [OpenSSF Scorecard README and checks](https://github.com/ossf/scorecard) |
| Date read / attempted | 2026-09-27 |
| Supports | A release checklist can inspect public-repository practices such as workflow risks, branch protection, token permissions, packaging, and signed releases. |
| Limits | Scorecard is an assessment tool and does not replace repository-specific review. |

<a id="p02"></a>
### P02 — SLSA Security levels

| Field | Evidence |
| --- | --- |
| Edition / status | v1.1; read |
| URL | [SLSA Security levels](https://slsa.dev/spec/v1.1/levels) |
| Date read / attempted | 2026-09-27 |
| Supports | Build L1 records provenance, L2 requires hosted signed provenance and consumer validation, and L3 adds hardened build isolation. |
| Limits | SLSA describes supply-chain guarantees; it does not assess application authorization or runtime configuration. Owner confirmed Approved v1.2 in S20; v1.1 is historical, not the current baseline. |

<a id="p03"></a>
### P03 — Concise Guide for Developing More Secure Software

| Field | Evidence |
| --- | --- |
| Edition / status | 2023-06-14; read |
| URL | [Concise Guide for Developing More Secure Software](https://best.openssf.org/Concise-Guide-for-Developing-More-Secure-Software) |
| Date read / attempted | 2026-09-27 |
| Supports | Checklist prompts for MFA on privileged developer accounts, dependency selection and monitoring, tests, secret prevention, review, a security policy, signed releases, SBOMs, and SLSA. |
| Limits | It is broad guidance; individual changes need stack-specific validation. |

<a id="p04"></a>
### P04 — GitHub Actions hardening documentation

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; unavailable (404) |
| URL | [GitHub Actions hardening documentation](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-your-deployments) |
| Date read / attempted | 2026-09-27 |
| Supports | No rule recorded: the requested documentation URL returned 404 during this pass. |
| Limits | Use a current GitHub Docs URL before turning this into a normative checklist item. Correct current path was read as S21. |

<a id="p05"></a>
### P05 — OpenSSF Scorecard beginner checks for GitHub workflows

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read |
| URL | [OpenSSF Scorecard beginner checks for GitHub workflows](https://github.com/ossf/scorecard/blob/main/docs/beginner-checks.md) |
| Date read / attempted | 2026-09-27 |
| Supports | Default workflow token permissions should be restrictive and each action should receive only permissions it needs. |
| Limits | This does not establish a complete GitHub repository-security baseline. |

<a id="p06"></a>
### P06 — npm trusted publishing

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read |
| URL | [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/) |
| Date read / attempted | 2026-09-27 |
| Supports | npm can use a configured OIDC trusted publisher from supported cloud CI, avoiding long-lived publish tokens; public packages from public repositories can receive automatic provenance. |
| Limits | Only applies to npm publication, and provenance has documented public-repository limitations. |

<a id="p07"></a>
### P07 — PyPI trusted publishers

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read |
| URL | [PyPI trusted publishers](https://docs.pypi.org/trusted-publishers/) |
| Date read / attempted | 2026-09-27 |
| Supports | PyPI can exchange CI OIDC identity for a short-lived, project-scoped publishing token instead of placing a long-lived API token in CI. |
| Limits | Applies only to package publication workflows configured as trusted publishers. |

<a id="p08"></a>
### P08 — Supabase Row Level Security

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read |
| URL | [Supabase Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security) |
| Date read / attempted | 2026-09-27 |
| Supports | For every exposed table, pair least-privilege grants with operation-specific RLS policies and allow/deny tests; service-role/secret keys bypass RLS and belong only on the server. |
| Limits | The correct policies depend on the product's authorization model; migration and RLS-policy changes require explicit approval. |

<a id="p09"></a>
### P09 — Firebase Security Rules

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read, narrow support only |
| URL | [Firebase Security Rules](https://firebase.google.com/docs/rules) |
| Date read / attempted | 2026-09-27 |
| Supports | Firebase deployments need reviewed service-specific rules rather than relying on default open access. |
| Limits | Fetched page content was navigation-heavy in this pass; consult the service-specific Rules testing documentation before prescribing exact syntax. |

<a id="p10"></a>
### P10 — Vercel security documentation

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read, evidence extraction limited |
| URL | [Vercel security documentation](https://vercel.com/docs/security) |
| Date read / attempted | 2026-09-27 |
| Supports | Conditional hosting review point for Vercel projects. |
| Limits | Fetch completed but extracted body was elided by the tool output; no precise platform configuration rule is recorded. |

<a id="p11"></a>
### P11 — Netlify secure access documentation

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read, evidence extraction limited |
| URL | [Netlify secure access documentation](https://docs.netlify.com/security/secure-access-to-sites/) |
| Date read / attempted | 2026-09-27 |
| Supports | Conditional hosting review point for Netlify projects. |
| Limits | Fetch completed but extracted body was elided by the tool output; no precise platform configuration rule is recorded. |

<a id="p12"></a>
### P12 — Cloudflare account security documentation

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read, evidence extraction limited |
| URL | [Cloudflare account security documentation](https://developers.cloudflare.com/fundamentals/setup/account/account-security/) |
| Date read / attempted | 2026-09-27 |
| Supports | Conditional hosting review point for Cloudflare projects. |
| Limits | Fetch completed but extracted body was elided by the tool output; no precise platform configuration rule is recorded. |

<a id="p13"></a>
### P13 — AWS shared responsibility model

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read, evidence extraction limited |
| URL | [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) |
| Date read / attempted | 2026-09-27 |
| Supports | Conditional AWS review should distinguish AWS-managed infrastructure responsibilities from customer configuration responsibilities. |
| Limits | The shared-responsibility model does not provide resource-specific hardening settings. |

<a id="p14"></a>
### P14 — Amazon S3 Block Public Access

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read, evidence extraction limited |
| URL | [Amazon S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Public-storage exposure is a conditional launch check for S3-backed uploads and assets. |
| Limits | Fetched as primary documentation but no exact configuration assertion is recorded here because the output was elided. Owner added direct official page S31. |

<a id="p15"></a>
### P15 — Stripe webhook signature verification

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read |
| URL | [Stripe webhook signature verification](https://docs.stripe.com/webhooks/signature) |
| Date read / attempted | 2026-09-27 |
| Supports | Verify Stripe-Signature using the endpoint secret and the unchanged UTF-8 request body; body parsers must not alter the webhook body before verification. |
| Limits | This does not by itself define event replay handling or application business logic. |

<a id="p16"></a>
### P16 — Stripe idempotent requests

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read, evidence extraction limited |
| URL | [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) |
| Date read / attempted | 2026-09-27 |
| Supports | Conditional payments module should review idempotency for client retries. |
| Limits | Fetched as primary documentation but no exact configuration assertion is recorded here because the output was elided. Owner completed direct reading in S27. |

<a id="p17"></a>
### P17 — Next.js environment variables

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read, narrow support only |
| URL | [Next.js environment variables](https://nextjs.org/docs/app/guides/environment-variables) |
| Date read / attempted | 2026-09-27 |
| Supports | `NEXT_PUBLIC_` is a client-exposure marker and must be treated as unsuitable for secrets. |
| Limits | Exact page content was elided in the combined fetch; verify the current framework wording before citation in a public skill. Owner added direct official page S30; no unverified runtime-version claim. |

<a id="p18"></a>
### P18 — Vite environment variables and modes

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read |
| URL | [Vite environment variables and modes](https://vite.dev/guide/env-and-mode) |
| Date read / attempted | 2026-09-27 |
| Supports | `VITE_` values are bundled into client source, so they must not contain sensitive values; local env files should be ignored by Git. |
| Limits | The prefix rule is Vite-specific and is not a generic secret-detection rule. |

<a id="p19"></a>
### P19 — Express behind proxies

| Field | Evidence |
| --- | --- |
| Edition / status | unversioned; read |
| URL | [Express behind proxies](https://expressjs.com/en/guide/behind-proxies.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Rate-limiting and logging should use a client IP derived from a proxy setup that exactly matches deployment; blindly setting `trust proxy` to true can allow client-supplied forwarded headers to control the value. |
| Limits | The proper trust configuration depends on the actual proxy chain and must be tested in that deployment topology. |

<a id="s01"></a>
### S01 — MITRE CWE Top 25

| Field | Evidence |
| --- | --- |
| Edition / status | 2025; current landing page lists this year; read |
| URL | [MITRE CWE Top 25](https://cwe.mitre.org/top25/) |
| Date read / attempted | 2026-09-27 |
| Supports | Prioritization context for recurring software weakness classes. |
| Limits | Population ranking is not an application-specific risk score. |

<a id="s02"></a>
### S02 — NIST Secure Software Development Framework

| Field | Evidence |
| --- | --- |
| Edition / status | SP 800-218 / SSDF 1.1; final February 2022; read |
| URL | [NIST Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) |
| Date read / attempted | 2026-09-27 |
| Supports | Lifecycle practices, security requirements, release integrity and vulnerability response. |
| Limits | A framework to tailor, not a certification or automatic checklist. |

<a id="s03"></a>
### S03 — NIST SSDF revision

| Field | Evidence |
| --- | --- |
| Edition / status | SP 800-218 Rev. 1 / 1.2; initial public draft, December 17 2025; read |
| URL | [NIST SSDF revision](https://csrc.nist.gov/pubs/sp/800/218/r1/ipd) |
| Date read / attempted | 2026-09-27 |
| Supports | Identifies the newer draft and prevents presenting it as the final baseline. |
| Limits | Draft status explicit; normative recommendations use S02 until a final successor is verified. |

<a id="s04"></a>
### S04 — NIST Digital Identity Guidelines: Authentication

| Field | Evidence |
| --- | --- |
| Edition / status | SP 800-63B-4; final July 2025; read |
| URL | [NIST Digital Identity Guidelines: Authentication](https://csrc.nist.gov/pubs/sp/800/63/b/4/final) |
| Date read / attempted | 2026-09-27 |
| Supports | Confirms the current revision and its authentication scope. |
| Limits | Government-system scope; do not claim every commercial app is legally bound by it. |

<a id="s05"></a>
### S05 — NIST authenticator requirements

| Field | Evidence |
| --- | --- |
| Edition / status | 800-63B-4, section 3; read |
| URL | [NIST authenticator requirements](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/) |
| Date read / attempted | 2026-09-27 |
| Supports | Password-only minimum is 15 characters; MFA passwords may use 8. Supports blocklists and avoiding composition rules and routine forced changes. |
| Limits | Separate centrally checked passwords from device unlock secrets; changes to existing auth require approval. |

<a id="s06"></a>
### S06 — CISA Secure by Design hub and joint guidance

| Field | Evidence |
| --- | --- |
| Edition / status | Current hub unavailable; October 2023 joint paper seen in primary-source index; partial / access limited |
| URL | [CISA Secure by Design hub and joint guidance](https://www.cisa.gov/securebydesign) |
| Date read / attempted | 2026-09-27 |
| Supports | Source discovery only; an indexed primary extract describes manufacturer responsibility and secure defaults. |
| Limits | Hub returned 403; PDF retrieval failed, and partner PDF exceeded tool size. Do not claim full paper review or newest CISA edition. Use S07/S02 for supported principles. |

<a id="s07"></a>
### S07 — ASD Secure by Design foundations

| Field | Evidence |
| --- | --- |
| Edition / status | July 2024 document; HTML last updated July 30 2024; read |
| URL | [ASD Secure by Design foundations](https://www.cyber.gov.au/business-government/secure-design/secure-by-design/secure-by-design-foundations) |
| Date read / attempted | 2026-09-27 |
| Supports | Security defaults and lifecycle ownership as design responsibilities. |
| Limits | Partner-government guidance, not a substitute for inaccessible CISA publication verification. |

<a id="s08"></a>
### S08 — MDN Web Security

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling documentation; read |
| URL | [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security) |
| Date read / attempted | 2026-09-27 |
| Supports | Browser-facing controls: HTTPS, safer content handling, cookie restrictions and cross-origin boundaries. |
| Limits | Choose applicable controls; no operational environment or application has been audited. |

<a id="s09"></a>
### S09 — Mozilla HTTP Observatory tests and scoring

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling documentation; read |
| URL | [Mozilla HTTP Observatory tests and scoring](https://developer.mozilla.org/en-US/observatory/docs/tests_and_scoring) |
| Date read / attempted | 2026-09-27 |
| Supports | Browser-header checks and interpretation of their grades. |
| Limits | Grade is a signal, not proof of authorization, tenant separation or complete security; no remote scan was run. |

<a id="s10"></a>
### S10 — Security disclosure file format

| Field | Evidence |
| --- | --- |
| Edition / status | RFC 9116; read |
| URL | [Security disclosure file format](https://www.rfc-editor.org/rfc/rfc9116.html) |
| Date read / attempted | 2026-09-27 |
| Supports | A discoverable security contact with expiry, normally at /.well-known/security.txt over HTTPS. |
| Limits | Use a user-approved real contact; a placeholder contact is not a completed disclosure channel. |

<a id="s11"></a>
### S11 — MDN CSP Report-Only

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling documentation; read |
| URL | [MDN CSP Report-Only](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy-Report-Only) |
| Date read / attempted | 2026-09-27 |
| Supports | Trial a policy while observing violations before enforcement. |
| Limits | Report-Only does not block violations. External reporting destinations need separate data-sharing approval. |

<a id="s12"></a>
### S12 — MDN Strict-Transport-Security

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling documentation; read |
| URL | [MDN Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security) |
| Date read / attempted | 2026-09-27 |
| Supports | HSTS relies on an HTTPS response; subdomain scope and preload require care. |
| Limits | An HTTP localhost header check cannot prove HTTPS enforcement; do not casually add preload or includeSubDomains. |

<a id="s13"></a>
### S13 — MDN CORS

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling documentation; read |
| URL | [MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) |
| Date read / attempted | 2026-09-27 |
| Supports | Credentialed browser access needs explicit allowed origins; public noncredentialed resources can allow all origins. |
| Limits | CORS controls browser response access, not caller authorization or all cross-site requests. |

<a id="s14"></a>
### S14 — Electron security guidance

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling latest documentation; no app-version claim; read |
| URL | [Electron security guidance](https://www.electronjs.org/docs/latest/tutorial/security) |
| Date read / attempted | 2026-09-27 |
| Supports | Renderer isolation, sandboxing, remote-content and privileged-bridge boundaries. |
| Limits | Only applicable to Electron; another desktop runtime needs its own official guidance. |

<a id="s15"></a>
### S15 — MCP authorization specification

| Field | Evidence |
| --- | --- |
| Edition / status | 2026-07-28; latest specification redirected here; read |
| URL | [MCP authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) |
| Date read / attempted | 2026-09-27 |
| Supports | Validate access-token audience and use constrained authorization scopes. |
| Limits | Map controls to the detected transport and SDK version; reading docs does not authorize connector changes. |

<a id="s16"></a>
### S16 — MCP security best practices

| Field | Evidence |
| --- | --- |
| Edition / status | Draft documentation; read |
| URL | [MCP security best practices](https://modelcontextprotocol.io/docs/draft/tutorials/security/security_best_practices) |
| Date read / attempted | 2026-09-27 |
| Supports | Threat discovery: confused deputy, unsafe token forwarding, SSRF and local-server execution. |
| Limits | Draft is supplementary; use S15 for stable normative authorization requirements. |

<a id="s17"></a>
### S17 — Django deployment checklist

| Field | Evidence |
| --- | --- |
| Edition / status | Stable redirect resolved to Django 6.1; read |
| URL | [Django deployment checklist](https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/) |
| Date read / attempted | 2026-09-27 |
| Supports | Check production debug settings, hosts and environment-specific deployment configuration. |
| Limits | Installed applications may use a different supported version; inspect their manifests first. |

<a id="s18"></a>
### S18 — FastAPI behind a proxy

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling documentation; read |
| URL | [FastAPI behind a proxy](https://fastapi.tiangolo.com/advanced/behind-a-proxy/) |
| Date read / attempted | 2026-09-27 |
| Supports | Forwarded headers should be accepted from known proxy addresses. |
| Limits | Trusting all sources is only appropriate under an enforced proxy-only network boundary; inspect topology. |

<a id="s19"></a>
### S19 — EU General Data Protection Regulation

| Field | Evidence |
| --- | --- |
| Edition / status | Regulation (EU) 2016/679; read |
| URL | [EU General Data Protection Regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) |
| Date read / attempted | 2026-09-27 |
| Supports | When applicable, data minimization, retention, security and an appropriate processing basis need attention. |
| Limits | No jurisdiction or lawful-basis determination made. Consent is not the only possible basis; legal decisions stay with the user and qualified advisers. |

<a id="s20"></a>
### S20 — SLSA specification

| Field | Evidence |
| --- | --- |
| Edition / status | 1.2 / Approved; read |
| URL | [SLSA specification](https://slsa.dev/spec/v1.2/) |
| Date read / attempted | 2026-09-27 |
| Supports | Current supply-chain framework with build/source tracks and provenance. |
| Limits | Supersedes P02 as this research baseline; provenance alone does not establish safe behavior or a SLSA level. |

<a id="s21"></a>
### S21 — GitHub Actions secure use

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling documentation; read |
| URL | [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use) |
| Date read / attempted | 2026-09-27 |
| Supports | Least workflow privilege, handling untrusted event data safely, and full commit-SHA references for third-party actions. |
| Limits | An immutable action can still be unsafe; inspect source and update deliberately. Replaces unavailable P04. |

<a id="s22"></a>
### S22 — GitHub repository-security quickstart

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling documentation; read |
| URL | [GitHub repository-security quickstart](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository) |
| Date read / attempted | 2026-09-27 |
| Supports | Repository security-policy and security-feature setup pointers. |
| Limits | Plan availability and dashboard state are not verified from local files; user performs remote setup. |

<a id="s23"></a>
### S23 — npm publishing 2FA requirements

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling documentation; read |
| URL | [npm publishing 2FA requirements](https://docs.npmjs.com/requiring-2fa-for-package-publishing-and-settings-modification/) |
| Date read / attempted | 2026-09-27 |
| Supports | Maintainer authentication and package publishing protections. |
| Limits | Account settings and publication remain user actions; recheck supported publishing paths before implementation. |

<a id="s24"></a>
### S24 — MASVS release ledger

| Field | Evidence |
| --- | --- |
| Edition / status | 2.1.0 marked Latest; read |
| URL | [MASVS release ledger](https://github.com/OWASP/masvs/releases) |
| Date read / attempted | 2026-09-27 |
| Supports | Confirms stable mobile baseline including privacy controls. |
| Limits | O05 is live documentation; pin a release for precise requirements. Do not reuse old MASVS level labels uncritically. |

<a id="s25"></a>
### S25 — MASTG release ledger

| Field | Evidence |
| --- | --- |
| Edition / status | 2.0.0 marked Latest; first stable v2 framework; read |
| URL | [MASTG release ledger](https://github.com/OWASP/mastg/releases) |
| Date read / attempted | 2026-09-27 |
| Supports | Confirms modular mobile test guidance and stable edition. |
| Limits | Use detected platform tools locally; missing device/emulator support must be reported. |

<a id="s26"></a>
### S26 — ASVS usage and verification levels

| Field | Evidence |
| --- | --- |
| Edition / status | Pinned v5.0.0; read |
| URL | [ASVS usage and verification levels](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x03-What-is-the-ASVS.md) |
| Date read / attempted | 2026-09-27 |
| Supports | L1 starts with essential defenses; L2 includes L1 and broader requirements; L3 adds the most demanding controls. Tailoring depends on application context. |
| Limits | A selected subset is ASVS-informed, not an ASVS certification. GitHub latest release alias also exposes bleeding-edge content; do not substitute it for v5.0.0. |

<a id="s27"></a>
### S27 — Stripe idempotent requests

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling API documentation; read |
| URL | [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) |
| Date read / attempted | 2026-09-27 |
| Supports | Use an operation-specific key to make supported API retries return the recorded outcome. |
| Limits | API request idempotency is different from deduplicating incoming webhook events; payment edits require separate approval. |

<a id="s28"></a>
### S28 — Supabase API key types

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling documentation; read |
| URL | [Supabase API key types](https://supabase.com/docs/guides/getting-started/api-keys) |
| Date read / attempted | 2026-09-27 |
| Supports | Distinguishes publishable/anon keys from privileged secret/service-role keys that bypass RLS. |
| Limits | Prefix presence is not proof of a leak. Assess privileges and RLS without displaying key values. |

<a id="s29"></a>
### S29 — Firebase basic security rules

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling documentation; read |
| URL | [Firebase basic security rules](https://firebase.google.com/docs/rules/basics) |
| Date read / attempted | 2026-09-27 |
| Supports | Tailor rules to authenticated users and the intended data access model rather than broad public access. |
| Limits | Product-specific rules differ; privileged server SDK paths also need server-side authorization. |

<a id="s30"></a>
### S30 — Next.js environment variables

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling App Router guide; selector showed 16.3.6; read |
| URL | [Next.js environment variables](https://nextjs.org/docs/app/guides/environment-variables) |
| Date read / attempted | 2026-09-27 |
| Supports | Investigate NEXT_PUBLIC_ variables as browser-exposure candidates alongside build artifacts. |
| Limits | Prefix is a signal, not proof a value is confidential; use version-specific instructions for the target app. |

<a id="s31"></a>
### S31 — Amazon S3 Block Public Access

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling service documentation; read |
| URL | [Amazon S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Inspect account/bucket public-access controls and deliberate public-object requirements. |
| Limits | Local IaC is only desired state; dashboard and actual resource state remain unverified. No AWS calls made. |

<a id="s32"></a>
### S32 — Vercel Deployment Protection

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling product documentation; read |
| URL | [Vercel Deployment Protection](https://vercel.com/docs/deployment-protection) |
| Date read / attempted | 2026-09-27 |
| Supports | Conditional review of preview/deployment access boundaries. |
| Limits | Do not assume features are included in a plan or that platform protection replaces app authorization. |

<a id="s33"></a>
### S33 — Cloudflare security guidance

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling documentation; read |
| URL | [Cloudflare security guidance](https://developers.cloudflare.com/fundamentals/security/) |
| Date read / attempted | 2026-09-27 |
| Supports | Conditional provider-security documentation entry point. |
| Limits | No account, origin lock-down or plan-specific settings verified; select implementation pages only when Cloudflare is detected. |

<a id="s34"></a>
### S34 — Auth0 production-deployment guidance

| Field | Evidence |
| --- | --- |
| Edition / status | Unconfirmed; unavailable |
| URL | [Auth0 production-deployment guidance](https://auth0.com/docs/deploy-monitor/deploy-applications/deploy-to-production) |
| Date read / attempted | 2026-09-27 |
| Supports | Conditional identity-provider pointer only. |
| Limits | Retrieval failed. No Auth0-specific checklist rule is derived; fetch current docs when provider is present. |

<a id="r01"></a>
### R01 — PortSwigger access-control guidance

| Field | Evidence |
| --- | --- |
| Edition / status | Unversioned practitioner material; read |
| URL | [PortSwigger access-control guidance](https://portswigger.net/web-security/access-control) |
| Date read / attempted | 2026-09-27 |
| Supports | Use resource-level authorization tests, including role and cross-user boundaries. |
| Limits | Practitioner evidence, corroborated by O03/O16/S26; no lab or attack was executed. |

<a id="r02"></a>
### R02 — Trail of Bits Testing Handbook

| Field | Evidence |
| --- | --- |
| Edition / status | Rolling practitioner handbook; read |
| URL | [Trail of Bits Testing Handbook](https://appsec.guide/) |
| Date read / attempted | 2026-09-27 |
| Supports | Choose deterministic analysis suited to the language and risk. |
| Limits | Tool discovery, not permission to install tools or run arbitrary rule downloads; corroborated by S02. |

<a id="r03"></a>
### R03 — Troy Hunt: Passwords Evolved

| Field | Evidence |
| --- | --- |
| Edition / status | Historical practitioner article; read |
| URL | [Troy Hunt: Passwords Evolved](https://www.troyhunt.com/passwords-evolved-authentication-guidance-for-the-modern-era/) |
| Date read / attempted | 2026-09-27 |
| Supports | Helpful explanation of credential reuse and usable authentication. |
| Limits | Do not inherit old numeric policy; use S04/S05/O09 for current requirements. |

<a id="r04"></a>
### R04 — Tanya Janca: Resources

| Field | Evidence |
| --- | --- |
| Edition / status | Unversioned practitioner material; read |
| URL | [Tanya Janca: Resources](https://shehackspurple.ca/resources/) |
| Date read / attempted | 2026-09-27 |
| Supports | Accessible teaching style for developers without a security background. |
| Limits | No technical control imported from the landing page. Linked securecodingguideline.com could not be retrieved. |

<a id="r05"></a>
### R05 — Jim Manico: Talks and workshops

| Field | Evidence |
| --- | --- |
| Edition / status | Page states last update May 13 2026; read |
| URL | [Jim Manico: Talks and workshops](https://manicode.com/talks.html) |
| Date read / attempted | 2026-09-27 |
| Supports | Coverage signal for secure coding, frontend boundaries, dependencies and AI/MCP. |
| Limits | Talk descriptions are not standards or verified talk transcripts; checklist authority remains OWASP/NIST. |

<a id="r06"></a>
### R06 — Latacora: Cryptographic right answers

| Field | Evidence |
| --- | --- |
| Edition / status | Historical 2018 practitioner article; read |
| URL | [Latacora: Cryptographic right answers](https://www.latacora.com/blog/cryptographic-right-answers/) |
| Date read / attempted | 2026-09-27 |
| Supports | Prefer established cryptographic constructions and proper password hashing. |
| Limits | Use current O09/S05 guidance; do not carry over historical preference ordering or custom crypto recipes. |

## Local inspiration and availability

Read the requested user-profile paths; missing files and fallback paths are distinguished below. No files from those skills were copied into this repository. The reference Lean repository was inspected read-only: runtime folder with SKILL.md and optional agents/openai.yaml, repository-level README/LICENSE/CHANGELOG/evals. We propose references/ as the requested additional runtime directory.

| Path | Read status | Useful pattern | Exclusions |
| --- | --- | --- | --- |
| C:\Users\aarav\.claude\skills\security-and-hardening\SKILL.md | read | Separate always-do, ask-first, and never-do changes; identify trust boundaries before selecting controls. | Do not reuse its prose, code samples, control lists, or exact decision wording. |
| C:\Users\aarav\.claude\skills\conducting-api-security-testing\SKILL.md | read | API test framing and authorization-safe testing boundaries. | Do not reuse its procedures, payloads, commands, or prose. |
| C:\Users\aarav\.claude\skills\hardening-docker-containers-for-production\SKILL.md | read | Container hardening scope and configuration review prompts. | Do not reuse its benchmark mappings, commands, or prose. |
| C:\Users\aarav\.claude\skills\detecting-indirect-prompt-injection\SKILL.md | read | Treat retrieved documents and other indirect content as untrusted before model ingestion. | Do not reuse its pipeline, detector selections, validation criteria, or prose. |
| C:\Users\aarav\.claude\skills\detecting-ai-model-prompt-injection-attacks\SKILL.md | read | Defense-in-depth framing for direct and indirect prompt injection. | Do not reuse its install instructions, detector parameters, code, or prose. |
| C:\Users\aarav\.claude\skills\auditing-mcp-servers-for-tool-poisoning\SKILL.md | read | MCP-specific focus on untrusted tool metadata, permissions, authentication, SSRF, and change detection. | Do not reuse its scanner workflow, probes, commands, mappings, or prose. |
| C:\Users\aarav\.claude\skills\detecting-supply-chain-attacks-in-ci-cd\SKILL.md | read | Workflow inventory: unpinned actions, expression-to-shell flow, excess token access, third-party write access, and dependency confusion. | Do not copy its scripts, examples, threat labels, or scanner workflow. |
| C:\Users\aarav\.claude\skills\detecting-malicious-npm-packages\SKILL.md | read | Treat package lifecycle scripts and package acquisition as potentially executable; prefer static inspection and isolation for any malware triage. | Do not copy its lengthy procedure, commands, examples, or unverified campaign claims. |
| C:\Users\aarav\.claude\skills\detecting-dependency-confusion\SKILL.md | read | Check internal package naming and registry-source restrictions when a project mixes public and private registries. | Do not copy its testing tools, implementation instructions, examples, or historical claims. |
| C:\Users\aarav\.claude\skills\aws-security\SKILL.md | read | Keep cloud inspection read-only, avoid unsupported conclusions, and summarize sensitive findings. | Do not copy its service-routing rules or operational API instructions. |
| C:\Users\aarav\.claude\skills\auditing-cloud-with-cis-benchmarks\SKILL.md | read | A cloud module should distinguish a posture review from application testing and require authorized scope. | Do not copy benchmark mappings, vendor tooling instructions, claims, or remediation timelines. |
| C:\Users\aarav\.claude\skills\conducting-gdpr-compliance-assessment\SKILL.md | read | When personal data is in scope, inventory data purposes, retention, processors, and rights as a separate user-owned launch track. | Do not copy legal interpretations, regional claims, templates, calculations, or procedural text. |
| C:\Users\aarav\.codex\skills\security-ownership-map\SKILL.md | read by owner; not executed | Optional ownership-maintenance context for larger repos. | No mandatory graph analysis, dependency installation or bus-factor claims for a small launch pass. |
| C:\Users\aarav\.agents\skills\security-and-hardening\SKILL.md | read by owner; explicitly invoked | Trust-boundary inventory, conditional checks, evidence and permission distinctions. | No verbatim prose/code, fixed bcrypt cost as universal policy, automatic CSP enforcement, secret-printing grep, blanket wildcard-CORS accusations, universal consent claims, or unsupported statistics. |

Codex security capability exposed and read: `security-ownership-map`. The runtime tool inventory exposed no dedicated Codex Security connector; its presence was not inferred from a recommended-plugin list. General engineering guardrails are not presented as that product. No ownership-map scripts ran.

## Decisions to carry into Phase 2

1. **Evidence is separate from action.** Preserve the four requested friendly action statuses. Add an evidence field: observed, failed, not run, or unavailable. “Already in place” requires a cited file plus a relevant check where feasible; configuration alone does not prove live deployment state. “I'll add this” means planned, not completed. Unknown items stay unresolved, never “Not needed”.
2. **Specific approval rules win.** Payment webhooks belong to the per-item payment gate. Session-semantic cookie/auth changes also need that gate. CSP monitoring may be proposed after plan approval, but enforcement remains separately approved. Approval covers concrete local changes, not deployment or dashboard actions.
3. **Protect secrets during inspection.** Do not open raw secret files or show candidate values. An installed scanner may process local bytes with redacted output; the model receives only file/line/rule IDs. A pattern fallback must suppress matched text. `.gitignore` does not untrack committed material or revoke keys. Key rotation stays with the user. [O14](#o14), [S21](#s21)
4. **Distinguish real boundaries.** A key in a public variable is a concern only if it grants confidential privileges; Supabase publishable keys can be public, secret/service-role keys cannot. CORS is not authorization. Logins and AI work need endpoint/user budgets; trusted-proxy IP handling cannot be guessed from a header. [S28](#s28), [S13](#s13), [P19](#p19)
5. **Local means local.** Test an isolated copy with synthetic data, loopback addresses, request caps/timeouts and outbound access disabled. A loopback server that calls Stripe/LLM providers is not isolated until its integrations are mocked. No hosted Observatory scan, registry probe or production load test. Audit commands often contact advisory services; either use supported offline data or mark unavailable and ask for a narrowly scoped advisory-query exception. Do not silently install scanners or dependencies.
6. **Verification must exercise the gap.** A 429 alone is insufficient if changing spoofed forwarding headers resets the limit. Tenant denial must also show that the correct tenant can read its own record. Removing a key from source must include a freshly built client artifact check. Keep valid webhook cases alongside invalid signatures; deduplicate repeated local events without calling Stripe. [O03](#o03), [P19](#p19), [P15](#p15), [S27](#s27)
7. **Keep the checklist proportional.** Authentication, Kubernetes and payments are not universal requirements. Sensitive personal/health/children's data raises the need for explicit owner decisions and specialist review; no compliance certificate or blanket legal conclusion. [S19](#s19), [S26](#s26)

## Comparables and alternatives

| Approach | Transfers | Tradeoff / reason not to copy wholesale |
| --- | --- | --- |
| Local security-and-hardening skill | Practical implementation categories and trust-boundary thinking | Its universal rules, code examples and phrasing are too broad for this positive, profile-driven launch checklist. |
| OWASP ASVS + Cheat Sheets | Requirements taxonomy and targeted implementation references | Shipping the whole standard would overload small projects; use original control records linked to sources. |
| OpenSSF concise guide | Short developer-facing lifecycle guidance | Package/CI controls alone do not cover SaaS tenancy, mobile or AI permissions. |
| Recommended: portable Markdown + profile/module selectors | Matches existing library, no mandatory runtime service | More editorial maintenance; source editions and stack-specific verification need periodic rechecking. |
| Alternative: executable scanner wrapper | More repeatable measurements for supported stacks | Installation, tool/version drift, execution permissions and network handling increase scope. Reconsider only after real usage shows repeated manual verification that a small helper can safely automate. |

## Next work and proof — not run

After review: design the short router and concrete control schema, implement reference files/README/license/metadata, then run exactly four isolated Codex fixture cases once each. Fixtures use clearly synthetic secrets, never usable credentials. Record failures and unrun checks without retries. Separate a denied/ask-first payment or policy change from automatic remediation; no fixture can both prohibit the edit and require a fixed result without an explicit approval stage. Tests should observe the approval request, provide the predeclared narrow authorization if included in the protocol, then verify behavior within that same single trial. Without authorization, the expected result is an honest pending item, not a false pass.

The first useful proof is the Express fixture: correct profile/modules, credential-aware CORS decision, local bounded login requests reaching 429, spoof-resistant identity handling, and a payment item held for approval. No behavioral success is claimed now.


## Approved Phase 2 changes — 2026-09-27

User approved secure-launch and the direction, then revised priorities and added controls. COVERAGE-MATRIX.md and runtime priorities now supersede the Phase 1 proposal. Mobile is explicitly starter coverage. Additional primary-source records N01–N07 are in the runtime sources ledger and research-ledger.json. No original research access limit has been silently removed.
