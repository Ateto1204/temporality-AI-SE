**Files Changed**

- [Cookie.kt](/Users/ateto/dev/temporality-AI-SE/repos/javalin/javalin/src/main/java/io/javalin/http/Cookie.kt:47)
- [TestCookie.kt](/Users/ateto/dev/temporality-AI-SE/repos/javalin/javalin/src/test/java/io/javalin/TestCookie.kt:137)

**Summary**

- Replaced `cookies.removeFirst()` with `isNotEmpty()` plus `removeAt(0)`, avoiding bytecode that can bind to Java 21 `List.removeFirst()` and crash on Java 17.
- Preserved existing cookie header rewrite behavior.

**Tests Added/Modified**

- Added regression test asserting compiled `CookieKt.class` does not contain `removeFirst`.

**Tests Run**

- `sh ./mvnw -pl javalin -Dtest=TestCookie test`
- Result: passed, `14` tests, `0` failures/errors.
- Note: `./mvnw` itself is not executable in this checkout, so I invoked it via `sh`.

**Remaining Uncertainty**

- Full repo test suite was not run; targeted cookie tests passed on local JDK 17.
