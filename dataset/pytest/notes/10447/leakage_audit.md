# Leakage Audit

## Repository

pytest

## Target Issue

#10447

## Base Release

7.2.0

## Audited Files

- `dataset/pytest/issues/10447/issue_for_agent.md`
- `dataset/pytest/issues/10447/excluded_artifacts.md`
- `dataset/pytest/evidence/past_window.md`
- `dataset/pytest/evidence/future_window.md`
- `dataset/pytest/notes/10447/past.md`
- `dataset/pytest/notes/10447/future.md`

## Audit Purpose

This audit checks whether the agent-facing issue description and temporal notes leak target-solution information for pytest issue #10447.

The goal is to ensure that Past/Future Notes provide temporal context at the feature-story level rather than implementation-level hints or direct solution evidence.

## Leakage Criteria

A file is considered risky if it includes any of the following in agent-facing materials:

- Target fixing pull request
- Fixing commit
- Direct root-cause explanation
- Direct implementation strategy
- Internal pytest file names
- Internal pytest function names
- Stack trace locations
- Regression test names
- Release-note entries that directly describe the target fix
- Future APIs, files, or implementation structures stated as if they already exist in the base release

## Issue Sanitization Check

### `raw_issue_thread.md`

Verdict: Preserved as raw evidence, not agent-facing.

Notes:

- The raw issue thread preserves the original issue context and should be kept for auditability.
- The raw thread may contain external references, comments, or later discussion that should not be directly included in agent prompts.
- This file must not be directly included in agent prompts.

### `issue_for_agent.md`

Verdict: Pass

Notes:

- The agent-facing issue description preserves the high-level observed failure after upgrading to pytest 7.2.
- It describes the relevant test structure: unittest-style classes, subclassing, and class-level `usefixtures`.
- It preserves the expected compatibility behavior without naming a fixing PR, commit, regression test, internal file, or internal function.
- It does not provide a concrete implementation strategy.

Potential concern:

- The issue prompt mentions `usefixtures`, subclassing, and unittest-style classes. This is acceptable because these are necessary to describe the user-observed behavior and do not reveal the concrete fix.

## Excluded Artifact Check

### `excluded_artifacts.md`

Verdict: Pass

Notes:

- The file documents that upstream issue references and full comments should be excluded from the agent-facing prompt.
- It records that maintainer analysis, root-cause discussion, fixing commits, pull requests, regression test names, and implementation-level analysis should not be included.
- It distinguishes preserved raw evidence from agent-facing task information.

## Past Note Check

### `past.md`

Verdict: Pass

Notes:

- The Past Note describes historical design context before pytest 7.2.0.
- It focuses on compatibility with existing test suites, unittest-style class support, fixture behavior, marker interpretation, and class-based collection.
- It does not mention issue #10447 as a solution source.
- It does not mention any fixing PR or fixing commit.
- It does not mention regression test names.
- It does not include internal pytest file names, function names, line numbers, or direct implementation strategies.
- It does not state that future implementation structures exist in the base release.

Potential concern:

- The note discusses unittest-style classes, `usefixtures`, and class inheritance, which are closely related to the target issue. This is acceptable because they describe the issue domain and established project behavior, not the target solution.

## Future Note Check

### `future.md`

Verdict: Pass

Notes:

- The Future Note describes later project evolution at a feature-story level.
- It focuses on compatibility regression recovery, fixture behavior, marker interpretation, collection semantics, and unittest-style suite compatibility.
- It does not mention a fixing PR, fixing commit, regression test name, or internal implementation location.
- It does not describe the target issue's concrete root cause or fix.
- It explicitly states that future information should not be treated as implementation details available in the base release.

Potential concern:

- The note is semantically close to the target issue domain because the issue concerns fixture behavior, class inheritance, and unittest integration.
- This is acceptable for the pilot because the note remains at the feature-story level and does not reveal implementation-level repair information.

## Overall Verdict

Pass for pilot use.

The current dataset artifacts appear suitable for a pilot run. The agent-facing issue and temporal notes avoid direct answer leakage while preserving enough context to test whether temporal information affects the agent's behavior.

## Remaining Risks

- The current raw issue thread may not yet include all GitHub comments if it was not exported with `gh issue view --comments`.
- The Past/Future Window Evidence files are pilot-level evidence and should later be strengthened with more precise changelog entries and source references.
- The Future Note is close to the issue domain, which is expected for relevant temporal context but should be monitored during evaluation.
- Before formal use, generated agent prompts should be checked to ensure they include only `issue_for_agent.md` and the selected Past/Future Notes, not `raw_issue_thread.md`.
