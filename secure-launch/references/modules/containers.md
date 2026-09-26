# Containers

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## C03 — Give containers only needed privileges

- **Why:** A container compromise should have as little reach as possible.
- **Applies:** Container runtime/build detected.
- **Default priority:** Before launch.
- **Who / approval:** Ask per infrastructure item.
- **Implementation:** Review user, capabilities, mounts, secret handling and image provenance.
- **Local verification:** Static config checks and approved local container checks; no production access.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O20](../sources.md#o20), [P03](../sources.md#p03).

## C04 — Keep Kubernetes identities and workloads scoped

- **Why:** Cluster-wide permissions can turn a small workload issue into a larger one.
- **Applies:** Kubernetes manifests detected.
- **Default priority:** As you grow.
- **Who / approval:** Ask per IaC item; user applies.
- **Implementation:** Review RBAC, pod privilege, network boundaries and secret references.
- **Local verification:** Offline manifest checks; no cluster remediation or live scanning.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O21](../sources.md#o21).
- **Escalate earlier only when exposed:** identify the reachable path and day-one consequence; merely finding a manifest is not enough.
