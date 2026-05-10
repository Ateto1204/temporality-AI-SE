**Files Changed**

- [`src/_pytest/fixtures.py`](/Users/ateto/dev/temporality-AI-SE/repos/pytest/src/_pytest/fixtures.py#L1439)
- [`testing/test_unittest.py`](/Users/ateto/dev/temporality-AI-SE/repos/pytest/testing/test_unittest.py#L1093)

**Summary**

- Fixed `usefixtures` collection so class-inherited markers are gathered in base-to-subclass order when building fixture info.
- Kept general marker semantics intact; the change only affects how `usefixtures` is assembled for fixture setup.
- Added a regression test for a subclassed `unittest.TestCase` where the child fixture depends on the parent fixture having already run.

**Tests Added or Modified**

- Added `test_usefixtures_marker_on_unittest_inherited_class` in [`testing/test_unittest.py`](/Users/ateto/dev/temporality-AI-SE/repos/pytest/testing/test_unittest.py#L1093).

**Tests Run**

- `pytest -W ignore::DeprecationWarning -W ignore::RuntimeWarning testing/test_unittest.py -k test_usefixtures_marker_on_unittest_inherited_class -q`  
  Passed.
- `pytest -W ignore::DeprecationWarning testing/python/fixtures.py -k test_usefixtures_marker -q`  
  Passed.
- Ad hoc repro with a minimal inherited `unittest.TestCase` and parent/child `usefixtures` markers under `.venv/bin/pytest`  
  Passed after the fix.

**Remaining Uncertainty**

- The local Python 3.13 harness still emits an unrelated `RuntimeWarning` from `unittest` about `TestResult` lacking `addDuration`; I filtered that for validation, but I did not change it because it is separate from this regression.
