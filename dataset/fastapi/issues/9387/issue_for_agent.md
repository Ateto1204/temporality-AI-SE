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
