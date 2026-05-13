#!/usr/bin/env python3

from pathlib import Path
import argparse
import sys

CONDITIONS = ["neither", "past", "future", "both"]


def read_required(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError(f"Required file is empty: {path}")
    return text


def read_template(condition: str) -> str:
    template_path = Path("prompts") / f"{condition}.md"
    return read_required(template_path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--base-release", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument(
        "--condition",
        required=True,
        choices=CONDITIONS,
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

    template = read_template(args.condition)
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