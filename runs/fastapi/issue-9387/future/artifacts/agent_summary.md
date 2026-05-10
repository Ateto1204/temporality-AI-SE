Files changed:

- [fastapi/dependencies/utils.py](file:///Users/ateto/dev/temporality-AI-SE/repos/fastapi/fastapi/dependencies/utils.py#L385)
- [tests/test_ambiguous_params.py](file:///Users/ateto/dev/temporality-AI-SE/repos/fastapi/tests/test_ambiguous_params.py#L70)

Summary of the fix:

- `Annotated` parameter metadata is now deep-copied before FastAPI applies the signature default.
- That avoids mutating shared `FieldInfo` state during router inclusion, which is the path that was tripping the startup assertion for `APIRouter` routes.

Tests added or modified:

- Added a regression test covering `APIRouter` with `n: Annotated[float, Query()] = 50`.

Tests run and results:

- `python3 -m py_compile fastapi/dependencies/utils.py tests/test_ambiguous_params.py` passed.
- `pytest -q tests/test_ambiguous_params.py -q` could not run in this environment because the local test environment is missing dependencies needed by the repo configuration.

Remaining uncertainty:

- Full runtime verification is still blocked by missing installed test dependencies, so I could only do syntax-level validation here.
