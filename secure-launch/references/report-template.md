# Plan and completion format

Use ordinary words and explain a necessary technical term in one short line. Prefer “Add a request limit so this endpoint cannot run up a bill” over alarmist labels.

## Plan

Project: <evidence-backed profiles, stack, users/data, hosting, unknowns>.

Group applicable items into Before launch / First week / As you grow. Typical SaaS target: 12–15 actionable launch groups, fewer when features are absent. Do not hide urgent items to fit the target.

| ID(s) / item / why | Action status | Evidence + file | Proposed files / local command + cwd | Approval / owner | Sources |
| --- | --- | --- | --- | --- | --- |
| <specific control> | <Already in place / I'll add this / You'll need to / Not needed because> | <OBSERVED / FAILED / NOT RUN / UNAVAILABLE; truthful evidence> | <concrete scope> | <plan / separate item / user action> | <IDs> |

Ask approval for the concrete plan. List reserved items individually; generic plan approval cannot authorize their execution. If the user declines, leave them pending with a practical next step.

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
