# Web Platform

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## W01 — Serve browser traffic securely

- **Why:** Encrypted transport protects data on its way to the service.
- **Applies:** HTTP surface; relevant client backend.
- **Default priority:** Before launch.
- **Who / approval:** Agent config; user hosting.
- **Implementation:** Review HTTPS termination and scoped HSTS, then provider handoff.
- **Local verification:** Local TLS/config check only; HTTP localhost cannot prove deployed HSTS.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S08](../sources.md#s08), [S12](../sources.md#s12), [O22](../sources.md#o22).

## W02 — Set baseline browser response headers

- **Why:** Browser defaults can be tightened without redesigning the app.
- **Applies:** HTTP responses.
- **Default priority:** Before launch.
- **Who / approval:** Agent after plan; ask for enforcement.
- **Implementation:** Choose content-type, framing and referrer controls that fit the app. CSP rollout is W06, not a required day-one enforcement project.
- **Local verification:** Inspect local responses and browser console; label Report-Only as monitoring.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O22](../sources.md#o22), [S09](../sources.md#s09), [S11](../sources.md#s11).

## W03 — Allow only intended cross-origin access

- **Why:** Only intended browser origins should read private responses.
- **Applies:** Cross-origin browser clients.
- **Default priority:** Before launch.
- **Who / approval:** Agent after plan.
- **Implementation:** Separate private credentialed APIs from intentionally public resources.
- **Local verification:** Allowed and denied origin preflights; normal same-origin flow still works.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S13](../sources.md#s13), [O16](../sources.md#o16).

## W05 — Show useful errors without debug internals

- **Why:** Debug output may reveal implementation and user data.
- **Applies:** Server functions or production build.
- **Default priority:** Before launch.
- **Who / approval:** Agent after plan.
- **Implementation:** Disable production debug; define safe failure responses.
- **Local verification:** Local production-mode error exposes no stack/credential data.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O18](../sources.md#o18), [O19](../sources.md#o19), [S17](../sources.md#s17).

## W06 — Roll out a Content Security Policy

- **Why:** A measured rollout can restrict unwanted scripts without breaking real workflows.
- **Applies:** Browser content with scripts/resources.
- **Default priority:** First week.
- **Who / approval:** Agent proposes Report-Only; ask separately before enforcement.
- **Implementation:** Inventory required resource origins; retain existing enforcement and introduce Report-Only only for a new policy. Keep reports local unless data sharing is approved.
- **Local verification:** A local synthetic violation is observed; expected pages work. Report-Only is never counted as blocked execution.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S11](../sources.md#s11), [O22](../sources.md#o22).

## I01 — Validate input and encode output

- **Why:** Untrusted values should not become commands, queries or executable markup.
- **Applies:** Untrusted input or rendered content.
- **Default priority:** Before launch.
- **Who / approval:** Agent after plan; ask if public contract changes.
- **Implementation:** Use existing schemas, parameterized storage and context-appropriate encoding.
- **Local verification:** Malformed input denied; stored/displayed untrusted data stays inert.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O10](../sources.md#o10), [O16](../sources.md#o16), [S01](../sources.md#s01).

## I02 — Bound work, payloads and waiting time

- **Why:** Small bounded requests should not trigger unlimited work.
- **Applies:** Network or expensive operations.
- **Default priority:** Before launch.
- **Who / approval:** Agent after plan.
- **Implementation:** Limit body/file size, request duration and concurrency based on actual workloads.
- **Local verification:** Small bounded local probes verify rejection and timeout without load testing.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O03](../sources.md#o03), [O18](../sources.md#o18), [O17](../sources.md#o17).

## I07 — Bound GraphQL and API resource access

- **Why:** A valid query can still request excessive or unauthorized data.
- **Applies:** GraphQL or rich API queries.
- **Default priority:** As you grow.
- **Who / approval:** Agent after plan; contract changes ask-first.
- **Implementation:** Review depth/complexity/pagination and field-level authorization as applicable.
- **Local verification:** Oversized synthetic query denied; authorized bounded query succeeds.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O17](../sources.md#o17), [O03](../sources.md#o03).
- **Escalate earlier only when exposed:** identify the reachable path and day-one consequence; merely finding a manifest is not enough.
