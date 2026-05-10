Implemented the compatibility fix in `repos/pytest`.

**Files Changed**

- [fixtures.py](/Users/ateto/dev/temporality-AI-SE/repos/pytest/src/_pytest/fixtures.py:233)
- [test_unittest.py](/Users/ateto/dev/temporality-AI-SE/repos/pytest/testing/test_unittest.py:1093)

**Summary**

- `usefixtures` names from inherited class markers are now gathered base-class-first for class nodes.
- General marker lookup/MRO behavior is unchanged.
- Extra dynamically added class node `usefixtures` markers are still preserved.

**Tests Added**

- Added `test_usefixtures_marker_on_unittest_subclass`, covering a `unittest.TestCase` subclass where the subclass fixture depends on parent fixture effects.

**Tests Run**

- `testing/test_unittest.py::test_usefixtures_marker_on_unittest` + new test: `3 passed`
- `testing/python/fixtures.py::TestFixtureUsages::test_usefixtures_marker` + `TestScopeOrdering`: `10 passed`
- `testing/test_mark.py::test_mark_mro`: `1 passed`
- Full `testing/test_unittest.py`: `65 passed, 9 skipped`
- `git diff --check`: passed

**Remaining Uncertainty**

- The local venv is Python 3.13, while pytest 7.2.0 predates it, so I used warning filters for Python 3.13 deprecations and unittest’s `addDuration` warning during test runs.
