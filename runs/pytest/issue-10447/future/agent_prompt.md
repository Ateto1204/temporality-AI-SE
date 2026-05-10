# Agent Task

Repository:
pytest

Base release:
7.2.0

Issue:
# Target Issue

## Repository

pytest

## Base Release

7.2.0

## Title

Parent class marked fixture no longer reached with pytest 7.2

## Summary

Starting with pytest 7.2, a test suite that previously worked began failing. The reported failure involves unittest-style test classes where one test class subclasses another, and both classes are marked with `usefixtures`.

The subclass fixture appears to rely on prior execution of a fixture associated with the parent class. After upgrading to pytest 7.2, the expected parent-class fixture behavior is no longer reached before the subclass fixture depends on it.

## Observed Context

The issue was originally observed in the distutils test suite after upgrading to pytest 7.2.

The suspected conditions are:

- A test class is a subclass of another class.
- Both the parent class and subclass are marked with `usefixtures`.
- The subclass fixture relies on prior execution of a fixture associated with the parent class.
- The failure appeared after upgrading to pytest 7.2.

## Actual Behavior

Tests that previously passed begin failing after upgrading to pytest 7.2.

The fixture behavior associated with the parent class is no longer reached before the subclass fixture depends on it.

## Expected Behavior

Fixture behavior involving parent and subclass test classes should remain compatible with the behavior before pytest 7.2.

If both parent and subclass test classes are marked with `usefixtures`, the subclass should still observe the fixture effects expected from the parent-class fixture behavior.

## Environment

- pytest version: 7.2.0
- Test style: unittest-style classes
- Area: fixture handling and unittest integration

## Evaluation Hint

A valid patch should preserve compatible fixture behavior for subclassed unittest-style test classes marked with `usefixtures`, without introducing unrelated changes to pytest's fixture system or unittest integration.

Future Note:
# Future Note

## Scope

- Repository: pytest
- Base release: 7.2.0
- Temporal position: after the base release
- Release window: 7.2.1 to 7.3.x

## Evolution Story

After the base release, pytest continued stabilizing compatibility regressions discovered by downstream projects and users. Later evolution suggests continued attention to the interaction between fixture behavior, marker interpretation, collection semantics, and integration with existing unittest-style suites. The project continued treating regressions in established test patterns as important maintenance concerns, especially when subtle behavior changes affected real-world test suites.

## Emerging Design Tendencies

- Later releases suggest continued attention to regression recovery after behavioral changes in collection, fixtures, markers, or integrations.
- Subsequent evolution indicates that compatibility with existing downstream test suites remained an important maintenance priority.
- The project gradually continued to treat fixture and marker behavior as sensitive compatibility surfaces.
- Future maintenance shows increasing attention to preserving predictable behavior for mixed pytest-style and unittest-style test suites.
- Later evolution suggests that class inheritance, collection behavior, and fixture setup interactions needed to remain stable for established users.

## Emerging Behavioral Expectations

- Compatibility regressions in existing test suites should be corrected when they arise from subtle fixture, marker, or collection interactions.
- Fixture setup behavior should remain predictable across common class-based test patterns.
- unittest-style integrations should continue working when combined with pytest features.
- Marker interpretation should not unexpectedly alter fixture behavior in ways that break established test suites.
- Fixes should be narrow enough to recover compatibility without destabilizing broader fixture or collection behavior.

## Constraints and Non-goals

- This note does not describe the target issue, its root cause, or its concrete fix.
- This note does not imply that later APIs, files, regression tests, or implementation structures exist in the base release.
- This note should not be treated as a list of implementation instructions.
- This note should not be used to copy later code or reproduce a future patch.
- Any patch should remain grounded in the checked-out base release and should avoid broad rewrites of fixture handling, marker interpretation, collection, or unittest integration.

## Risk of Misuse

This note describes later project evolution after the base release. It should be used only as high-level temporal context about where pytest later continued to move, not as evidence that future implementation details are available in the base release.

Instructions:
1. Use the Future Note only as high-level later-evolution context.
2. Do not assume future APIs, dependencies, files, configuration formats, or designs exist in the base release.
3. Do not copy future implementation strategies.
4. Verify every implementation choice against the current codebase.
5. Keep the patch minimal and maintainable.
6. Run relevant tests if possible.
7. Summarize your changes and tests run.
