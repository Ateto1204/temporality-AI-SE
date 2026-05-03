author:	jaraco
association:	contributor
edited:	false
status:	none
--
To be sure, these tests deserve a refactor. The tests are in this state because the project is transitioning away from unittest, but some artifacts remain.
--
author:	jaraco
association:	contributor
edited:	false
status:	none
--
Probably `plugin:unittest` is not relevant here, because the class hierarchy is no longer based on `unittest.TestCase`. I mention unittest because it explains why the fixtures reference `request.instance` as `self` (an artifact of the expectation when they did rely on `TestCase`).
--
author:	RonnyPfannschmidt
association:	member
edited:	false
status:	none
--
this may be related to extraction of marks from the mro, (dint happenbefore, was aded recently
--
author:	jaraco
association:	contributor
edited:	false
status:	none
--
The MRO refactor was #7792 (31df38f6a79b0734be3c1386eb7df6512b1a321b). I've confirmed that the distutils fail on 31df38f6a79b0734be3c1386eb7df6512b1a321b but pass on 31df38f6a79b0734be3c1386eb7df6512b1a321b^1, confirming that change is the culprit.

The changelog says:

> When inheriting marks from super-classes, the `pytestmark` attribute of the sub-class now only contains the marks directly applied to it. Previously, it also contained marks from its super-classes.

That implies that it's intentional that previously reachable marks are now intentionally ignored.

I'm not sure why that wouldn't be a breaking change.

Is there any chance pytest will restore support for this use-case? Is there a way to apply a fixture at a superclass and have it take effect in a subclass?
--
author:	RonnyPfannschmidt
association:	member
edited:	false
status:	none
--
The markers should take effect as all of them should land in the node for the class, I'll have to investigate the order difference 
--
author:	jaraco
association:	contributor
edited:	false
status:	none
--
In that case, let me put together a more minimal repro.
--
author:	jaraco
association:	contributor
edited:	true
status:	none
--
Good news. A minimal repro was easy and I learned something:

```python
 draft @ cat test_something.py
import pytest

@pytest.fixture
def add_attr1(request):
    request.instance.attr1 = object()


@pytest.fixture
def add_attr2(request):
    request.instance.attr2 = request.instance.attr1


@pytest.mark.usefixtures('add_attr1')
class Parent:
    pass


@pytest.mark.usefixtures('add_attr2')
class TestThings(Parent):
    def test_attrs(self):
        self.attr1
        self.attr2
```
```
 draft @ pip-run 'pytest@git+https://github.com/pytest-dev/pytest@31df38f6a79b0734be3c1386eb7df6512b1a321b^1' -- -m pytest
  WARNING: Did not find branch or tag '31df38f6a79b0734be3c1386eb7df6512b1a321b^1', assuming revision or ref.
========================================================================= test session starts ==========================================================================
platform darwin -- Python 3.11.4, pytest-7.2.0.dev331+g15ac0349, pluggy-1.2.0
rootdir: /Users/jaraco/draft
plugins: anyio-3.6.2
collected 1 item                                                                                                                                                       

test_something.py .                                                                                                                                              [100%]

========================================================================== 1 passed in 0.00s ===========================================================================
 draft @ pip-run 'pytest@git+https://github.com/pytest-dev/pytest@31df38f6a79b0734be3c1386eb7df6512b1a321b' -- -m pytest
========================================================================= test session starts ==========================================================================
platform darwin -- Python 3.11.4, pytest-7.2.0.dev338+g31df38f6, pluggy-1.2.0
rootdir: /Users/jaraco/draft
plugins: anyio-3.6.2
collected 1 item                                                                                                                                                       

test_something.py E                                                                                                                                              [100%]

================================================================================ ERRORS ================================================================================
_______________________________________________________________ ERROR at setup of TestThings.test_attrs ________________________________________________________________

request = <SubRequest 'add_attr2' for <Function test_attrs>>

    @pytest.fixture
    def add_attr2(request):
>       request.instance.attr2 = request.instance.attr1
E       AttributeError: 'TestThings' object has no attribute 'attr1'

test_something.py:10: AttributeError
======================================================================= short test summary info ========================================================================
ERROR test_something.py::TestThings::test_attrs - AttributeError: 'TestThings' object has no attribute 'attr1'
=========================================================================== 1 error in 0.02s ===========================================================================
```

The issue isn't that the fixture on the parent class isn't being called, but that the fixtures are called in a different order with the fixture on the child being called before the fixture on the parent. Independent of this specific example, I'd expect fixtures on more basic classes to be called first, as the child (derived) class is liable to depend on behavior from the parent but not vice-versa (from a modeling perspective, the parent class is largely unaware of the child classes).
--
author:	RonnyPfannschmidt
association:	member
edited:	false
status:	none
--
Found the bug

https://github.com/pytest-dev/pytest/blob/main/src/_pytest/mark/structures.py#L377 is missing a reversed when considering the mro 

--
author:	RonnyPfannschmidt
association:	member
edited:	false
status:	none
--
@jaraco seems like our timing was unfortuate
--
author:	jaraco
association:	contributor
edited:	false
status:	none
--
No problem. Happy to consolidate. I'll fix the mypy bug in mine and copy the test from yours, but feel free to choose the PR you prefer.
--
author:	RonnyPfannschmidt
association:	member
edited:	false
status:	none
--
@jaraco im under the impression that the content would practically be the same, so i'd just go with mine

--
