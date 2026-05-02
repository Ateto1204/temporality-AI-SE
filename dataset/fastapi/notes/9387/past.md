# Past Note

## Scope

- Repository: FastAPI
- Base release: 0.95.0
- Temporal position: before the base release
- Release window: 0.90.0 to 0.94.1

## Evolution Story

Before the base release, FastAPI had already been shaped by a strong reliance on Python type hints and function signatures as the primary interface for declaring API behavior. The framework treated parameter declarations, dependency injection, validation behavior, route registration, and generated documentation as closely connected parts of the developer experience. Earlier evolution also shows that compatibility with underlying framework components and type-annotation behavior was already an important concern.

## Stable Design Tendencies

- FastAPI tends to derive user-facing API behavior from Python function signatures and type hints.
- Parameter declarations and dependency declarations are expected to remain predictable across common routing patterns.
- Developer ergonomics, editor support, and documented declaration styles are central to the framework's design.
- Framework-level changes should preserve compatibility with existing application structure where possible.
- Integration with underlying components such as validation and ASGI framework behavior is treated as part of FastAPI's practical stability.

## Behavioral Expectations

- Route registration should behave consistently when users follow documented parameter declaration patterns.
- Parameter metadata should support validation and generated documentation without unexpectedly breaking application startup.
- Similar path operation declarations should not behave differently merely because they are attached through common routing structure.
- User-facing errors should reflect real misuse rather than rejecting documented or otherwise valid declaration styles.

## Constraints and Non-goals

- This note does not describe a direct fix for any specific issue.
- This note does not imply that later APIs, later dependencies, or later implementation structures exist in the base release.
- This note should not be treated as an instruction to rewrite routing, dependency analysis, validation, or documentation generation broadly.
- Any patch should remain grounded in the checked-out base release and should avoid unrelated refactoring.

## Risk of Misuse

This note describes historical design context that had already shaped FastAPI before the base release. It should be used only as background for understanding the project's established design tendencies and compatibility expectations, not as a direct solution guide.
