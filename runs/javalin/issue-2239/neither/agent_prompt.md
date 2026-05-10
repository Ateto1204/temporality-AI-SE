# Agent Task

Repository:
javalin

Base release:
javalin-parent-5.6.4

Issue:
# Target Issue

## Repository

Javalin

## Base Release

javalin-parent-5.6.4

## Title

Javalin 5.6.4 crashes on Java 17 when setting a cookie

## Summary

After upgrading from Javalin 5.6.3 to Javalin 5.6.4, an application that previously worked on JDK 17 crashes when setting a cookie through the request context.

The same application behavior worked with Javalin 5.6.3 on JDK 17, but fails after the minor upgrade to Javalin 5.6.4.

## Observed Context

The failure occurs when application code calls the context cookie API to create or set a cookie during request handling.

The failure is observed on JDK 17.

## Actual Behavior

The application crashes while servicing an HTTP request.

The observed exception is:

    java.lang.NoSuchMethodError: 'java.lang.Object java.util.List.removeFirst()'

The error appears when setting a cookie through Javalin's context cookie behavior.

## Expected Behavior

Setting a cookie should work on JDK 17.

A minor upgrade from Javalin 5.6.3 to 5.6.4 should not unexpectedly introduce a runtime requirement that breaks cookie behavior on JDK 17.

## Environment

- Javalin version: 5.6.4
- Previously working version: 5.6.3
- Java runtime: JDK 17
- Area: HTTP context cookie handling

## Evaluation Hint

A valid patch should allow cookie setting to work on JDK 17 in Javalin 5.6.4 without introducing a broader runtime-version requirement or unrelated changes to HTTP request handling.

Temporal context:
No temporal note is provided for this run.

Instructions:
1. Resolve the issue on the checked-out base release.
2. Use only the current codebase and the issue description.
3. Do not assume future APIs, dependencies, files, or designs.
4. Keep the patch minimal and maintainable.
5. Run relevant tests if possible.
6. Summarize your changes and tests run.
