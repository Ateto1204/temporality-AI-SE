**Fix**

- [fastapi/dependencies/utils.py](/Users/ateto/dev/temporality-AI-SE/repos/fastapi/fastapi/dependencies/utils.py) now deep-copies the `FieldInfo` extracted from `Annotated` before assigning a default. This prevents `APIRouter` from mutating the shared `Query()` metadata during its first pass, which was causing the second pass during `include_router()` to hit the assertion.

**Tests**

- Modified [tests/test_ambiguous_params.py](/Users/ateto/dev/temporality-AI-SE/repos/fastapi/tests/test_ambiguous_params.py).
- Added a regression test that defines a route on `APIRouter` with `n: Annotated[float, Query()] = 50`, includes the router into a `FastAPI` app, and verifies the request succeeds with the default value.

**Verification**

- `./.venv/bin/python - <<'PY' ... PY` with the router example passed and returned `{"n": 50.0}`.
- `./.venv/bin/python -m pytest tests/test_ambiguous_params.py -q` could not run in this environment because the local venv’s pytest stack is incompatible with the installed Python 3.13 runtime (`traceback_exception_format() got an unexpected keyword argument 'colorize'`).
- `./.venv/bin/python -m pytest tests/test_annotated.py -q` failed for the same environment issue.

**Remaining uncertainty**

- The code change is verified by direct execution, but I could not complete the pytest suite here because of the local Python/pytest incompatibility.
