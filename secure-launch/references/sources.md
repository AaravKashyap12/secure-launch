# Dated sources

Read/attempt date 2026-09-27. Rolling pages can change; final, draft and unavailable records remain distinct. Use only claims supported by the record, and prefer the detected framework’s own version. Research history and full limits are in the repository RESEARCH.md. Original guidance here does not relicense third-party prose.

<a id="o01"></a>
## O01 — OWASP Top 10:2025

- Edition: 2025 final release; read/attempted 2026-09-27; read.
- Source: https://owasp.org/Top10/2025/
- Supports: A web-app baseline covering access control, configuration, supply chain, crypto, injection, design, authentication, integrity, logging, and exceptional-condition handling.
- Limits: An awareness taxonomy, not a project-specific checklist or proof that a control works.

<a id="o02"></a>
## O02 — OWASP Application Security Verification Standard

- Edition: 5.0.0 stable; read/attempted 2026-09-27; read; level-detail gap recorded.
- Source: https://asvs.owasp.org/
- Supports: A versioned catalogue of web-application verification requirements; its levels are assurance-depth selections for scoping verification, not a generic ranking of product risk.
- Limits: The landing page confirmed 5.0.0 but did not expose the detailed level definitions in the fetched extract; cite the version with individual requirements before prescribing a level. Owner resolved level wording using pinned source S26.

<a id="o03"></a>
## O03 — OWASP API Security Top 10

- Edition: 2023 final edition; read/attempted 2026-09-27; read.
- Source: https://owasp.org/API-Security/editions/2023/en/0x11-t10/
- Supports: API checks for object and function authorization, authentication, resource consumption, sensitive business flows, SSRF, configuration, inventory, and third-party API use.
- Limits: API-focused guidance; it does not replace web, mobile, or cloud configuration guidance.

<a id="o04"></a>
## O04 — OWASP Top 10 for LLM Applications and Generative AI

- Edition: 2025; read/attempted 2026-09-27; read.
- Source: https://genai.owasp.org/llm-top-10/
- Supports: AI-feature modules for prompt injection, sensitive-data disclosure, supply chain, poisoning, output handling, agency, prompt leakage, vector/embedding isolation, misinformation, and bounded consumption.
- Limits: A risk catalogue; each application still needs code-enforced authorization, validation, and product-specific abuse controls.

<a id="o05"></a>
## O05 — OWASP Mobile Application Security Verification Standard

- Edition: rolling documentation; exact release unknown; read/attempted 2026-09-27; read.
- Source: https://mas.owasp.org/MASVS/
- Supports: Mobile modules for storage, cryptography, authentication/authorization, network communication, platform interaction, code quality, resilience, and privacy.
- Limits: The fetched page did not display a release number; do not label it with an inferred version. Release number resolved by S24: 2.1.0.

<a id="o06"></a>
## O06 — OWASP Mobile Application Security Testing Guide

- Edition: rolling documentation; exact release unknown; read/attempted 2026-09-27; read.
- Source: https://mas.owasp.org/MASTG/
- Supports: Mobile testing references aligned to the MAS project, useful when a repository contains a native mobile app.
- Limits: The fetched page did not display a release number; it is testing guidance and does not establish compliance by itself. Release number resolved by S25: 2.0.0.

<a id="o07"></a>
## O07 — OWASP Authentication Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- Supports: Authentication flows: generic failure handling, automated-attack resistance, MFA, and event monitoring.
- Limits: Choose controls and thresholds for the product; the page is not a turnkey authentication design.

<a id="o08"></a>
## O08 — OWASP Session Management Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- Supports: Session-cookie and lifecycle checks when an app uses browser sessions.
- Limits: Applies differently to token-based native and service-to-service clients.

<a id="o09"></a>
## O09 — OWASP Password Storage Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
- Supports: Password-hash storage checks for applications that own password verification.
- Limits: Does not apply when an external identity provider alone owns passwords.

<a id="o10"></a>
## O10 — OWASP Input Validation Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
- Supports: Boundary validation and allow-list-oriented handling for untrusted request data.
- Limits: Validation complements output encoding and authorization; it is not a substitute for either.

