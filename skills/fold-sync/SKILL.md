---
name: fold-sync
description: Preserve significant outcomes from an explicitly selected Fold conversation window across the repository, Linear, and Notion. Use only when the user explicitly invokes $fold-sync with a positive message count or a follow-up command for a pending preview.
---

# Fold sync

Prevent significant Fold work from remaining only in the conversation. Do not summarize the conversation indiscriminately and do not activate implicitly.

## Invocation

Accept only these explicit forms:

- `$fold-sync N`, where `N` is a positive integer;
- `$fold-sync applica tutto`;
- `$fold-sync applica W1 W2`;
- `$fold-sync applica W1 W3 e approvo M1`;
- `$fold-sync rivedi: ...`;
- `$fold-sync annulla`.

Follow-up commands refer to the latest valid pending preview in the current conversation. Ask for a preview identifier only when more than one recoverable preview makes the reference genuinely ambiguous.

## Initial command dispatch

Before loading any reference, repository document, or external source, classify the invocation from its arguments alone and follow exactly one route:

- **Acquire — positive integer `N`:** validate the requested window, then load governance and run acquisition, classification, progressive consultation, and preview generation.
- **Cancel — `annulla`:** inspect only the current conversation for the pertinent pending preview. If exactly one is recoverable, mark it `cancelled`, confirm that no writes occurred, and stop. If none is recoverable, return `no_pending_preview`; if more than one is genuinely valid, return `ambiguous_preview` and request the minimum identifier needed. Do not load references, repository files, Linear, Notion, or other project sources for this route.
- **Revise — `rivedi: ...`:** recover the pertinent preview from the current conversation, mark it `invalidated`, and load only the preview-cycle instructions and candidate-specific sources required to produce the replacement. Do not rerun acquisition or classification unless the requested revision changes them.
- **Apply — `applica ...`:** recover the approved preview from the current conversation and skip acquisition and classification. Load governance, authority, destination, concurrency, and verification instructions progressively for the authorized actions only.

For an unrecognized form, stop without loading project sources or writing anything. The principle is: dispatch first, then load only what that command needs.

For the Acquire route, if `N` is missing, invalid, zero, negative, or greater than the visible user-message history, stop without writes or project-source loading. Never reduce it silently. The invocation itself is not part of the selected window.

## Governance loading for acquisition and writes

After validating the Acquire route, or before any write in the Apply route, locate the Fold repository and read, in this order:

1. `AGENTS.md`;
2. `docs/README.md`;
3. `docs/metodo-di-lavoro.md`.

Also follow any additional repository reading order required by `AGENTS.md`, including `README.md` and directly pertinent Canonical documents. These files govern the run; they are not automatically audit targets or candidates.

If any of the three mandatory governance files is unavailable, preliminary analysis may continue but no write is allowed. Report the missing authority explicitly.

## Run model

For the Acquire route:

1. Freeze the acquisition window and record its boundaries in the report.
2. Use earlier content only as minimum interpretation context for a reference in the first selected user message. It cannot create an autonomous candidate.
3. Identify significant elements, then split each into distinct persistent aspects when their meanings differ.
4. Classify each aspect by nature before deciding its disposition.
5. Consult only the sources pertinent to each aspect, progressively and in read-only mode.
6. Recognize an equivalent existing registration before proposing a new one.
7. Produce either a final no-write report or a mandatory write preview, then stop and wait for an explicit follow-up command.

Load [acquisition-and-classification.md](references/acquisition-and-classification.md) only for Acquire steps 1–6. Load [persistence-and-authority.md](references/persistence-and-authority.md) before proposing a write, revising affected actions, or applying authorized actions. Load [verification-and-reporting.md](references/verification-and-reporting.md) for acquisition reports, write previews, Apply verification, and detailed final reports. The Cancel route is self-contained above and must not load any reference.

## Core invariants

- Nature and disposition are separate. `Canonical` is never a primary nature.
- The code proves implemented behavior or technical results, not automatically product, method, or architecture intent.
- One conversational passage may yield several linked actions for distinct persistent aspects; never copy the same meaning into multiple sources.
- Material product, method, or architecture decisions require explicit user approval unless that exact decision was explicitly delegated to Codex.
- A general confirmation approves a material decision only when the preview contains the explicit section `Decisioni materiali che questa conferma approverà` and lists the corresponding `M` identifiers.
- No write occurs before a complete, concise preview and explicit confirmation.
- Never commit, push, or create a branch unless the user explicitly requests it.
- Protect Historical artifacts according to their role; do not append later evolution to a consolidated milestone summary.
- A fallback is temporary reconciliation work, never a final state or implicit decision.
- A suspended or partially applied outcome is recoverable only when the remaining work is persisted outside the conversation.

## Preview contract

Assign a stable preview identifier and stable action identifiers:

- `W1`, `W2`, ... for proposed writes;
- `M1`, `M2`, ... for material decisions whose substantive approval is requested.

For every `W` action show source, target registration, create/update operation, semantic delta, reason, dependencies, fallback if applicable, and whether it depends on an `M` approval. Group no-write and already-correct aspects compactly.

Do not execute a write during preview generation. A revision invalidates the prior preview and creates a new one. Cancellation makes the referenced preview terminal. Applied previews are terminal. If a target changes after preview, proceed without a new preview only when the approved effect, target identity, and delta safety remain unchanged and no new content is overwritten or invalidated; otherwise invalidate and re-preview.

## Final responsibility

The run is complete only when every significant aspect in the frozen acquisition window has a verified disposition and none remains solely in the chat. State clearly what was recognized, changed, left unchanged, reconciled, or left incomplete.
