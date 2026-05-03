# Past Window Evidence

## Repository

pytest

## Base Release

7.2.0

## Temporal Position

Before the base release

## Release Window

7.0.0 to 7.1.x

## Purpose

This file collects release-window evidence before pytest 7.2.0. It will be used to generate the Past Note for issue #10447.

The Past Note should describe design tendencies, behavioral expectations, compatibility concerns, and constraints that had already shaped pytest before the base release.

This file is evidence, not the final Past Note. It may contain concrete release-note entries, but the generated Past Note should later be rewritten into feature-story-level language.

## Source

pytest changelog:
https://docs.pytest.org/en/stable/changelog.html

## Raw Evidence

### Pre-7.2.0 context

Before pytest 7.2.0, pytest already supported both native pytest-style tests and unittest-style test classes. This compatibility mattered because many existing projects relied on pytest to run legacy unittest-based suites while still using pytest features such as fixtures, markers, and collection behavior.

The issue #10447 concerns this compatibility boundary: unittest-style inheritance, class-level fixture usage, and fixture ordering expectations.

### Evidence from pytest 7.0.x to 7.1.x

#### Compatibility with existing test suites

pytest's evolution before 7.2.0 continued to emphasize compatibility with existing test suites and plugins. Changes to collection, fixture handling, and unittest integration could affect downstream projects, so preserving expected behavior across established test patterns remained important.

Relevant high-level signal:

- pytest needed to support legacy unittest-style test classes.
- pytest features such as `usefixtures` could interact with class-based test structures.
- Backward compatibility was important because downstream suites could rely on subtle collection and fixture behavior.

#### Fixture behavior and class-based tests

Before the base release, fixture behavior was already a core part of pytest's model. In class-based tests, fixture setup and marker interpretation needed to remain predictable across inheritance and collection patterns.

Relevant high-level signal:

- Fixture behavior was expected to be stable across common test organization styles.
- Class-level fixture markers could influence setup behavior.
- Changes to fixture resolution or marker handling could create compatibility regressions.

#### Collection and unittest integration

pytest's collection system had to bridge pytest-native tests and unittest-style tests. This made collection behavior sensitive: small changes in how classes, subclasses, markers, or fixtures are interpreted could alter test execution order or fixture availability.

Relevant high-level signal:

- unittest integration was an established compatibility surface.
- Class inheritance and test collection behavior were not isolated details; they affected whether existing suites continued to run.
- pytest's behavior needed to remain consistent for projects that mixed unittest conventions with pytest fixtures.

## Initial Observations

- pytest already treated backward compatibility with existing test suites as an important design concern before 7.2.0.
- Fixture handling was a central compatibility surface.
- unittest-style class support was an established part of pytest's behavior.
- Class inheritance, collection behavior, and fixture markers could interact in subtle ways.
- For issue #10447, the historically relevant context is not a specific fix, but pytest's established expectation that fixture behavior should remain compatible across common class-based test patterns.

## Notes for Past Note Generation

The Past Note should not mention:

- issue #10447
- any fixing PR or fixing commit
- regression test names
- internal pytest file names or function names
- direct implementation strategies

The Past Note may mention, at a feature-story level:

- backward compatibility with existing test suites
- support for unittest-style classes
- fixture behavior as a compatibility surface
- predictable class-based collection behavior
- caution around inheritance, markers, and fixture setup expectations
