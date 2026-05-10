Fixed the startup failure by stopping `analyze_param()` from mutating the `FieldInfo` object stored inside `Annotated`. It now copies the `Query()` metadata before applying the signature default, so an endpoint analyzed twice, as happens when a router is included, no longer trips the stale-default assertion. See [fastapi/dependencies/utils.py:386](fastapi/dependencies/utils.py#L386).

I also added a regression test that defines the failing pattern on an `APIRouter`, includes it into a `FastAPI` app, and verifies the default value is accepted and returned. See [tests/test_annotated.py:229](tests/test_annotated.py#L229).

Files changed:

- [fastapi/dependencies/utils.py](fastapi/dependencies/utils.py#L386)
- [tests/test_annotated.py](tests/test_annotated.py#L229)

Tests added or modified:

- Added `test_annotated_query_default_with_router` in `tests/test_annotated.py`

Tests run and results:

- `python3 -m py_compile fastapi/dependencies/utils.py tests/test_annotated.py` succeeded
- `pytest tests/test_annotated.py -q` could not run in this environment because the system `pytest` is missing `trio`
- `./.venv/bin/pytest tests/test_annotated.py -q` could not run because the local venv is missing `starlette`

Remaining uncertainty:

- The patch is syntactically valid and targets the identified mutation bug, but I could not execute the FastAPI test suite here because the available Python environments are incomplete.
