**Files Changed**

- [src/\_pytest/fixtures.py](/Users/ateto/dev/temporality-AI-SE/repos/pytest/src/_pytest/fixtures.py)
- [testing/test_unittest.py](/Users/ateto/dev/temporality-AI-SE/repos/pytest/testing/test_unittest.py)

**Fix Summary**

- Changed `usefixtures` resolution so class-inherited fixtures are gathered base-first within each class hierarchy, instead of using the flattened MRO order that put subclass fixtures ahead of parent fixtures.
- Kept existing ordering for non-class nodes unchanged.
- Added a regression test covering a `unittest.TestCase` subclass inheriting `usefixtures` from a parent class and depending on the parent fixture’s side effect.

**Tests Added or Modified**

- Added `test_usefixtures_marker_inherited_from_unittest_base` in [testing/test_unittest.py](/Users/ateto/dev/temporality-AI-SE/repos/pytest/testing/test_unittest.py).

**Tests Run and Results**

- Isolated reproducer for the reported inheritance case: passed.
- Isolated sanity check for a plain class with `usefixtures`: passed.
- Isolated sanity check for a `unittest.TestCase` class with `usefixtures`: passed.
- Isolated multiple-inheritance sanity check: passed.
- Attempted to run `testing/test_unittest.py -k usefixtures` directly, but the suite’s `testing/conftest.py` currently fails under the local Python 3.13 environment because of deprecation warnings being promoted to errors.

**Remaining Uncertainty**

- I could not run the repo’s full targeted test module in this environment because of the unrelated `testing/conftest.py` deprecation failure, so the added regression was validated via isolated reproducer instead.
