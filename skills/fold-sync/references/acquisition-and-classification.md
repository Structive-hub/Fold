# Acquisition and classification

Use this reference for a new `$fold-sync N` analysis. Keep the acquisition perimeter distinct from all supporting context.

## Freeze the window

`N` counts the last `N` user messages before the invocation. Select the oldest of those messages as the start and include every chronological event from there until just before the invocation: user messages, assistant messages, commentary, tool calls, and tool outputs that are visible to the runtime.

Report:

- requested `N`;
- first and last selected user message in a safely identifiable form;
- included event types;
- any unavailable message identifiers or timestamps as observability limits.

Do not infer an exact window when the visible history is insufficient.

## Minimum interpretation context

If the first selected user message depends on a preceding reference such as “Sì, approvo”, consult only the minimum preceding content required to resolve it. Record that content separately as `interpretation_context`.

Interpretation context:

- is outside `selected_window`;
- is not an intermediate event;
- cannot produce an autonomous candidate;
- must not be expanded beyond what is necessary.

If the reference remains uncertain, suspend the dependent candidate instead of guessing. The runtime may expose more prior history than the report uses; record that as an observability limit, not as evidence that the boundary failed.

## Significance test

An element is significant when losing it would materially impair at least one of:

- continuing Fold correctly;
- governing work, scope, dependencies, or completion;
- verifying a delivered result;
- reconstructing a significant product or design passage.

Narrative interest alone is insufficient. A still-vague topic can be significant when it already blocks work, changes a completion criterion, or introduces a concrete risk.

Significance is independent of whether persistence is newly required. An aspect already recoverable from a source authoritative for that meaning remains significant and receives `already represented correctly` when appropriate.

## Split and classify

Split one passage into distinct persistent aspects when necessary. Classify each aspect by primary nature:

- `evidence_or_research`;
- `insight_or_hypothesis`;
- `decision`;
- `future_work`;
- `result`.

Record separately any operational consequence, verification evidence, or relationship required to preserve meaning. Do not classify `Canonical` as a nature; it is a possible later status or disposition.

## Progressive source consultation

Start with the governance sources. For each candidate, consult only what is needed to interpret, verify, route, and detect an existing equivalent:

- repository documents or code relevant to that exact meaning;
- the pertinent Linear issue, milestone, dependency, checkpoint, or closure;
- the pertinent Notion research, insight, or narrative record.

Do not turn governance documents into audit objects. Do not widen the run into a general project audit. Significant but independent information encountered incidentally may be mentioned only when it exposes a material limit; do not acquire or follow it in this run.

## Determine the disposition

For every aspect choose exactly one current disposition:

- no persistent result required;
- already represented correctly by an authoritative source;
- update an existing registration;
- create a new registration in the appropriate source;
- suspend under a defined recoverable fallback;
- incomplete because no recoverable persistence is possible.

Before choosing create, search the pertinent scope for semantic equivalents. Same wording is not required; compare meaning, scope, time, and role. Do not merge different phases or meanings merely because they concern the same topic.

## Source authority

- Repository: versioned knowledge that must guide design or implementation; approved product, method, or architecture decisions; appropriate implementation behavior and verified technical results.
- Linear: roadmap, milestones, issues, state, dependencies, checkpoints, closures, and operational consequences.
- Notion: extended research, significant insights, hypotheses, design journey, and case-study narrative that must not be required to continue Fold.

For a significant insight persisted in Notion, preserve at least the originating problem or observation, what it suggests, why it may matter, its current state, and when it would make sense to revisit it.

Code is authoritative for observed implementation behavior and technical results only. It does not by itself preserve the intent of a product, method, or architecture decision.

A transformation is a linked chain, not a relocation: `insight → work → possible decision → possible consolidation`. Preserve the meaning of each earlier phase; update it only with appropriate state and links.
