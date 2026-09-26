# Agent Tools

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## G01 — Review skill commands and permission boundaries

- **Why:** Instructions and helper commands should not silently expand their host permissions.
- **Applies:** Agent instructions, scripts and referenced resources.
- **Default priority:** Before launch.
- **Who / approval:** Agent reviews; user approves external actions.
- **Implementation:** Inventory executable paths, network calls, file scope and untrusted instruction entry points.
- **Local verification:** Static trace plus later isolated fixture; fetched text cannot authorize commands.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O04](../sources.md#o04), [S16](../sources.md#s16), [S21](../sources.md#s21).

## G02 — Validate MCP authorization and transport boundaries

- **Why:** A token intended for one service should not authorize another.
- **Applies:** MCP server/client.
- **Default priority:** As you grow.
- **Who / approval:** Ask per auth/access item.
- **Implementation:** Match transport/version; validate token audience, consent and minimal permissions.
- **Local verification:** Local invalid-audience and unauthorized-tool fixtures fail without external OAuth calls.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S15](../sources.md#s15), [S16](../sources.md#s16), [O03](../sources.md#o03).
- **Escalate earlier only when exposed:** identify the reachable path and day-one consequence; merely finding a manifest is not enough.

## I05 — Keep URL fetches inside their intended destinations

- **Why:** A public URL field must not become access to private network services.
- **Applies:** URL import, previews, callbacks or discovery.
- **Default priority:** Before launch.
- **Who / approval:** Agent after plan; ask for infra changes.
- **Implementation:** Restrict scheme/host/address and redirects; account for DNS re-resolution.
- **Local verification:** Mock resolver/HTTP client rejects private/metadata destinations; no real target probing.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O12](../sources.md#o12), [S16](../sources.md#s16).
