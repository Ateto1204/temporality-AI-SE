### Discussed in https://github.com/tiangolo/fastapi/discussions/9279

<div type='discussions-op-text'>

<sup>Originally posted by **tlinhart** March 19, 2023</sup>

This is a confirmed bug. :bug: There's a fix in https://github.com/tiangolo/fastapi/pull/9315.

### First Check

- [x] I added a very descriptive title here.
- [x] I used the GitHub search to find a similar question and didn't find it.
- [x] I searched the FastAPI documentation, with the integrated search.
- [x] I already searched in Google "How to X in FastAPI" and didn't find any information.
- [x] I already read and followed all the tutorial in the docs and didn't find an answer.
- [x] I already checked if it is not related to FastAPI but to [Pydantic](https://github.com/pydantic/pydantic).
- [x] I already checked if it is not related to FastAPI but to [Swagger UI](https://github.com/swagger-api/swagger-ui).
- [x] I already checked if it is not related to FastAPI but to [ReDoc](https://github.com/Redocly/redoc).

### Commit to Help

- [x] I commit to help with one of those options 👆

### Example Code

```python
# main.py

from fastapi import FastAPI
from router import router

app = FastAPI()
app.include_router(router)

# router.py

from typing import Annotated
from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/")
async def root(*, n: Annotated[float, Query()] = 50):
    return {"n": n}
```

### Description

When starting the Uvicorn server using `uvicorn main:app`, I receive:

```
Traceback (most recent call last):
  File "/home/pasmen/tmp/x-annotated-query-router/./venv/bin/uvicorn", line 8, in <module>
    sys.exit(main())
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/click/core.py", line 1130, in __call__
    return self.main(*args, **kwargs)
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/click/core.py", line 1055, in main
    rv = self.invoke(ctx)
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/click/core.py", line 1404, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/click/core.py", line 760, in invoke
    return __callback(*args, **kwargs)
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/uvicorn/main.py", line 403, in main
    run(
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/uvicorn/main.py", line 568, in run
    server.run()
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/uvicorn/server.py", line 59, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "uvloop/loop.pyx", line 1517, in uvloop.loop.Loop.run_until_complete
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/uvicorn/server.py", line 66, in serve
    config.load()
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/uvicorn/config.py", line 471, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/uvicorn/importer.py", line 21, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/pasmen/tmp/x-annotated-query-router/main.py", line 5, in <module>
    app.include_router(router)
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/fastapi/applications.py", line 427, in include_router
    self.router.include_router(
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/fastapi/routing.py", line 782, in include_router
    self.add_api_route(
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/fastapi/routing.py", line 600, in add_api_route
    route = route_class(
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/fastapi/routing.py", line 446, in __init__
    self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 303, in get_dependant
    type_annotation, depends, param_field = analyze_param(
  File "/home/pasmen/tmp/x-annotated-query-router/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 387, in analyze_param
    assert field_info.default is Undefined or field_info.default is Required, (
AssertionError: `Query` default value cannot be set in `Annotated` for 'n'. Set the default value with `=` instead.
```

### Operating System

Linux

### Operating System Details

`lsb_release -a`:

```
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.2 LTS
Release:	22.04
Codename:	jammy
```

### FastAPI Version

0.95.0

### Python Version

Python 3.10.6

### Additional Context

This should work according to the [documentation about default values](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#default-values). Also, it works when not using `APIRouter` but having the path operation directly on `app`.</div>
