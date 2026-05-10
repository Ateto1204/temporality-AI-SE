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

Past Note:
# Past Note

## Scope

- Repository: pytest
- Base release: 7.2.0
- Temporal position: before the base release
- Release window: 7.0.0 to 7.1.x

## Evolution Story

Before the base release, pytest had already been shaped by a strong commitment to compatibility with existing test suites, including projects that mixed pytest features with unittest-style test classes. Fixture behavior, marker interpretation, class-based collection, and unittest integration were established compatibility surfaces. Changes in these areas could affect downstream projects because many suites rely on subtle interactions among inheritance, class-level markers, and fixture setup behavior.

## Stable Design Tendencies

- pytest tends to preserve compatibility with existing test suites, especially where users rely on established collection and fixture behavior.
- unittest-style test class support is an established compatibility boundary rather than a peripheral feature.
- Fixture setup behavior is expected to remain predictable across common test organization styles.
- Class-level markers such as fixture-related markers can influence setup behavior and should interact consistently with class inheritance.
- Changes to collection, markers, and fixture resolution should be handled cautiously because downstream projects may depend on subtle behavior.

## Behavioral Expectations

- Existing unittest-style test suites should continue to run when they combine pytest fixtures with class-based test structures.
- Fixture behavior should remain predictable when parent and subclass test classes both participate in fixture-related setup.
- Class inheritance should not unexpectedly prevent fixture behavior that existing suites reasonably relied on.
- Compatibility with legacy or mixed test styles should be preserved unless a deliberate breaking change is clearly justified.
- Regression fixes should avoid broad changes to the fixture system or unittest integration unless necessary.

## Constraints and Non-goals

- This note does not describe a direct fix for any specific issue.
- This note does not imply that later APIs, later implementation structures, or later regression tests exist in the base release.
- This note should not be treated as an instruction to rewrite pytest's fixture system, marker system, collection model, or unittest integration broadly.
- Any patch should remain grounded in the checked-out base release and should avoid unrelated refactoring.

## Risk of Misuse

This note describes historical design context that had already shaped pytest before the base release. It should be used only as background for understanding pytest's established compatibility expectations, not as a direct solution guide.

Instructions:
1. Use the Past Note only as historical context already valid before the base release.
2. Do not treat it as a direct solution guide.
3. Verify all implementation choices against the current codebase.
4. Do not assume future APIs, dependencies, files, or designs.
5. Keep the patch minimal and maintainable.
6. Run relevant tests if possible.
7. Summarize your changes and tests run.
