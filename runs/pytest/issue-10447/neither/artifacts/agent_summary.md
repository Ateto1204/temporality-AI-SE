Files changed:

- [src/\_pytest/fixtures.py](/Users/ateto/dev/temporality-AI-SE/repos/pytest/src/_pytest/fixtures.py)
- [testing/test_unittest.py](/Users/ateto/dev/temporality-AI-SE/repos/pytest/testing/test_unittest.py)

Summary of the fix:

- Adjusted `FixtureManager.getfixtureinfo()` so `usefixtures` resolution for `unittest.TestCase` items preserves parent-class fixtures before subclass fixtures.
- The fix only special-cases unittest-style items and keeps the existing marker behavior for normal tests unchanged.
- Added a regression test covering a base `unittest.TestCase` with `usefixtures` and a subclass whose fixture depends on the parent fixture having already run.

Tests added or modified:

- Added `test_usefixtures_marker_on_unittest_inheritance` in [testing/test_unittest.py](/Users/ateto/dev/temporality-AI-SE/repos/pytest/testing/test_unittest.py).

Tests run and results:

- `PYTHONPATH=src /private/tmp/pytest-venv-312/bin/python -m pytest -q -W ignore::DeprecationWarning -W ignore::RuntimeWarning testing/test_unittest.py -k 'usefixtures_marker_on_unittest'`
- Result: `3 passed, 71 deselected`

Remaining uncertainty:

- I did not run the full test suite.
- The local Python 3.12 environment emits unrelated `RuntimeWarning` noise from `unittest`; I filtered that out for the targeted validation run.