<a id="o11"></a>
## O11 — OWASP Cross-Site Request Forgery Prevention Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
- Supports: CSRF protections for state-changing browser requests authenticated by cookies.
- Limits: Usually not applicable to non-browser or bearer-token-only flows; confirm the client/auth model.

<a id="o12"></a>
## O12 — OWASP Server-Side Request Forgery Prevention Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html
- Supports: Controls for server-side URL fetching, including allowlisting and network-boundary safeguards.
- Limits: Only applies when the service follows user- or content-influenced URLs; DNS and redirect behavior need stack-specific handling.

<a id="o13"></a>
## O13 — OWASP File Upload Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
- Supports: Upload controls such as allowed formats, size bounds, storage separation, and handling of untrusted files.
- Limits: Applies only to upload or import features; malware scanning and retention are deployment choices.

<a id="o14"></a>
## O14 — OWASP Secrets Management Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- Supports: Secret lifecycle, access, rotation, and non-disclosure practices for source and runtime configuration.
- Limits: A local source scan can detect patterns but cannot prove a credential is valid or safely rotated.

<a id="o15"></a>
## O15 — OWASP Logging Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
- Supports: Security-event logging and safe treatment of sensitive or untrusted log data.
- Limits: Logging policy is not monitoring coverage; operational retention and alerting require environment-specific setup.

<a id="o16"></a>
## O16 — OWASP REST Security Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html
- Supports: HTTPS, endpoint-local access control, and token/API design checks for REST services.
- Limits: Designed for REST-style APIs; do not use it as the sole reference for GraphQL or browser pages.

<a id="o17"></a>
## O17 — OWASP GraphQL Security Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html
- Supports: GraphQL validation, authorization, query-cost, batching, and introspection-aware review.
- Limits: Applies only when GraphQL is present; schema and resolver behavior still need local inspection.

<a id="o18"></a>
## O18 — OWASP Node.js Security Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html
- Supports: Node-specific application, error, server, and platform hardening pointers.
- Limits: Framework and hosting defaults vary; validate against the actual Node stack.

<a id="o19"></a>
## O19 — OWASP Django Security Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Django_Security_Cheat_Sheet.html
- Supports: Django checks including production debug state, built-in authentication protections, dependency upkeep, and throttling options.
- Limits: Django defaults can be overridden; inspect settings and deployment configuration locally.

<a id="o20"></a>
## O20 — OWASP Docker Security Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html
- Supports: Container checks such as timely updates, avoiding Docker-socket exposure, and running as an unprivileged user.
- Limits: Container image review does not assess the host or orchestrator configuration.

<a id="o21"></a>
## O21 — OWASP Kubernetes Security Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html
- Supports: Cluster host, component, build, deployment, and runtime security coverage.
- Limits: Use only where Kubernetes manifests or a cluster target exist; local manifests cannot prove managed-cluster posture.

<a id="o22"></a>
## O22 — OWASP HTTP Headers Cheat Sheet

- Edition: unversioned rolling cheat sheet; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html
- Supports: Response-header choices, including browser-facing security headers and deployment considerations.
- Limits: A Content Security Policy needs staged, app-specific validation; headers should be checked against a local response.

<a id="o23"></a>
## O23 — OWASP Cheat Sheet Series

- Edition: unversioned rolling collection; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/
- Supports: The collection and maintenance context for the topical cheat sheets above.
- Limits: An index, not a single prescriptive launch standard.

<a id="p01"></a>
## P01 — OpenSSF Scorecard README and checks

- Edition: unversioned; read/attempted 2026-09-27; read.
- Source: https://github.com/ossf/scorecard
- Supports: A release checklist can inspect public-repository practices such as workflow risks, branch protection, token permissions, packaging, and signed releases.
- Limits: Scorecard is an assessment tool and does not replace repository-specific review.

<a id="p02"></a>
## P02 — SLSA Security levels

