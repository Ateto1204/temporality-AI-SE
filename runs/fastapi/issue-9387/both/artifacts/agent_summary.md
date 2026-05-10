Changed file:

- [`fastapi/dependencies/utils.py`](/Users/ateto/dev/temporality-AI-SE/repos/fastapi/fastapi/dependencies/utils.py)

Summary of the fix:

- I made `Annotated` parameter analysis idempotent for router registration by deep-copying the `FieldInfo` metadata before inspecting it.
- The default-value assertion now still rejects real misuse like `Query(default=...)` inside `Annotated`, but allows the same parameter to be analyzed again when the signature default is already the intended value.
- This keeps the `APIRouter` inclusion path from tripping startup on the documented `Annotated[float, Query()] = 50` pattern.

Tests added or modified:

- None by me.
- There is already a regression test for this case in the worktree at [`tests/test_ambiguous_params.py`](/Users/ateto/dev/temporality-AI-SE/repos/fastapi/tests/test_ambiguous_params.py); I left it unchanged.

Tests run and results:

- `./.venv/bin/python -m py_compile fastapi/dependencies/utils.py` passed.
- A direct runtime check passed:
  - `Annotated[float, Query(default=1)] = 50` still raises the expected assertion.
  - The router example from the issue registers successfully through `app.include_router(router)`.

Remaining uncertainty:

- I could not run `pytest` end-to-end in this checkout because the local `.venv` is on Python 3.13 and the bundled pytest/trio stack fails during startup with an environment compatibility error.
