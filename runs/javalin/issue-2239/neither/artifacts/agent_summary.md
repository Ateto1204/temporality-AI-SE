**Files Changed**

- [Cookie.kt](/Users/ateto/dev/temporality-AI-SE/repos/javalin/javalin/src/main/java/io/javalin/http/Cookie.kt:47)
- [TestCookie.kt](/Users/ateto/dev/temporality-AI-SE/repos/javalin/javalin/src/test/java/io/javalin/TestCookie.kt:90)

**Summary**
Replaced `cookies.removeFirst()` with a guarded `cookies.removeAt(0)` in cookie response handling. This preserves behavior while avoiding linkage to Java 21’s `java.util.List.removeFirst()`, which crashes on Java 17.

**Tests**
Added a regression test asserting the cookie helper bytecode no longer contains `removeFirst`.

Ran:

```bash
env JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home mvn -pl javalin -Dtest=io.javalin.TestCookie test
```

Result: passed, 14 tests run, 0 failures/errors.

Also ran `git diff --check`: passed.

**Remaining Uncertainty**
Full project test suite was not run. The pre-existing untracked `javalin-bom/` directory was left untouched.
