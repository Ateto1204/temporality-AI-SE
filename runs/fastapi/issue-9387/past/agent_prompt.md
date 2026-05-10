# Agent Task

Repository:
fastapi

Base release:
0.95.0

Issue:
# Target Issue

## Repository

FastAPI

## Base Release

0.95.0

## Title

`Query` default value cannot be set in `Annotated` when using `APIRouter`

## Summary

When using `Annotated` with `Query()` in a route defined on `APIRouter`, FastAPI raises an assertion error during application startup if the default value is provided with `=` in the function signature.

The same pattern is expected to work according to the FastAPI documentation on default values. It also works when the path operation is defined directly on the main `FastAPI` app instead of being included through `APIRouter`.

## Example Code

main.py:

    from fastapi import FastAPI
    from router import router

    app = FastAPI()
    app.include_router(router)

router.py:

    from typing import Annotated
    from fastapi import APIRouter, Query

    router = APIRouter()

    @router.get("/")
    async def root(*, n: Annotated[float, Query()] = 50):
        return {"n": n}

## Actual Behavior

Starting the application with:

    uvicorn main:app

raises an assertion error during application startup:

    AssertionError: `Query` default value cannot be set in `Annotated` for 'n'. Set the default value with `=` instead.

## Expected Behavior

The application should start successfully.

The default value should be accepted when the default is provided with `=` in the function signature, while `Query()` is used inside `Annotated`.

## Environment

- Operating system: Linux / Ubuntu 22.04
- FastAPI version: 0.95.0
- Python version: 3.10.6

## Evaluation Hint

A valid patch should allow the example above to be registered through `APIRouter` without raising the assertion error at startup.

Past Note:
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

Instructions:
1. Use the Past Note only as historical context already valid before the base release.
2. Do not treat it as a direct solution guide.
3. Verify all implementation choices against the current codebase.
4. Do not assume future APIs, dependencies, files, or designs.
5. Keep the patch minimal and maintainable.
6. Run relevant tests if possible.
7. Summarize your changes and tests run.
