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

Past Note:
# Past Note

## Scope

- Repository: Javalin
- Base release: javalin-parent-5.6.4
- Temporal position: before the base release
- Release window: 5.5.x to 5.6.3

## Evolution Story

Before the base release, Javalin had already been shaped as a lightweight JVM web framework whose user-facing behavior depended not only on source-level APIs, but also on runtime compatibility with commonly deployed Java versions and server components. Common HTTP context operations, such as setting cookies and manipulating response behavior, were part of the framework’s practical stability surface. Within the same major release line, users could reasonably expect minor upgrades to preserve ordinary request-handling behavior unless a breaking change was clearly documented.

## Stable Design Tendencies

- Javalin tends to preserve common HTTP request-handling behavior across minor releases in the same major version line.
- Context-level operations, including cookie handling, are part of the framework’s user-facing compatibility surface.
- Runtime compatibility is important because Javalin applications are deployed on specific JVM versions.
- Build-time assumptions should remain compatible with the runtime expectations of the release line.
- Compatibility concerns are not limited to API signatures; they also include bytecode/runtime behavior and dependency interactions.

## Behavioral Expectations

- Setting cookies through the context API should remain stable across minor releases.
- A minor release should not unexpectedly introduce runtime failures for common request-handling behavior.
- Framework behavior should remain compatible with the Java runtime expectations of the release line.
- Fixes should preserve existing HTTP context semantics and avoid unrelated rewrites of request/response handling.
- Runtime-version assumptions should be handled cautiously in a JVM framework.

## Constraints and Non-goals

- This note does not describe a direct fix for any specific issue.
- This note does not imply that later Java APIs, later dependencies, or later platform assumptions are valid for the base release.
- This note should not be treated as an instruction to rewrite Javalin’s HTTP context API, routing system, or server integration broadly.
- Any patch should remain grounded in the checked-out base release and should avoid unrelated refactoring.

## Risk of Misuse

This note describes historical design context that had already shaped Javalin before the base release. It should be used only as background for understanding compatibility expectations in the 5.x release line, not as a direct solution guide.

Instructions:
1. Use the Past Note only as historical context already valid before the base release.
2. Do not treat it as a direct solution guide.
3. Verify all implementation choices against the current codebase.
4. Do not assume future APIs, dependencies, files, or designs.
5. Keep the patch minimal and maintainable.
6. Run relevant tests if possible.
7. Summarize your changes and tests run.
