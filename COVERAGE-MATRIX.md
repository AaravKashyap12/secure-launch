# Approved coverage — 2026-09-27

Supersedes the Phase 1 priority defaults. [Priority policy](secure-launch/references/priorities.md). All items are conditional, not findings about an application. Detailed why/applicability/implementation/proof/owner/source fields live in their canonical references.

| ID | Item | Profiles | Default priority | Reference |
| --- | --- | --- | --- | --- |
| B01 | Know what is exposed and what data is held | W, A, L, G, M, S, D, I | Process step, not a list item | [baseline.md](secure-launch/references/baseline.md) |
| B02 | Keep confidential values out of shipped files | W, A, L, G, M, S, D, I | Before launch | [baseline.md](secure-launch/references/baseline.md) |
| B03 | Keep builds repeatable and dependencies understood | W, A, L, G, M, S, D, I | First week | [baseline.md](secure-launch/references/baseline.md) |
| B04 | Choose a clear security contact | W, A, L, G, M, S, D, I | First week | [baseline.md](secure-launch/references/baseline.md) |
| B05 | Record what was checked and what remains | W, A, L, G, M, S, D, I | Process step, not a list item | [baseline.md](secure-launch/references/baseline.md) |
| W01 | Serve browser traffic securely | W, A, G, S, I | Before launch | [modules/web-platform.md](secure-launch/references/modules/web-platform.md) |
| W02 | Set baseline browser response headers | W, A, G, S, I | Before launch | [modules/web-platform.md](secure-launch/references/modules/web-platform.md) |
| W03 | Allow only intended cross-origin access | W, A, G, S, I | Before launch | [modules/web-platform.md](secure-launch/references/modules/web-platform.md) |
| W04 | Prevent cross-site state changes | W, I | Before launch | [modules/sessions.md](secure-launch/references/modules/sessions.md) |
| W05 | Show useful errors without debug internals | W, A, G, S, I | Before launch | [modules/web-platform.md](secure-launch/references/modules/web-platform.md) |
| A01 | Protect accounts and administrative actions | W, A, G, I | Before launch | [modules/auth.md](secure-launch/references/modules/auth.md) |
| A02 | Use appropriate password and recovery controls | W, A, I | Before launch | [modules/auth.md](secure-launch/references/modules/auth.md) |
| A03 | Keep sessions scoped and revocable | W, I | Before launch | [modules/sessions.md](secure-launch/references/modules/sessions.md) |
| A04 | Bound login and recovery attempts | W, A, G, I | Before launch | [modules/auth.md](secure-launch/references/modules/auth.md) |
| A05 | Keep tenant and user records separated | W, A, G, I | Before launch | [modules/multi-tenant.md](secure-launch/references/modules/multi-tenant.md) |
| A06 | Protect Supabase tables, views and privileged access | W, A, I | Before launch | [modules/multi-tenant.md](secure-launch/references/modules/multi-tenant.md) |
| A07 | Limit Firebase access to the intended users | W, A, M, I | Before launch | [modules/multi-tenant.md](secure-launch/references/modules/multi-tenant.md) |
| A08 | Use the identity provider safely | W, A, M, D, I | Before launch | [modules/auth.md](secure-launch/references/modules/auth.md) |
| I01 | Validate input and encode output | W, A, L, G, M, S, D, I | Before launch | [modules/web-platform.md](secure-launch/references/modules/web-platform.md) |
| I02 | Bound work, payloads and waiting time | W, A, G, I | Before launch | [modules/web-platform.md](secure-launch/references/modules/web-platform.md) |
| I03 | Trust forwarded addresses only through known proxies | W, A, G, I | Before launch | [modules/proxy-and-cdn.md](secure-launch/references/modules/proxy-and-cdn.md) |
| I04 | Accept uploads without granting execution | W, A, G, I | Before launch | [modules/uploads.md](secure-launch/references/modules/uploads.md) |
| I05 | Keep URL fetches inside their intended destinations | W, A, G, I | Before launch | [modules/agent-tools.md](secure-launch/references/modules/agent-tools.md) |
| I06 | Keep sensitive records out of logs | W, A, L, G, M, S, D, I | First week | [modules/privacy.md](secure-launch/references/modules/privacy.md) |
| I07 | Bound GraphQL and API resource access | W, A, G, I | As you grow | [modules/web-platform.md](secure-launch/references/modules/web-platform.md) |
| P01 | Verify incoming payment events | W, A, I | Before launch | [modules/payments.md](secure-launch/references/modules/payments.md) |
| P02 | Avoid processing the same payment twice | W, A, I | Before launch | [modules/payments.md](secure-launch/references/modules/payments.md) |
| P03 | Authenticate other incoming webhooks | W, A, G, I | Before launch | [modules/webhooks.md](secure-launch/references/modules/webhooks.md) |
| C01 | Make storage exposure deliberate | W, A, G, M, S, D, I | Before launch | [modules/cloud.md](secure-launch/references/modules/cloud.md) |
| C02 | Protect preview and management surfaces | W, A, G, S, I | Before launch | [modules/cloud.md](secure-launch/references/modules/cloud.md) |
| C03 | Give containers only needed privileges | W, A, G, L, I | Before launch | [modules/containers.md](secure-launch/references/modules/containers.md) |
| C04 | Keep Kubernetes identities and workloads scoped | W, A, G, I | As you grow | [modules/containers.md](secure-launch/references/modules/containers.md) |
| AI01 | Keep model credentials on the server | W, A, G, M, D, I | Before launch | [modules/ai-features.md](secure-launch/references/modules/ai-features.md) |
| AI02 | Put a ceiling on AI spending and loops | W, A, G, I | Before launch | [modules/ai-features.md](secure-launch/references/modules/ai-features.md) |
| AI03 | Treat retrieved text and generated output as data | W, A, G, M, D, I | Before launch | [modules/ai-features.md](secure-launch/references/modules/ai-features.md) |
| AI04 | Keep retrieval and tool access within each user scope | W, A, G, I | Before launch | [modules/ai-features.md](secure-launch/references/modules/ai-features.md) |
| G01 | Review skill commands and permission boundaries | G | Before launch | [modules/agent-tools.md](secure-launch/references/modules/agent-tools.md) |
| G02 | Validate MCP authorization and transport boundaries | G | As you grow | [modules/agent-tools.md](secure-launch/references/modules/agent-tools.md) |
| M01 | Protect mobile storage and platform entry points | M | Before launch | [modules/native-apps.md](secure-launch/references/modules/native-apps.md) |
| D01 | Separate desktop content from OS privileges | D | Before launch | [modules/native-apps.md](secure-launch/references/modules/native-apps.md) |
| SC01 | Pin and constrain CI execution | W, A, L, G, M, S, D, I | First week | [modules/supply-chain.md](secure-launch/references/modules/supply-chain.md) |
| SC02 | Keep private packages tied to their registry | W, A, L, G, M, S, D, I | First week | [modules/supply-chain.md](secure-launch/references/modules/supply-chain.md) |
| SC03 | Protect package publishing identities | L, G | First week | [modules/supply-chain.md](secure-launch/references/modules/supply-chain.md) |
| SC04 | Trace released artifacts to their source | L, G, M, D | As you grow | [modules/supply-chain.md](secure-launch/references/modules/supply-chain.md) |
| PR01 | Collect and retain only needed personal data | W, A, G, M, S, D, I | Before launch | [modules/privacy.md](secure-launch/references/modules/privacy.md) |
| OP01 | Plan recovery and watch for failed protections | W, A, G, M, D, I | First week | [modules/operations.md](secure-launch/references/modules/operations.md) |
| OP02 | Revisit sources and deeper assurance as the app grows | W, A, L, G, M, S, D, I | As you grow | [modules/operations.md](secure-launch/references/modules/operations.md) |
| W06 | Roll out a Content Security Policy | W, G, S, I | First week | [modules/web-platform.md](secure-launch/references/modules/web-platform.md) |
| A09 | Limit public and write-endpoint abuse | W, A, G, I | Before launch | [modules/auth.md](secure-launch/references/modules/auth.md) |
| A10 | Make automated sign-up and form abuse harder | W, I | Before launch | [modules/auth.md](secure-launch/references/modules/auth.md) |
| C05 | Put an appropriate edge proxy in front of public services | W, A, G, S, I | Before launch | [modules/proxy-and-cdn.md](secure-launch/references/modules/proxy-and-cdn.md) |
| I08 | Keep redirects on approved destinations | W, A, I | Before launch | [modules/auth.md](secure-launch/references/modules/auth.md) |
| C06 | Authenticate the domain used to send email | W, A, I | Before launch | [modules/cloud.md](secure-launch/references/modules/cloud.md) |
| B06 | Separate development from production data and credentials | W, A, L, G, M, S, D, I | Before launch | [baseline.md](secure-launch/references/baseline.md) |
| SC05 | Keep dependency updates arriving automatically | W, A, L, G, M, S, D, I | First week | [modules/supply-chain.md](secure-launch/references/modules/supply-chain.md) |

Profiles: W web SaaS, A public API, L library/CLI, G skill/MCP, M mobile, S static site, D desktop, I internal tool. Source IDs are preserved in every linked control. First-week/growth defaults are promoted only for specific demonstrated day-one exposure.
