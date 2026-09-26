# Plan and completion format

Use ordinary words and explain a necessary technical term in one short line. Prefer “Add a request limit so this endpoint cannot run up a bill” over alarmist labels.

## Plan — short chat view

Start with three lines:
1. <Project profiles, stack and scope supported by repository evidence.>
2. <Observed launch gaps and the bounded local changes proposed.>
3. <Key unknown or verification limitation; no certification claim.>

Then one line per applicable **Before launch** group: <plain-language action — action status — owner/approval>. Target 12–15 actionable groups for a typical SaaS, fewer when features are absent; never hide an urgent item to fit the target.

**First week:** <count> groups. **As you grow:** <count> groups. Details follow in the appendix; do not repeat each item in chat.

B01 and B05 are **Process step, not a list item**. Perform inventory and evidence recording, but never list either as a checklist item or include them in priority counts, including in the appendix.

For credential-shaped values in template/example files, include the proposed placeholder replacement after plan approval and a **You'll need to** line: rotate the value if it was ever real. Report locations only, never values.

Ask approval for the concrete plan. List reserved items individually; generic plan approval cannot authorize their execution. If declined, leave them pending with a practical next step.

## Plan appendix — evidence and execution detail

Group applicable actionable controls by Before launch / First week / As you grow. Keep full per-item fields here below the short chat view (or in a linked local PLAN.md appendix).

| ID(s) / item / why / applicability / priority | Action status | Evidence + file | Proposed files / local command + cwd | Approval / owner | Sources |
| --- | --- | --- | --- | --- | --- |
| <specific actionable control> | <Already in place / I'll add this / You'll need to / Not needed because> | <OBSERVED / FAILED / NOT RUN / UNAVAILABLE; truthful evidence> | <concrete scope> | <plan / separate item / user action> | <IDs> |

## Completion

Three lines:
1. <What this pass covered and the observed outcome.>
2. <The most important remaining Before-launch action, or none observed within this scope.>
3. <Verification limitation; no claim of certification or complete safety.>

Then concise sections:
- Added or changed: files and purpose.
- Checks: command, cwd, exit result, evidence; skipped checks with reason.
- You'll need to: numbered provider/DNS/credential/legal steps; no secret values.
- Deferred: priority, rationale and owner. A known day-one exposure stays visible.
- Re-run: “Use secure-launch on this repo after I complete the listed actions. Recheck changed areas and treat old results as historical.”

Do not convert NOT RUN to “Already in place”. A scan finding is not proof that a credential is real, a private key is valid or an attack succeeded. State what the evidence actually establishes.
