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
