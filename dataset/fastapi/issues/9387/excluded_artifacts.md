# Excluded Target-Related Artifacts

## Repository

FastAPI

## Target Issue

#9387

## Excluded References

### Fixing PR Reference

- Original text: "There's a fix in https://github.com/tiangolo/fastapi/pull/9315."
- Reason: This directly identifies the fixing pull request and may reveal the target solution.

### Discussion Reference

- Original text: "Discussed in https://github.com/tiangolo/fastapi/discussions/9279"
- Reason: The linked discussion may contain root-cause analysis or implementation suggestions. It is preserved in raw evidence but excluded from the agent-facing issue prompt.

## Excluded Implementation-Level Material

- Full stack trace internal paths and line numbers are preserved in `raw_issue_thread.md`.
- The agent-facing issue prompt only keeps the final assertion error message.
- Reason: The full trace contains implementation-level file and function names that may over-direct the agent toward the fixing location.

## Included Agent-Facing Information

The agent-facing issue prompt keeps the minimal reproduction code, the final assertion error message, expected behavior, affected FastAPI version, Python version, and operating system because these are necessary to reproduce and understand the issue.
