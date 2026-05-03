# Excluded Target-Related Artifacts

## Repository

pytest

## Target Issue

#10447

## Excluded References

### Upstream Distutils Issue Reference

- Original reference: upstream distutils issue linked from the original pytest issue.
- Reason: The upstream thread may contain detailed reproduction information, maintainer diagnosis, or implementation-level discussion. It is preserved in `raw_issue_thread.md` but excluded from the agent-facing issue prompt.

### Full Issue Comments

- Reason: Comments may contain maintainer analysis, root-cause discussion, workaround suggestions, or references to fixing commits or pull requests.
- Handling: The pilot agent-facing issue is derived only from the original issue body and high-level observed behavior.

## Excluded Implementation-Level Material

- Specific fixing pull requests, commits, regression test names, or implementation-level analysis should be excluded if found during later artifact collection.
- Internal pytest file names, function names, or direct repair strategies should not be included in `issue_for_agent.md`.

## Included Agent-Facing Information

The following information is retained in `issue_for_agent.md` because it is necessary to understand the task:

- The issue appeared after upgrading to pytest 7.2.
- The affected behavior involves unittest-style test classes.
- The test class is a subclass of another class.
- Both parent and subclass are marked with `usefixtures`.
- The subclass fixture relies on fixture behavior associated with the parent class.
- The expected behavior is compatibility with pre-7.2 fixture behavior.
