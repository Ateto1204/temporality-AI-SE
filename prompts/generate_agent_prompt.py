#!/usr/bin/env python3

from pathlib import Path
import argparse
import sys

CONDITION_TEMPLATES = {
    "neither": """# Agent Task

Repository:
{repo}

Base release:
{base_release}

Issue:
{issue}

Temporal context:
No temporal note is provided for this run.

Instructions:
1. Resolve the issue on the checked-out base release.
2. Use only the current codebase and the issue description.
3. Do not assume future APIs, dependencies, files, or designs.
4. Keep the patch minimal and maintainable.
5. Run relevant tests if possible.
6. Summarize your changes and tests run.
""",
    "past": """# Agent Task

Repository:
{repo}

Base release:
{base_release}

Issue:
{issue}

Past Note:
{past_note}

Instructions:
1. Use the Past Note only as historical context already valid before the base release.
2. Do not treat it as a direct solution guide.
3. Verify all implementation choices against the current codebase.
4. Do not assume future APIs, dependencies, files, or designs.
5. Keep the patch minimal and maintainable.
6. Run relevant tests if possible.
7. Summarize your changes and tests run.
""",
    "future": """# Agent Task

Repository:
{repo}

Base release:
{base_release}

Issue:
{issue}

Future Note:
{future_note}

Instructions:
1. Use the Future Note only as high-level later-evolution context.
2. Do not assume future APIs, dependencies, files, configuration formats, or designs exist in the base release.
3. Do not copy future implementation strategies.
4. Verify every implementation choice against the current codebase.
5. Keep the patch minimal and maintainable.
6. Run relevant tests if possible.
7. Summarize your changes and tests run.
""",
    "both": """# Agent Task

Repository:
{repo}

Base release:
{base_release}

Issue:
{issue}

Past Note:
{past_note}

Future Note:
{future_note}

Instructions:
1. Use the Past Note as historical context already valid before the base release.
2. Use the Future Note only as high-level later-evolution context.
3. If the notes suggest different directions, prioritize what is valid in the checked-out base release.
4. Do not assume future APIs, dependencies, files, configuration formats, or designs exist in the base release.
5. Verify every implementation choice against the current codebase.
6. Keep the patch minimal and maintainable.
7. Run relevant tests if possible.
8. Summarize your changes and tests run.
"""
}


def read_required(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError(f"Required file is empty: {path}")
    return text


def read_optional(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8").strip()
    return ""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--base-release", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument(
        "--condition",
        required=True,
        choices=["neither", "past", "future", "both"],
    )
    args = parser.parse_args()

    root = Path("dataset") / args.repo

    issue_path = root / "issues" / args.issue_id / "issue_for_agent.md"
    past_path = root / "notes" / args.issue_id / "past.md"
    future_path = root / "notes" / args.issue_id / "future.md"

    issue = read_required(issue_path)

    past_note = ""
    future_note = ""

    if args.condition in ["past", "both"]:
        past_note = read_required(past_path)

    if args.condition in ["future", "both"]:
        future_note = read_required(future_path)

    template = CONDITION_TEMPLATES[args.condition]
    prompt = template.format(
        repo=args.repo,
        base_release=args.base_release,
        issue=issue,
        past_note=past_note,
        future_note=future_note,
    )

    out_dir = Path("runs") / args.repo / f"issue-{args.issue_id}" / args.condition
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / "agent_prompt.md"
    out_path.write_text(prompt, encoding="utf-8")

    print(f"Generated: {out_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)