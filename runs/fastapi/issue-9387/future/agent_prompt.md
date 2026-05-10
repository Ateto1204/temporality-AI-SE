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

Future Note:
# Future Note

## Scope

- Repository: FastAPI
- Base release: 0.95.0
- Temporal position: after the base release
- Release window: 0.95.1 to 0.100.0

## Evolution Story

After the base release, FastAPI continued moving toward broader use of Python typing metadata as a central way to declare API behavior. Later evolution suggests increasing attention to making type-driven parameter declarations behave consistently across routing contexts, validation behavior, dependency handling, and generated documentation. The project also continued stabilizing the interaction between developer-facing declaration patterns and the underlying framework/runtime behavior.

## Emerging Design Tendencies

- Later releases suggest increasing attention to making `Annotated`-style declarations reliable as part of FastAPI's recommended developer experience.
- Subsequent evolution indicates that parameter metadata, validation behavior, routing behavior, and documentation generation needed to remain consistent with one another.
- The project gradually moved toward stronger compatibility between documented declaration patterns and actual runtime behavior.
- Future evolution shows continued attention to reducing surprising failures during application startup or route registration.
- Later changes suggest that type-driven API declarations were expected to work across common application structures, not only in the simplest direct-route cases.

## Emerging Behavioral Expectations

- Documented parameter declaration patterns should behave consistently across common routing contexts.
- Route registration should not fail unexpectedly when user code follows a supported type-driven declaration style.
- Parameter metadata should remain usable for validation and documentation without creating inconsistent runtime behavior.
- Framework behavior should remain predictable when users compose applications with routers and shared route definitions.
- Developer-facing errors should distinguish between real misuse and valid declaration patterns that the framework should support.

## Constraints and Non-goals

- This note does not describe the target issue, its root cause, or its concrete fix.
- This note does not imply that later APIs, dependencies, files, or implementation structures exist in the base release.
- This note should not be treated as a list of implementation instructions.
- This note should not be used to copy later code or reproduce a future patch.
- Any patch should remain grounded in the checked-out base release and should avoid broad rewrites of routing, validation, dependency analysis, or documentation generation.

## Risk of Misuse

This note describes later project evolution after the base release. It should be used only as high-level temporal context about where the project later moved, not as evidence that future implementation details are available in the base release.

Instructions:
1. Use the Future Note only as high-level later-evolution context.
2. Do not assume future APIs, dependencies, files, configuration formats, or designs exist in the base release.
3. Do not copy future implementation strategies.
4. Verify every implementation choice against the current codebase.
5. Keep the patch minimal and maintainable.
6. Run relevant tests if possible.
7. Summarize your changes and tests run.