- Edition: v1.1; read/attempted 2026-09-27; read.
- Source: https://slsa.dev/spec/v1.1/levels
- Supports: Build L1 records provenance, L2 requires hosted signed provenance and consumer validation, and L3 adds hardened build isolation.
- Limits: SLSA describes supply-chain guarantees; it does not assess application authorization or runtime configuration. Owner confirmed Approved v1.2 in S20; v1.1 is historical, not the current baseline.

<a id="p03"></a>
## P03 — Concise Guide for Developing More Secure Software

- Edition: 2023-06-14; read/attempted 2026-09-27; read.
- Source: https://best.openssf.org/Concise-Guide-for-Developing-More-Secure-Software
- Supports: Checklist prompts for MFA on privileged developer accounts, dependency selection and monitoring, tests, secret prevention, review, a security policy, signed releases, SBOMs, and SLSA.
- Limits: It is broad guidance; individual changes need stack-specific validation.

<a id="p04"></a>
## P04 — GitHub Actions hardening documentation

- Edition: unversioned; read/attempted 2026-09-27; unavailable (404).
- Source: https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-your-deployments
- Supports: No rule recorded: the requested documentation URL returned 404 during this pass.
- Limits: Use a current GitHub Docs URL before turning this into a normative checklist item. Correct current path was read as S21.

<a id="p05"></a>
## P05 — OpenSSF Scorecard beginner checks for GitHub workflows

- Edition: unversioned; read/attempted 2026-09-27; read.
- Source: https://github.com/ossf/scorecard/blob/main/docs/beginner-checks.md
- Supports: Default workflow token permissions should be restrictive and each action should receive only permissions it needs.
- Limits: This does not establish a complete GitHub repository-security baseline.

<a id="p06"></a>
## P06 — npm trusted publishing

- Edition: unversioned; read/attempted 2026-09-27; read.
- Source: https://docs.npmjs.com/trusted-publishers/
- Supports: npm can use a configured OIDC trusted publisher from supported cloud CI, avoiding long-lived publish tokens; public packages from public repositories can receive automatic provenance.
- Limits: Only applies to npm publication, and provenance has documented public-repository limitations.

<a id="p07"></a>
## P07 — PyPI trusted publishers

- Edition: unversioned; read/attempted 2026-09-27; read.
- Source: https://docs.pypi.org/trusted-publishers/
- Supports: PyPI can exchange CI OIDC identity for a short-lived, project-scoped publishing token instead of placing a long-lived API token in CI.
- Limits: Applies only to package publication workflows configured as trusted publishers.

<a id="p08"></a>
## P08 — Supabase Row Level Security

- Edition: unversioned; read/attempted 2026-09-27; read.
- Source: https://supabase.com/docs/guides/database/postgres/row-level-security
- Supports: For every exposed table, pair least-privilege grants with operation-specific RLS policies and allow/deny tests; service-role/secret keys bypass RLS and belong only on the server.
- Limits: The correct policies depend on the product's authorization model; migration and RLS-policy changes require explicit approval.

<a id="p09"></a>
## P09 — Firebase Security Rules

- Edition: unversioned; read/attempted 2026-09-27; read, narrow support only.
- Source: https://firebase.google.com/docs/rules
- Supports: Firebase deployments need reviewed service-specific rules rather than relying on default open access.
- Limits: Fetched page content was navigation-heavy in this pass; consult the service-specific Rules testing documentation before prescribing exact syntax.

<a id="p10"></a>
## P10 — Vercel security documentation

- Edition: unversioned; read/attempted 2026-09-27; read, evidence extraction limited.
- Source: https://vercel.com/docs/security
- Supports: Conditional hosting review point for Vercel projects.
- Limits: Fetch completed but extracted body was elided by the tool output; no precise platform configuration rule is recorded.

<a id="p11"></a>
## P11 — Netlify secure access documentation

- Edition: unversioned; read/attempted 2026-09-27; read, evidence extraction limited.
- Source: https://docs.netlify.com/security/secure-access-to-sites/
- Supports: Conditional hosting review point for Netlify projects.
- Limits: Fetch completed but extracted body was elided by the tool output; no precise platform configuration rule is recorded.

