# Persistence and authority

Load this reference before proposing or applying any write.

## Update versus create

Update an existing registration only when the persistent aspect, scope, temporal phase, and documentary role match. Otherwise propose a new registration and link it when useful.

Respect the role of Historical artifacts. A consolidated milestone summary remains a historical photograph and is not a running register of later evolution. Modify it only for a demonstrated historical correction or a link explicitly allowed by the current method.

Never create a new issue merely because there is no other place for an operational conflict or fallback. Propose an issue only when the required result and completion criterion are already sufficiently defined.

When a verified result completes or materially advances existing work, update the pertinent Linear checkpoint or closure with the result, verification, artifacts, residual out-of-scope work, dependency changes, and work unlocked. Do not duplicate those operational facts in Notion or a repository document whose role does not require them.

## Authority and material decisions

Ordinary technical details that apply consolidated decisions can become verified task results. A material product, method, or architecture decision becomes eligible for Canonical consolidation only after explicit user approval, unless the user explicitly delegated that specific decision to Codex.

When an approved decision is not yet consolidated and the repository is available, propose the pertinent repository document as its destination. Update Linear only for a distinct operational consequence; do not create a checkpoint automatically merely because consolidation is pending during the preview.

If a preview asks one confirmation to authorize both writing and substantive approval, include exactly this section:

`Decisioni materiali che questa conferma approverà`

List each decision as `M1`, `M2`, ... with precise consequence and target Canonical artifact. Without this section, a general “apply” confirmation authorizes registration only, not substantive approval.

## Write preview

The preview must make all actual writes quickly reviewable. For each `W` action include:

- source and exact target;
- create or update;
- semantic delta, not merely a prose summary;
- reason and candidate/aspect served;
- dependency on another write or `M` approval;
- applicable fallback and reconciliation obligation.

Keep no-write and already-correct aspects grouped. Show ready-to-copy responses appropriate to the preview, for example:

- `$fold-sync applica tutto`;
- `$fold-sync applica W1 W2`;
- `$fold-sync applica W1 W3 e approvo M1`;
- `$fold-sync rivedi: ...`;
- `$fold-sync annulla`.

## Preview state and follow-up commands

Recover the most recent pending preview from the current conversation and verify its identifier, actions, decision approvals, and status rather than reconstructing them by supposition.

- `applica tutto`: authorize every write that does not require an unapproved material decision.
- `applica W...`: authorize only the listed writes and prerequisites explicitly included.
- `... e approvo M...`: substantively approve only the listed material decisions that the preview exposed.
- `rivedi: ...`: mark the old preview `invalidated`, reevaluate the requested aspects, and issue a new preview with a new identifier.
- `annulla`: mark the referenced pending preview `cancelled`; write nothing.

If multiple valid pending previews are genuinely recoverable, return `ambiguous_preview` and request an identifier. Never choose by guesswork.

## Safe application

Before each authorized write:

1. verify that the required write and reread operations are available;
2. reread the exact target;
3. compare it with the state used for the preview;
4. apply only the approved semantic delta;
5. reread and verify the target immediately.

If relevant concurrent content changed, invalidate that write decision and reevaluate. Proceed without another confirmation only when approved effect, target identity, and delta safety are unchanged and no new content is overwritten or invalidated.

Order dependent work as primary write, verification, then secondary links. Do not apply a dependent operation when its prerequisite failed. Do not automatically delete a successful write after a later failure; reread actual state and persist the residual obligation.

## Fallbacks

Every fallback is temporary and must preserve final destination, content still to transfer or consolidate, and the condition for resuming. Later runs must recognize it as pending reconciliation.

### Notion unavailable

When a significant insight cannot be written to Notion, use the pertinent existing Linear registration for a clearly marked `Intuizione da trasferire in Notion` reference. Preserve origin, distilled suggestion, importance, intended Notion destination, and resume condition. Do not create an issue only for this fallback. The marker does not become an issue, decision, or Canonical knowledge.

### Repository unavailable or not writable

When an approved decision or required guiding knowledge cannot be consolidated, use the pertinent existing Linear registration for `Consolidamento nel repository in sospeso`. Preserve the intended repository target, approved content, and resume condition. The knowledge is not Canonical until repository consolidation is verified; readiness may remain blocked.

### Linear unavailable

Do not place operational state in Notion. Continue only independent repository or Notion actions. If the missing operational persistence cannot be made recoverable outside the chat, the run is incomplete.

### Source fails after preview

Use a fallback only when it was included in the preview and authorized. Otherwise stop the affected action and report it as incomplete or require a new preview.

## Divergence

Classify differences as apparent, temporal evolution, obsolete material, or unresolved conflict. Follow explicit `Supersedes` and `Superseded by` links. Never silently select a meaning when an unresolved conflict affects the candidate.

Record an operationally consequential conflict only in the pertinent Linear issue, milestone, or other existing operational registration. If none exists, a new issue is merely proposed and only when its result and completion criterion are defined.
