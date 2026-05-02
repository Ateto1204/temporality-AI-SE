# Leakage Audit

## Repository

FastAPI

## Target Issue

#9387

## Base Release

0.95.0

## Audited Files

- `dataset/fastapi/issues/9387/issue_for_agent.md`
- `dataset/fastapi/issues/9387/excluded_artifacts.md`
- `dataset/fastapi/evidence/past_window.md`
- `dataset/fastapi/evidence/future_window.md`
- `dataset/fastapi/notes/9387/past.md`
- `dataset/fastapi/notes/9387/future.md`

## Audit Purpose

This audit checks whether the agent-facing issue description and temporal notes leak target-solution information for FastAPI issue #9387.

The goal is to ensure that Past/Future Notes provide temporal context at the feature-story level rather than implementation-level hints or direct solution evidence.

## Leakage Criteria

A file is considered risky if it includes any of the following in agent-facing materials:

- Target fixing pull request
- Fixing commit
- Direct root-cause explanation
- Direct implementation strategy
- Internal function names
- Internal file names
- Stack trace locations
- Regression test names
- Release-note entries that directly describe the target fix
- Future APIs, dependencies, or implementation structures stated as if they already exist in the base release

## Issue Sanitization Check

### `raw_issue_thread.md`

Verdict: Preserved as raw evidence, not agent-facing.

Notes:

- The raw issue thread preserves the original issue content, including the discussion link, fixing PR reference, full stack trace, reproduction code, environment, and additional context.
- This file must not be directly included in agent prompts.

### `issue_for_agent.md`

Verdict: Pass

Notes:

- The agent-facing issue description preserves the minimal reproduction, observed assertion error, expected behavior, FastAPI version, Python version, and operating system.
- The fixing PR reference is removed.
- The linked discussion reference is removed.
- The full internal stack trace is removed.
- The remaining assertion message is necessary to describe the observed failure.

Potential concern:

- The issue description mentions that the behavior works when the path operation is defined directly on the main app instead of through `APIRouter`. This is retained because it is part of the user-observed behavior and does not reveal the concrete fix.

## Excluded Artifact Check

### `excluded_artifacts.md`

Verdict: Pass

Notes:

- The file explicitly documents the removal of the fixing PR reference.
- The file explicitly documents the removal of the linked discussion reference.
- The file documents that the full stack trace was excluded from the agent-facing issue prompt.
- The file provides a clear rationale for each exclusion.

## Past Note Check

### `past.md`

Verdict: Pass

Notes:

- The Past Note describes historical design context before FastAPI 0.95.0.
- It focuses on type-hint-driven API design, parameter/dependency declaration consistency, developer ergonomics, compatibility, and predictable route registration.
- It does not mention issue #9387.
- It does not mention PR #9315.
- It does not mention discussion #9279.
- It does not include internal file names, function names, line numbers, or direct fix strategies.
- It does not state that future APIs or future implementation structures exist in the base release.

Potential concern:

- The note discusses type hints, function signatures, and route registration, which are related to the issue domain. This is acceptable because they are project-level design tendencies rather than target-specific solution details.

## Future Note Check

### `future.md`

Verdict: Pass

Notes:

- The Future Note describes later project evolution at a feature-story level.
- It focuses on type-metadata-based declarations, consistency across routing contexts, validation behavior, dependency handling, and documentation generation.
- It does not mention issue #9387.
- It does not mention PR #9315.
- It does not mention discussion #9279.
- It does not include internal file names, function names, line numbers, regression test names, or direct fix strategies.
- It explicitly states that future information should not be treated as implementation details available in the base release.

Potential concern:

- The note is semantically close to the target issue domain because the issue itself concerns type-driven parameter declarations and router behavior.
- This is acceptable for the pilot because the note remains at the feature-story level and does not reveal the concrete fix.

## Overall Verdict

Pass for pilot use.

The current dataset artifacts appear suitable for a pilot run. The agent-facing issue and temporal notes avoid direct answer leakage while preserving enough context to test whether temporal information affects the agent's behavior.

## Remaining Risks

- The Past/Future Window Evidence files are currently pilot-level evidence and should later be strengthened with more precise release-note entries and source references.
- The Future Note is close to the issue domain, which is expected for a relevant temporal context but should be monitored during evaluation.
- Before formal use, all generated agent prompts should be checked to ensure they include only `issue_for_agent.md` and the selected Past/Future Notes, not `raw_issue_thread.md`.