<a id="p12"></a>
## P12 — Cloudflare account security documentation

- Edition: unversioned; read/attempted 2026-09-27; read, evidence extraction limited.
- Source: https://developers.cloudflare.com/fundamentals/setup/account/account-security/
- Supports: Conditional hosting review point for Cloudflare projects.
- Limits: Fetch completed but extracted body was elided by the tool output; no precise platform configuration rule is recorded.

<a id="p13"></a>
## P13 — AWS shared responsibility model

- Edition: unversioned; read/attempted 2026-09-27; read, evidence extraction limited.
- Source: https://aws.amazon.com/compliance/shared-responsibility-model/
- Supports: Conditional AWS review should distinguish AWS-managed infrastructure responsibilities from customer configuration responsibilities.
- Limits: The shared-responsibility model does not provide resource-specific hardening settings.

<a id="p14"></a>
## P14 — Amazon S3 Block Public Access

- Edition: unversioned; read/attempted 2026-09-27; read, evidence extraction limited.
- Source: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html
- Supports: Public-storage exposure is a conditional launch check for S3-backed uploads and assets.
- Limits: Fetched as primary documentation but no exact configuration assertion is recorded here because the output was elided. Owner added direct official page S31.

<a id="p15"></a>
## P15 — Stripe webhook signature verification

- Edition: unversioned; read/attempted 2026-09-27; read.
- Source: https://docs.stripe.com/webhooks/signature
- Supports: Verify Stripe-Signature using the endpoint secret and the unchanged UTF-8 request body; body parsers must not alter the webhook body before verification.
- Limits: This does not by itself define event replay handling or application business logic.

<a id="p16"></a>
## P16 — Stripe idempotent requests

- Edition: unversioned; read/attempted 2026-09-27; read, evidence extraction limited.
- Source: https://docs.stripe.com/api/idempotent_requests
- Supports: Conditional payments module should review idempotency for client retries.
- Limits: Fetched as primary documentation but no exact configuration assertion is recorded here because the output was elided. Owner completed direct reading in S27.

<a id="p17"></a>
## P17 — Next.js environment variables

- Edition: unversioned; read/attempted 2026-09-27; read, narrow support only.
- Source: https://nextjs.org/docs/app/guides/environment-variables
- Supports: `NEXT_PUBLIC_` is a client-exposure marker and must be treated as unsuitable for secrets.
- Limits: Exact page content was elided in the combined fetch; verify the current framework wording before citation in a public skill. Owner added direct official page S30; no unverified runtime-version claim.

<a id="p18"></a>
## P18 — Vite environment variables and modes

- Edition: unversioned; read/attempted 2026-09-27; read.
- Source: https://vite.dev/guide/env-and-mode
- Supports: `VITE_` values are bundled into client source, so they must not contain sensitive values; local env files should be ignored by Git.
- Limits: The prefix rule is Vite-specific and is not a generic secret-detection rule.

<a id="p19"></a>
## P19 — Express behind proxies

- Edition: unversioned; read/attempted 2026-09-27; read.
- Source: https://expressjs.com/en/guide/behind-proxies.html
- Supports: Rate-limiting and logging should use a client IP derived from a proxy setup that exactly matches deployment; blindly setting `trust proxy` to true can allow client-supplied forwarded headers to control the value.
- Limits: The proper trust configuration depends on the actual proxy chain and must be tested in that deployment topology.

<a id="s01"></a>
## S01 — MITRE CWE Top 25

- Edition: 2025; current landing page lists this year; read/attempted 2026-09-27; read.
- Source: https://cwe.mitre.org/top25/
- Supports: Prioritization context for recurring software weakness classes.
- Limits: Population ranking is not an application-specific risk score.

<a id="s02"></a>
## S02 — NIST Secure Software Development Framework

- Edition: SP 800-218 / SSDF 1.1; final February 2022; read/attempted 2026-09-27; read.
- Source: https://csrc.nist.gov/pubs/sp/800/218/final
- Supports: Lifecycle practices, security requirements, release integrity and vulnerability response.
- Limits: A framework to tailor, not a certification or automatic checklist.

