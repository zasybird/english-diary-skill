#!/usr/bin/env python3
"""
Append a vocabulary entry to the user's Obsidian learning log.

Usage:
    python3 archive_vocab.py --type vocab --entry "markdown entry"
    python3 archive_vocab.py --type phrase --entry "markdown entry"

Entries are appended to:
    /home/loopy/.openclaw/workspace-dev/obsidian-vault/英语学习/词汇积累.md  (for vocab)
    /home/loopy/.openclaw/workspace-dev/obsidian-vault/英语学习/词组搭配.md  (for phrase)
"""

import argparse
import os
import sys
from datetime import datetime

VAULT_BASE = os.environ.get("OBSIDIAN_VAULT", "/path/to/your/obsidian-vault")
VOCAB_FILE = os.path.join(VAULT_BASE, "英语学习", "词汇积累.md")
PHRASE_FILE = os.path.join(VAULT_BASE, "英语学习", "词组搭配.md")


def ensure_dir(path: str) -> None:
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)


def ensure_file_header(filepath: str, header: str) -> None:
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(header + "\n\n")


def archive_entry(entry_type: str, content: str) -> str:
    if entry_type == "vocab":
        filepath = VOCAB_FILE
        header = "# 📚 词汇积累 (Vocabulary Log)"
    elif entry_type == "phrase":
        filepath = PHRASE_FILE
        header = "# 🔗 词组搭配 (Phrase & Collocation Log)"
    else:
        raise ValueError(f"Unknown type: {entry_type}. Use 'vocab' or 'phrase'.")

    ensure_dir(filepath)
    ensure_file_header(filepath, header)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n---\n\n**[{timestamp}]**\n\n{content}\n"

    with open(filepath, "a", encoding="utf-8") as f:
        f.write(entry)

    return filepath


def main():
    parser = argparse.ArgumentParser(description="Archive vocab/phrase to Obsidian")
    parser.add_argument("--type", required=True, choices=["vocab", "phrase"], help="Entry type")
    parser.add_argument("--entry", required=True, help="Markdown content of the entry")
    args = parser.parse_args()

    try:
        path = archive_entry(args.type, args.entry)
        print(f"OK: {path}")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
