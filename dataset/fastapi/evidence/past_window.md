# Past Window Evidence

## Repository

FastAPI

## Base Release

0.95.0

## Temporal Position

Before the base release

## Release Window

0.90.0 to 0.94.1

## Purpose

This file collects release-window evidence before FastAPI 0.95.0. It will be used to generate the Past Note for issue #9387.

The Past Note should describe design tendencies, behavioral expectations, compatibility concerns, and constraints that had already shaped FastAPI before the base release.

This file is evidence, not the final Past Note. It may contain concrete release-note entries, but the generated Past Note should later be rewritten into feature-story-level language.

## Source

FastAPI official release notes:
https://fastapi.tiangolo.com/release-notes/

## Raw Evidence

### Pre-0.95.0 context

FastAPI is designed around Python type hints and automatic API behavior derived from function signatures, including request parameters, validation, dependency injection, and documentation generation.

Before 0.95.0, FastAPI already emphasized developer ergonomics, editor support, automatic documentation, and predictable behavior from annotated function parameters.

### Evidence from releases before 0.95.0

#### FastAPI 0.94.1

FastAPI 0.94.1 was a small bug-fix release related to type annotations for the newer lifespan behavior and Starlette compatibility.

Relevant high-level signal:

- FastAPI was actively maintaining compatibility around type annotations and framework integration behavior.
- Type annotation correctness was already a concern before 0.95.0.
- Compatibility with Starlette remained part of FastAPI's evolution.

#### FastAPI 0.94.0

FastAPI 0.94.0 introduced support for the newer lifespan protocol, replacing or complementing older startup/shutdown event patterns.

Relevant high-level signal:

- FastAPI was evolving framework lifecycle behavior while preserving application-level ergonomics.
- Changes to framework-level behavior needed to remain compatible with user-facing application structure.
- Route and application registration behavior remained important to framework usability.

#### FastAPI 0.93.x and earlier

FastAPI continued improving documentation, compatibility, and developer-facing behavior around path operations, dependency injection, and generated API documentation.

Relevant high-level signal:

- FastAPI's behavior is strongly tied to Python function signatures.
- The framework relies on parameter metadata to infer request behavior and generated OpenAPI documentation.
- Backward-compatible developer experience is important because user code often depends on documented declaration patterns.

## Initial Observations

- FastAPI already treated Python type hints and function signatures as core API design mechanisms before 0.95.0.
- Dependency injection and parameter declaration behavior were central to FastAPI's developer experience.
- Compatibility with underlying frameworks and libraries, especially Starlette and Pydantic, was already part of the project's evolution.
- Framework changes needed to preserve predictable route registration and documentation behavior.
- The project was moving toward clearer, more type-driven declaration styles even before the explicit `Annotated` recommendation in 0.95.0.

## Notes for Past Note Generation

The Past Note should not mention issue #9387, PR #9315, or the linked GitHub discussion.

The Past Note should avoid implementation-level details such as internal function names, file names, or exact code paths.

The Past Note should focus on:

- Type-hint-driven API design
- Parameter and dependency declaration consistency
- Developer ergonomics
- Compatibility with existing user code
- Predictable route registration behavior