<a id="s03"></a>
## S03 — NIST SSDF revision

- Edition: SP 800-218 Rev. 1 / 1.2; initial public draft, December 17 2025; read/attempted 2026-09-27; read.
- Source: https://csrc.nist.gov/pubs/sp/800/218/r1/ipd
- Supports: Identifies the newer draft and prevents presenting it as the final baseline.
- Limits: Draft status explicit; normative recommendations use S02 until a final successor is verified.

<a id="s04"></a>
## S04 — NIST Digital Identity Guidelines: Authentication

- Edition: SP 800-63B-4; final July 2025; read/attempted 2026-09-27; read.
- Source: https://csrc.nist.gov/pubs/sp/800/63/b/4/final
- Supports: Confirms the current revision and its authentication scope.
- Limits: Government-system scope; do not claim every commercial app is legally bound by it.

<a id="s05"></a>
## S05 — NIST authenticator requirements

- Edition: 800-63B-4, section 3; read/attempted 2026-09-27; read.
- Source: https://pages.nist.gov/800-63-4/sp800-63b/authenticators/
- Supports: Password-only minimum is 15 characters; MFA passwords may use 8. Supports blocklists and avoiding composition rules and routine forced changes.
- Limits: Separate centrally checked passwords from device unlock secrets; changes to existing auth require approval.

<a id="s06"></a>
## S06 — CISA Secure by Design hub and joint guidance

- Edition: Current hub unavailable; October 2023 joint paper seen in primary-source index; read/attempted 2026-09-27; partial / access limited.
- Source: https://www.cisa.gov/securebydesign
- Supports: Source discovery only; an indexed primary extract describes manufacturer responsibility and secure defaults.
- Limits: Hub returned 403; PDF retrieval failed, and partner PDF exceeded tool size. Do not claim full paper review or newest CISA edition. Use S07/S02 for supported principles.

<a id="s07"></a>
## S07 — ASD Secure by Design foundations

- Edition: July 2024 document; HTML last updated July 30 2024; read/attempted 2026-09-27; read.
- Source: https://www.cyber.gov.au/business-government/secure-design/secure-by-design/secure-by-design-foundations
- Supports: Security defaults and lifecycle ownership as design responsibilities.
- Limits: Partner-government guidance, not a substitute for inaccessible CISA publication verification.

<a id="s08"></a>
## S08 — MDN Web Security

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://developer.mozilla.org/en-US/docs/Web/Security
- Supports: Browser-facing controls: HTTPS, safer content handling, cookie restrictions and cross-origin boundaries.
- Limits: Choose applicable controls; no operational environment or application has been audited.

<a id="s09"></a>
## S09 — Mozilla HTTP Observatory tests and scoring

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://developer.mozilla.org/en-US/observatory/docs/tests_and_scoring
- Supports: Browser-header checks and interpretation of their grades.
- Limits: Grade is a signal, not proof of authorization, tenant separation or complete security; no remote scan was run.

<a id="s10"></a>
## S10 — Security disclosure file format

- Edition: RFC 9116; read/attempted 2026-09-27; read.
- Source: https://www.rfc-editor.org/rfc/rfc9116.html
- Supports: A discoverable security contact with expiry, normally at /.well-known/security.txt over HTTPS.
- Limits: Use a user-approved real contact; a placeholder contact is not a completed disclosure channel.

<a id="s11"></a>
## S11 — MDN CSP Report-Only

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy-Report-Only
- Supports: Trial a policy while observing violations before enforcement.
- Limits: Report-Only does not block violations. External reporting destinations need separate data-sharing approval.

<a id="s12"></a>
## S12 — MDN Strict-Transport-Security

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security
- Supports: HSTS relies on an HTTPS response; subdomain scope and preload require care.
- Limits: An HTTP localhost header check cannot prove HTTPS enforcement; do not casually add preload or includeSubDomains.

