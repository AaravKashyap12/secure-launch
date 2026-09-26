# Control index

| ID | Control | Default priority | Canonical reference |
| --- | --- | --- | --- |
| B01 | Know what is exposed and what data is held | Process step, not a list item | [baseline.md](baseline.md) |
| B02 | Keep confidential values out of shipped files | Before launch | [baseline.md](baseline.md) |
| B03 | Keep builds repeatable and dependencies understood | First week | [baseline.md](baseline.md) |
| B04 | Choose a clear security contact | First week | [baseline.md](baseline.md) |
| B05 | Record what was checked and what remains | Process step, not a list item | [baseline.md](baseline.md) |
| W01 | Serve browser traffic securely | Before launch | [modules/web-platform.md](modules/web-platform.md) |
| W02 | Set baseline browser response headers | Before launch | [modules/web-platform.md](modules/web-platform.md) |
| W03 | Allow only intended cross-origin access | Before launch | [modules/web-platform.md](modules/web-platform.md) |
| W04 | Prevent cross-site state changes | Before launch | [modules/sessions.md](modules/sessions.md) |
| W05 | Show useful errors without debug internals | Before launch | [modules/web-platform.md](modules/web-platform.md) |
| A01 | Protect accounts and administrative actions | Before launch | [modules/auth.md](modules/auth.md) |
| A02 | Use appropriate password and recovery controls | Before launch | [modules/auth.md](modules/auth.md) |
| A03 | Keep sessions scoped and revocable | Before launch | [modules/sessions.md](modules/sessions.md) |
| A04 | Bound login and recovery attempts | Before launch | [modules/auth.md](modules/auth.md) |
| A05 | Keep tenant and user records separated | Before launch | [modules/multi-tenant.md](modules/multi-tenant.md) |
| A06 | Protect Supabase tables, views and privileged access | Before launch | [modules/multi-tenant.md](modules/multi-tenant.md) |
| A07 | Limit Firebase access to the intended users | Before launch | [modules/multi-tenant.md](modules/multi-tenant.md) |
| A08 | Use the identity provider safely | Before launch | [modules/auth.md](modules/auth.md) |
| I01 | Validate input and encode output | Before launch | [modules/web-platform.md](modules/web-platform.md) |
| I02 | Bound work, payloads and waiting time | Before launch | [modules/web-platform.md](modules/web-platform.md) |
| I03 | Trust forwarded addresses only through known proxies | Before launch | [modules/proxy-and-cdn.md](modules/proxy-and-cdn.md) |
| I04 | Accept uploads without granting execution | Before launch | [modules/uploads.md](modules/uploads.md) |
| I05 | Keep URL fetches inside their intended destinations | Before launch | [modules/agent-tools.md](modules/agent-tools.md) |
| I06 | Keep sensitive records out of logs | First week | [modules/privacy.md](modules/privacy.md) |
| I07 | Bound GraphQL and API resource access | As you grow | [modules/web-platform.md](modules/web-platform.md) |
| P01 | Verify incoming payment events | Before launch | [modules/payments.md](modules/payments.md) |
| P02 | Avoid processing the same payment twice | Before launch | [modules/payments.md](modules/payments.md) |
| P03 | Authenticate other incoming webhooks | Before launch | [modules/webhooks.md](modules/webhooks.md) |
| C01 | Make storage exposure deliberate | Before launch | [modules/cloud.md](modules/cloud.md) |
| C02 | Protect preview and management surfaces | Before launch | [modules/cloud.md](modules/cloud.md) |
| C03 | Give containers only needed privileges | Before launch | [modules/containers.md](modules/containers.md) |
| C04 | Keep Kubernetes identities and workloads scoped | As you grow | [modules/containers.md](modules/containers.md) |
| AI01 | Keep model credentials on the server | Before launch | [modules/ai-features.md](modules/ai-features.md) |
| AI02 | Put a ceiling on AI spending and loops | Before launch | [modules/ai-features.md](modules/ai-features.md) |
| AI03 | Treat retrieved text and generated output as data | Before launch | [modules/ai-features.md](modules/ai-features.md) |
| AI04 | Keep retrieval and tool access within each user scope | Before launch | [modules/ai-features.md](modules/ai-features.md) |
| G01 | Review skill commands and permission boundaries | Before launch | [modules/agent-tools.md](modules/agent-tools.md) |
| G02 | Validate MCP authorization and transport boundaries | As you grow | [modules/agent-tools.md](modules/agent-tools.md) |
| M01 | Protect mobile storage and platform entry points | Before launch | [modules/native-apps.md](modules/native-apps.md) |
| D01 | Separate desktop content from OS privileges | Before launch | [modules/native-apps.md](modules/native-apps.md) |
| SC01 | Pin and constrain CI execution | First week | [modules/supply-chain.md](modules/supply-chain.md) |
| SC02 | Keep private packages tied to their registry | First week | [modules/supply-chain.md](modules/supply-chain.md) |
| SC03 | Protect package publishing identities | First week | [modules/supply-chain.md](modules/supply-chain.md) |
| SC04 | Trace released artifacts to their source | As you grow | [modules/supply-chain.md](modules/supply-chain.md) |
| PR01 | Collect and retain only needed personal data | Before launch | [modules/privacy.md](modules/privacy.md) |
| OP01 | Plan recovery and watch for failed protections | First week | [modules/operations.md](modules/operations.md) |
| OP02 | Revisit sources and deeper assurance as the app grows | As you grow | [modules/operations.md](modules/operations.md) |
| W06 | Roll out a Content Security Policy | First week | [modules/web-platform.md](modules/web-platform.md) |
| A09 | Limit public and write-endpoint abuse | Before launch | [modules/auth.md](modules/auth.md) |
| A10 | Make automated sign-up and form abuse harder | Before launch | [modules/auth.md](modules/auth.md) |
| C05 | Put an appropriate edge proxy in front of public services | Before launch | [modules/proxy-and-cdn.md](modules/proxy-and-cdn.md) |
| I08 | Keep redirects on approved destinations | Before launch | [modules/auth.md](modules/auth.md) |
| C06 | Authenticate the domain used to send email | Before launch | [modules/cloud.md](modules/cloud.md) |
| B06 | Separate development from production data and credentials | Before launch | [baseline.md](baseline.md) |
| SC05 | Keep dependency updates arriving automatically | First week | [modules/supply-chain.md](modules/supply-chain.md) |
