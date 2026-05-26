#!/usr/bin/env python3
"""
Archive an English diary review to the user's Obsidian vault.

Usage:
    python3 archive_review.py --date YYYY-MM-DD --content "markdown content"

The review is saved to:
    /home/loopy/.openclaw/workspace-dev/obsidian-vault/英语学习/日记点评/YYYY-MM-DD.md
"""

import argparse
import os
import sys
from datetime import datetime

VAULT_BASE = os.environ.get("OBSIDIAN_VAULT", "/path/to/your/obsidian-vault")
REVIEW_DIR = os.path.join(VAULT_BASE, "英语学习", "日记点评")


def ensure_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def archive_review(date_str: str, content: str) -> str:
    ensure_dir(REVIEW_DIR)
    filepath = os.path.join(REVIEW_DIR, f"{date_str}.md")

    header = f"# 📝 日记点评 — {date_str}\n\n"
    full_content = header + content

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)

    return filepath


def main():
    parser = argparse.ArgumentParser(description="Archive diary review to Obsidian")
    parser.add_argument("--date", required=True, help="Date string YYYY-MM-DD")
    parser.add_argument("--content", required=True, help="Markdown content of the review")
    args = parser.parse_args()

    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print("ERROR: Date must be in YYYY-MM-DD format", file=sys.stderr)
        sys.exit(1)

    path = archive_review(args.date, args.content)
    print(f"OK: {path}")


if __name__ == "__main__":
    main()