<a id="s13"></a>
## S13 — MDN CORS

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
- Supports: Credentialed browser access needs explicit allowed origins; public noncredentialed resources can allow all origins.
- Limits: CORS controls browser response access, not caller authorization or all cross-site requests.

<a id="s14"></a>
## S14 — Electron security guidance

- Edition: Rolling latest documentation; no app-version claim; read/attempted 2026-09-27; read.
- Source: https://www.electronjs.org/docs/latest/tutorial/security
- Supports: Renderer isolation, sandboxing, remote-content and privileged-bridge boundaries.
- Limits: Only applicable to Electron; another desktop runtime needs its own official guidance.

<a id="s15"></a>
## S15 — MCP authorization specification

- Edition: 2026-07-28; latest specification redirected here; read/attempted 2026-09-27; read.
- Source: https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization
- Supports: Validate access-token audience and use constrained authorization scopes.
- Limits: Map controls to the detected transport and SDK version; reading docs does not authorize connector changes.

<a id="s16"></a>
## S16 — MCP security best practices

- Edition: Draft documentation; read/attempted 2026-09-27; read.
- Source: https://modelcontextprotocol.io/docs/draft/tutorials/security/security_best_practices
- Supports: Threat discovery: confused deputy, unsafe token forwarding, SSRF and local-server execution.
- Limits: Draft is supplementary; use S15 for stable normative authorization requirements.

<a id="s17"></a>
## S17 — Django deployment checklist

- Edition: Stable redirect resolved to Django 6.1; read/attempted 2026-09-27; read.
- Source: https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/
- Supports: Check production debug settings, hosts and environment-specific deployment configuration.
- Limits: Installed applications may use a different supported version; inspect their manifests first.

<a id="s18"></a>
## S18 — FastAPI behind a proxy

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://fastapi.tiangolo.com/advanced/behind-a-proxy/
- Supports: Forwarded headers should be accepted from known proxy addresses.
- Limits: Trusting all sources is only appropriate under an enforced proxy-only network boundary; inspect topology.

<a id="s19"></a>
## S19 — EU General Data Protection Regulation

- Edition: Regulation (EU) 2016/679; read/attempted 2026-09-27; read.
- Source: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
- Supports: When applicable, data minimization, retention, security and an appropriate processing basis need attention.
- Limits: No jurisdiction or lawful-basis determination made. Consent is not the only possible basis; legal decisions stay with the user and qualified advisers.

<a id="s20"></a>
## S20 — SLSA specification

- Edition: 1.2 / Approved; read/attempted 2026-09-27; read.
- Source: https://slsa.dev/spec/v1.2/
- Supports: Current supply-chain framework with build/source tracks and provenance.
- Limits: Supersedes P02 as this research baseline; provenance alone does not establish safe behavior or a SLSA level.

<a id="s21"></a>
## S21 — GitHub Actions secure use

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://docs.github.com/en/actions/reference/security/secure-use
- Supports: Least workflow privilege, handling untrusted event data safely, and full commit-SHA references for third-party actions.
- Limits: An immutable action can still be unsafe; inspect source and update deliberately. Replaces unavailable P04.

<a id="s22"></a>
## S22 — GitHub repository-security quickstart

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository
- Supports: Repository security-policy and security-feature setup pointers.
- Limits: Plan availability and dashboard state are not verified from local files; user performs remote setup.

<a id="s23"></a>
## S23 — npm publishing 2FA requirements

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://docs.npmjs.com/requiring-2fa-for-package-publishing-and-settings-modification/
- Supports: Maintainer authentication and package publishing protections.
- Limits: Account settings and publication remain user actions; recheck supported publishing paths before implementation.

<a id="s24"></a>
## S24 — MASVS release ledger

- Edition: 2.1.0 marked Latest; read/attempted 2026-09-27; read.
- Source: https://github.com/OWASP/masvs/releases
- Supports: Confirms stable mobile baseline including privacy controls.
- Limits: O05 is live documentation; pin a release for precise requirements. Do not reuse old MASVS level labels uncritically.

<a id="s25"></a>
## S25 — MASTG release ledger

