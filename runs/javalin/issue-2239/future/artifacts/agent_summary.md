**Files Changed**

- [Cookie.kt](/Users/ateto/dev/temporality-AI-SE/repos/javalin/javalin/src/main/java/io/javalin/http/Cookie.kt:47)

**Summary**
Replaced `cookies.removeFirst()` with `cookies.removeAt(0)` in cookie header rewriting. This preserves the existing behavior while avoiding a call that can compile to Java 21’s `java.util.List.removeFirst()`, which crashes on Java 17.

**Tests**

- Added/modified tests: none. Existing `TestCookie` already covers setting cookies through `Context.cookie(...)`.
- Ran `sh ./mvnw -pl javalin -Dtest=TestCookie test -o`
  - Result: passed, 13 tests run.
- Ran `git diff --check`
  - Result: passed.
- Also verified compiled bytecode now calls `java/util/List.remove:(I)` rather than `removeFirst`.

**Remaining Uncertainty**
Focused cookie tests passed on local JDK 17. I did not run the full test suite.
