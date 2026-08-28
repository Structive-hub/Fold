# Verification and reporting

Use this reference after acquisition analysis, for write previews, during Apply verification, and for detailed final reports. Do not load it for the self-contained Cancel route defined in `SKILL.md`.

## Verification sequence

After authorized actions:

1. reread every changed target and compare the persisted meaning with the approved delta;
2. verify that links and dependent updates point to the intended registrations;
3. rescan the same frozen acquisition window and assign a disposition to every significant aspect;
4. check only pertinent sources for semantic duplicates or equivalent records;
5. perform a non-mutative idempotence check: on the current state, the same frozen window should require no further semantic write except declared reconciliation work.

A successful tool response is not proof of persistence without rereading the target. Do not execute the writes a second time merely to test idempotence.

## Aspect and run statuses

Use one aspect status:

- `applied_and_verified`;
- `already_represented`;
- `no_persistence_required`;
- `suspended_recoverable`;
- `partially_applied_recoverable`;
- `not_completed`.

Use one overall run status:

- `completed`: all significant aspects have terminal verified dispositions and no reconciliation remains;
- `completed_with_reconciliation`: every residual operation is recoverable outside the conversation under a defined fallback;
- `incomplete`: at least one significant aspect or residual operation exists only in the conversation or lacks a safe disposition.

`partially_applied_recoverable` is allowed only when the missing operations are reconstructible from persistent state outside the chat.

## Initial no-write report

When no write is necessary, return:

- `Perimetro`: requested `N`, selected-window boundaries, interpretation context used, observability limits;
- `Fonti consultate`: only sources actually read;
- `Riconosciuto`: significant aspects and their classifications;
- `Nessuna modifica`: grouped already-represented and no-persistence dispositions;
- `Stato`: overall run status and non-mutative idempotence result.

## Write preview

Return:

- `Anteprima <preview_id>` and state `pending_valid`;
- concise acquisition perimeter and sources consulted;
- `Scritture proposte`, with complete `W` action details;
- `Decisioni materiali che questa conferma approverà`, only when applicable, with `M` identifiers;
- grouped `Nessuna modifica` items;
- `Fallback o riconciliazioni`, only when applicable;
- ready-to-copy `$fold-sync` response forms valid for this preview.

Do not describe a write as applied in a preview.

## Final report after a command

Return:

- resolved preview identifier and terminal/current state;
- `Modificato e verificato`: applied `W` actions with reread evidence;
- `Lasciato invariato`: skipped, already-correct, or no-persistence aspects;
- `Decisioni materiali`: approvals actually granted, not merely recorded;
- `Fallback e riconciliazioni`: persistent location, final destination, remaining work, resume condition;
- `In sospeso o incompleto`: anything not safely recoverable;
- `Verifica finale`: frozen-window coverage, relevant duplicate check, and non-mutative idempotence;
- overall run status.

For `cancelled`, confirm no writes and mark the preview terminal. For `invalidated`, identify the replacement preview. For `ambiguous_preview`, make no writes and list the minimum identifiers needed to resolve it.

## Honesty about evidence

Distinguish direct observation from inference. Mention unavailable message identifiers, timestamps, inaccessible history, unavailable sources, and unverified external effects. Do not claim that older context was technically inaccessible merely because it was not needed or reported.