- Edition: 2.0.0 marked Latest; first stable v2 framework; read/attempted 2026-09-27; read.
- Source: https://github.com/OWASP/mastg/releases
- Supports: Confirms modular mobile test guidance and stable edition.
- Limits: Use detected platform tools locally; missing device/emulator support must be reported.

<a id="s26"></a>
## S26 — ASVS usage and verification levels

- Edition: Pinned v5.0.0; read/attempted 2026-09-27; read.
- Source: https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x03-What-is-the-ASVS.md
- Supports: L1 starts with essential defenses; L2 includes L1 and broader requirements; L3 adds the most demanding controls. Tailoring depends on application context.
- Limits: A selected subset is ASVS-informed, not an ASVS certification. GitHub latest release alias also exposes bleeding-edge content; do not substitute it for v5.0.0.

<a id="s27"></a>
## S27 — Stripe idempotent requests

- Edition: Rolling API documentation; read/attempted 2026-09-27; read.
- Source: https://docs.stripe.com/api/idempotent_requests
- Supports: Use an operation-specific key to make supported API retries return the recorded outcome.
- Limits: API request idempotency is different from deduplicating incoming webhook events; payment edits require separate approval.

<a id="s28"></a>
## S28 — Supabase API key types

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://supabase.com/docs/guides/getting-started/api-keys
- Supports: Distinguishes publishable/anon keys from privileged secret/service-role keys that bypass RLS.
- Limits: Prefix presence is not proof of a leak. Assess privileges and RLS without displaying key values.

<a id="s29"></a>
## S29 — Firebase basic security rules

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://firebase.google.com/docs/rules/basics
- Supports: Tailor rules to authenticated users and the intended data access model rather than broad public access.
- Limits: Product-specific rules differ; privileged server SDK paths also need server-side authorization.

<a id="s30"></a>
## S30 — Next.js environment variables

- Edition: Rolling App Router guide; selector showed 16.3.6; read/attempted 2026-09-27; read.
- Source: https://nextjs.org/docs/app/guides/environment-variables
- Supports: Investigate NEXT_PUBLIC_ variables as browser-exposure candidates alongside build artifacts.
- Limits: Prefix is a signal, not proof a value is confidential; use version-specific instructions for the target app.

<a id="s31"></a>
## S31 — Amazon S3 Block Public Access

- Edition: Rolling service documentation; read/attempted 2026-09-27; read.
- Source: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html
- Supports: Inspect account/bucket public-access controls and deliberate public-object requirements.
- Limits: Local IaC is only desired state; dashboard and actual resource state remain unverified. No AWS calls made.

<a id="s32"></a>
## S32 — Vercel Deployment Protection

- Edition: Rolling product documentation; read/attempted 2026-09-27; read.
- Source: https://vercel.com/docs/deployment-protection
- Supports: Conditional review of preview/deployment access boundaries.
- Limits: Do not assume features are included in a plan or that platform protection replaces app authorization.

<a id="s33"></a>
## S33 — Cloudflare security guidance

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://developers.cloudflare.com/fundamentals/security/
- Supports: Conditional provider-security documentation entry point.
- Limits: No account, origin lock-down or plan-specific settings verified; select implementation pages only when Cloudflare is detected.

<a id="s34"></a>
## S34 — Auth0 production-deployment guidance

- Edition: Unconfirmed; read/attempted 2026-09-27; unavailable.
- Source: https://auth0.com/docs/deploy-monitor/deploy-applications/deploy-to-production
- Supports: Conditional identity-provider pointer only.
- Limits: Retrieval failed. No Auth0-specific checklist rule is derived; fetch current docs when provider is present.

<a id="r01"></a>
## R01 — PortSwigger access-control guidance

- Edition: Unversioned practitioner material; read/attempted 2026-09-27; read.
- Source: https://portswigger.net/web-security/access-control
- Supports: Use resource-level authorization tests, including role and cross-user boundaries.
- Limits: Practitioner evidence, corroborated by O03/O16/S26; no lab or attack was executed.

<a id="r02"></a>
## R02 — Trail of Bits Testing Handbook

