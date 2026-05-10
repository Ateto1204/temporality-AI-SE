import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path

metrics = ["EA", "BC", "RS", "CP"]
repos = ["pytest", "fastapi", "javalin"]
conditions = ["neither", "past", "future", "both"]

ordered_items = [
    (repo, condition)
    for condition in conditions
    for repo in repos
]

repo_issue_dirs = {
    "pytest": "issue-10447",
    "fastapi": "issue-9387",
    "javalin": "issue-2239",
}

repo_root = Path(__file__).resolve().parents[1]
runs_dir = repo_root / "runs"

columns = ["repo", "condition"] + metrics

def score_path(repo, condition):
    return runs_dir / repo / repo_issue_dirs[repo] / condition / "scores.csv"

def load_score_data():
    rows = []
    required_columns = {"scorer", *metrics}

    for repo, condition in ordered_items:
        path = score_path(repo, condition)
        if not path.exists():
            raise FileNotFoundError(f"Missing score file: {path}")

        score_df = pd.read_csv(path)
        missing_columns = required_columns - set(score_df.columns)
        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            raise ValueError(f"{path} is missing required columns: {missing}")

        for _, score_row in score_df.iterrows():
            rows.append({
                "scorer": int(score_row["scorer"]),
                "repo": repo,
                "condition": condition,
                **{metric: int(score_row[metric]) for metric in metrics},
            })

    all_scores = pd.DataFrame(rows)
    scorer_ids = sorted(all_scores["scorer"].unique())
    return [
        all_scores[all_scores["scorer"] == scorer_id][columns].reset_index(drop=True)
        for scorer_id in scorer_ids
    ]

dfs = load_score_data()

def majority_vote(values):
    counts = Counter(values)
    value, count = counts.most_common(1)[0]
    if count >= 2:
        return value, "majority"
    return int(np.median(values)), "no-majority-median"

voted_rows = []
cell_details = []
for repo, condition in ordered_items:
    row = {"repo": repo, "condition": condition}
    for metric in metrics:
        values = [
            int(df[(df["repo"] == repo) & (df["condition"] == condition)][metric].iloc[0])
            for df in dfs
        ]
        voted, rule = majority_vote(values)
        row[metric] = voted
        cell_details.append({
            "repo": repo,
            "condition": condition,
            "metric": metric,
            "scores": "/".join(map(str, values)),
            "voted_score": voted,
            "rule": rule,
        })
    voted_rows.append(row)

voted_df = pd.DataFrame(voted_rows)
details_df = pd.DataFrame(cell_details)

scores = np.array([[row[metric] for row in voted_rows] for metric in metrics])
column_labels = [f"{repo.capitalize()}\n{condition.capitalize()}" for repo, condition in ordered_items]

fig, ax = plt.subplots(figsize=(12, 3.2), dpi=220)
im = ax.imshow(scores, aspect="auto", vmin=0, vmax=2)

ax.set_xticks(np.arange(len(column_labels)))
ax.set_yticks(np.arange(len(metrics)))
ax.set_xticklabels(column_labels, rotation=45, ha="right", fontsize=8)
ax.set_yticklabels(metrics, fontsize=10)

for i in range(scores.shape[0]):
    for j in range(scores.shape[1]):
        ax.text(j, i, str(scores[i, j]), ha="center", va="center", fontsize=9)

ax.set_xlabel("Repository and Temporal-Context Condition", fontsize=9)
ax.set_ylabel("Evaluation Dimension", fontsize=9)

ax.set_xticks(np.arange(-.5, len(column_labels), 1), minor=True)
ax.set_yticks(np.arange(-.5, len(metrics), 1), minor=True)
ax.grid(which="minor", linewidth=0.5)
ax.tick_params(which="minor", bottom=False, left=False)

for x in [2.5, 5.5, 8.5]:
    ax.axvline(x=x, linewidth=1.2)

cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.02)
cbar.set_label("Score (0–2)", fontsize=9)
cbar.set_ticks([0, 1, 2])

fig.tight_layout()
fig.savefig("rubric_score_heatmap.svg", bbox_inches="tight")
plt.show()
