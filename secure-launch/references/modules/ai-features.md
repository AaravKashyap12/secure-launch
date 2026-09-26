# Ai Features

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## AI01 — Keep model credentials on the server

- **Why:** A browser bundle cannot keep a model-provider secret confidential.
- **Applies:** Hosted model calls.
- **Default priority:** Before launch.
- **Who / approval:** Agent code after plan; user rotates.
- **Implementation:** Remove privileged model keys from client build paths; protect the server endpoint.
- **Local verification:** Fresh client build contains no synthetic secret marker; no paid model call.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O04](../sources.md#o04), [S30](../sources.md#s30), [P18](../sources.md#p18), [O14](../sources.md#o14).

## AI02 — Put a ceiling on AI spending and loops

- **Why:** A request or agent loop should not create an unbounded bill.
- **Applies:** AI or other costly endpoints.
- **Default priority:** Before launch.
- **Who / approval:** Agent after plan.
- **Implementation:** Use authenticated-user limits plus request/token/tool-loop caps and proxy-aware network budgets.
- **Local verification:** Mock model; user limit reaches 429 without provider spend or cross-user blocking.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O04](../sources.md#o04), [O03](../sources.md#o03), [P19](../sources.md#p19).

## AI03 — Treat retrieved text and generated output as data

- **Why:** Retrieved text and model output are not permission to execute actions.
- **Applies:** LLM input/output, RAG or agent tools.
- **Default priority:** Before launch.
- **Who / approval:** Agent after plan; permission expansion never implicit.
- **Implementation:** Separate instruction authority from content; validate output and tool arguments outside the prompt.
- **Local verification:** Local adversarial document cannot cause unauthorized tool effects; log only safe evidence.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O04](../sources.md#o04), [O10](../sources.md#o10), [S16](../sources.md#s16).

## AI04 — Keep retrieval and tool access within each user scope

- **Why:** Tools and retrieval need the same user boundaries as the underlying data.
- **Applies:** RAG, connectors or agent execution.
- **Default priority:** Before launch.
- **Who / approval:** Ask per access/policy item.
- **Implementation:** Enforce tenant filters and scoped credentials at retrieval/tool boundaries.
- **Local verification:** Two fake identities cannot retrieve each other’s records or invoke disallowed tools.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O04](../sources.md#o04), [O03](../sources.md#o03), [S15](../sources.md#s15).