- Edition: Rolling practitioner handbook; read/attempted 2026-09-27; read.
- Source: https://appsec.guide/
- Supports: Choose deterministic analysis suited to the language and risk.
- Limits: Tool discovery, not permission to install tools or run arbitrary rule downloads; corroborated by S02.

<a id="r03"></a>
## R03 — Troy Hunt: Passwords Evolved

- Edition: Historical practitioner article; read/attempted 2026-09-27; read.
- Source: https://www.troyhunt.com/passwords-evolved-authentication-guidance-for-the-modern-era/
- Supports: Helpful explanation of credential reuse and usable authentication.
- Limits: Do not inherit old numeric policy; use S04/S05/O09 for current requirements.

<a id="r04"></a>
## R04 — Tanya Janca: Resources

- Edition: Unversioned practitioner material; read/attempted 2026-09-27; read.
- Source: https://shehackspurple.ca/resources/
- Supports: Accessible teaching style for developers without a security background.
- Limits: No technical control imported from the landing page. Linked securecodingguideline.com could not be retrieved.

<a id="r05"></a>
## R05 — Jim Manico: Talks and workshops

- Edition: Page states last update May 13 2026; read/attempted 2026-09-27; read.
- Source: https://manicode.com/talks.html
- Supports: Coverage signal for secure coding, frontend boundaries, dependencies and AI/MCP.
- Limits: Talk descriptions are not standards or verified talk transcripts; checklist authority remains OWASP/NIST.

<a id="r06"></a>
## R06 — Latacora: Cryptographic right answers

- Edition: Historical 2018 practitioner article; read/attempted 2026-09-27; read.
- Source: https://www.latacora.com/blog/cryptographic-right-answers/
- Supports: Prefer established cryptographic constructions and proper password hashing.
- Limits: Use current O09/S05 guidance; do not carry over historical preference ordering or custom crypto recipes.

<a id="n01"></a>
## N01 — Turnstile server-side validation

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://developers.cloudflare.com/turnstile/get-started/server-side-validation/
- Supports: A challenge must be validated on the server before its protected action.
- Limits: Conditional example; no provider purchase or live call authorized.

<a id="n02"></a>
## N02 — Cloudflare DDoS Protection

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://developers.cloudflare.com/ddos-protection/
- Supports: An edge service can absorb some network/HTTP abuse before origin handling.
- Limits: Not a replacement for origin authorization, application budgets or verifying proxy topology.

<a id="n03"></a>
## N03 — OWASP Unvalidated Redirects and Forwards

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html
- Supports: Restrict user-controlled redirect destinations.
- Limits: Validate the actual framework URL parsing and intended redirect flow.

<a id="n04"></a>
## N04 — Sender Policy Framework

- Edition: RFC 7208; read/attempted 2026-09-27; read.
- Source: https://www.rfc-editor.org/rfc/rfc7208
- Supports: Domain policy identifies permitted sending systems.
- Limits: RFC 7208 is a referenced standard, not a claim that no updates exist; actual DNS is user-owned.

<a id="n05"></a>
## N05 — DKIM Signatures

- Edition: RFC 6376; read/attempted 2026-09-27; read.
- Source: https://www.rfc-editor.org/rfc/rfc6376
- Supports: Domain signatures support message authentication.
- Limits: Private signing keys are not inspected; provider-specific DNS and later amendments must be checked.

<a id="n06"></a>
## N06 — DMARC

- Edition: RFC 7489; read/attempted 2026-09-27; read.
- Source: https://www.rfc-editor.org/rfc/rfc7489
- Supports: Align domain authentication and publish receiver-handling/reporting policy.
- Limits: Foundational RFC; check current amendments/provider support before final DNS instructions. Monitoring is not enforcement.

<a id="n07"></a>
## N07 — Dependabot version updates

- Edition: Rolling documentation; read/attempted 2026-09-27; read.
- Source: https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates
- Supports: Schedule dependency update pull requests for configured ecosystems.
- Limits: Not automatic safe merging; remote enablement and privileged CI require user action.
