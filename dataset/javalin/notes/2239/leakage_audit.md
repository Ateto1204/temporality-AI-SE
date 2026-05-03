# Leakage Audit

## Repository

Javalin

## Target Issue

#2239

## Base Release

javalin-parent-5.6.4

## Audited Files

- `dataset/javalin/issues/2239/issue_for_agent.md`
- `dataset/javalin/issues/2239/excluded_artifacts.md`
- `dataset/javalin/evidence/past_window.md`
- `dataset/javalin/evidence/future_window.md`
- `dataset/javalin/notes/2239/past.md`
- `dataset/javalin/notes/2239/future.md`

## Audit Purpose

This audit checks whether the agent-facing issue description and temporal notes leak target-solution information for Javalin issue #2239.

The goal is to ensure that Past/Future Notes provide temporal context at the feature-story level rather than implementation-level hints or direct solution evidence.

## Leakage Criteria

A file is considered risky if it includes any of the following in agent-facing materials:

- Target fixing pull request
- Fixing commit
- Direct root-cause explanation
- Direct implementation strategy
- Internal Javalin file names
- Internal Javalin function or method names
- Full stack trace locations
- Regression test names
- Release-note entries that directly describe the target fix
- Future Java APIs, dependencies, or implementation structures stated as if they already exist in the base release
- Future platform requirements treated as valid for the 5.x base release

## Issue Sanitization Check

### `raw_issue_thread.md`

Verdict: Preserved as raw evidence, not agent-facing.

Notes:

- The raw issue thread preserves the original issue content, including the full reporter description, runtime environment, stack trace details, and any root-cause hypotheses.
- This file must not be directly included in agent prompts.
- Any explicit hypothesis about a newer build/runtime mismatch should remain in raw evidence or excluded artifacts, not in the agent-facing issue prompt.

### `issue_for_agent.md`

Verdict: Pass

Notes:

- The agent-facing issue description preserves the observed release-to-release regression: Javalin 5.6.3 worked, while Javalin 5.6.4 fails on JDK 17.
- It preserves the behavioral context: the failure occurs when setting a cookie through the request context.
- It preserves the final runtime error message, which is necessary to describe the observed failure.
- It avoids giving a direct implementation strategy or naming a fixing pull request or commit.
- It avoids presenting future platform assumptions as a valid solution for the base release.

Potential concern:

- The error message includes `java.util.List.removeFirst()`, which is a strong clue about runtime API compatibility. This is retained because it is the observed runtime failure, but the agent-facing issue should not include additional explanation that directly identifies the root cause or fix.

## Excluded Artifact Check

### `excluded_artifacts.md`

Verdict: Pass

Notes:

- The file documents that root-cause hypotheses related to build/runtime version mismatch are excluded from the agent-facing issue prompt.
- The file documents that Java-version-specific API explanations are excluded to avoid over-directing the agent.
- The file documents that full internal stack trace details are excluded from the agent-facing issue prompt.
- The file distinguishes preserved raw evidence from information allowed in the final agent-facing issue.

## Past Note Check

### `past.md`

Verdict: Pass

Notes:

- The Past Note describes historical design context before Javalin 5.6.4.
- It focuses on minor-release compatibility, JVM runtime compatibility, HTTP context stability, cookie behavior, and build/runtime assumptions.
- It does not mention issue #2239 as a solution source.
- It does not mention a fixing pull request or fixing commit.
- It does not include internal Javalin file names, function names, line numbers, or direct implementation strategies.
- It does not state that future Java APIs or future platform assumptions are available in the base release.

Potential concern:

- The note discusses runtime compatibility and cookie behavior, which are closely related to the target issue. This is acceptable because they describe the issue domain and historical compatibility expectations, not the concrete target fix.

## Future Note Check

### `future.md`

Verdict: Pass

Notes:

- The Future Note describes later project evolution at the feature-story level.
- It focuses on runtime compatibility, platform evolution, release-line compatibility, and the need to distinguish future platform assumptions from the base release.
- It does not mention a fixing pull request, fixing commit, regression test name, or internal implementation location.
- It does not describe the target issue’s concrete root cause or fix.
- It explicitly states that future Java APIs, later server components, later dependencies, and future implementation structures should not be assumed to exist in the base release.

Potential concern:

- The note is semantically close to the target issue domain because the issue concerns runtime compatibility and HTTP context cookie behavior.
- This is acceptable for the pilot because the note remains at the feature-story level and does not reveal implementation-level repair information.

## Overall Verdict

Pass for pilot use.

The current dataset artifacts appear suitable for a pilot run. The agent-facing issue and temporal notes avoid direct answer leakage while preserving enough context to test whether temporal information affects the agent’s behavior.

## Remaining Risks

- The issue’s runtime error message is inherently informative and may guide the agent toward a compatibility-oriented fix.
- The Past/Future Window Evidence files are pilot-level evidence and should later be strengthened with precise release-note entries and source references.
- The Future Note is intentionally close to the issue domain because the task is about release-line runtime compatibility; this should be monitored during evaluation.
- Before formal use, generated agent prompts should be checked to ensure they include only `issue_for_agent.md` and the selected Past/Future Notes, not `raw_issue_thread.md`.
