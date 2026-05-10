**Files Changed**

- [Cookie.kt](/Users/ateto/dev/temporality-AI-SE/repos/javalin/javalin/src/main/java/io/javalin/http/Cookie.kt:47)
- [TestCookie.kt](/Users/ateto/dev/temporality-AI-SE/repos/javalin/javalin/src/test/java/io/javalin/TestCookie.kt:94)

**Summary**
Replaced `cookies.removeFirst()` in cookie header handling with a guarded `cookies.removeAt(0)`. This keeps the same header rewrite behavior while avoiding the Java 21 `List.removeFirst()` runtime dependency that crashes on Java 17.

**Tests Added**
Added a focused regression test for `setJavalinCookie` using a mocked `HttpServletResponse`, verifying cookie setting does not throw and rewrites `Set-Cookie`.

**Tests Run**

- `sh ./mvnw -pl javalin -Dtest=io.javalin.TestCookie test` passed: 14 tests, 0 failures.
- `git diff --check` passed.

The first sandboxed test run could not bind a local ephemeral port; rerunning the same test command with local port binding allowed passed.

**Remaining Uncertainty**
None.
