# English Diary Skill

> An [OpenClaw](https://github.com/openclaw/openclaw) skill for non-native English speakers to practice writing through daily diary correction, vocabulary tracking, and progress scoring.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## What It Does

This skill turns your AI assistant into a personal English writing coach. Submit your daily diary, and it will:

- **Correct every sentence** — grammar, vocabulary, expressions, one sentence at a time
- **Explain why** — each error gets a clear, numbered explanation in both Chinese and English
- **Score your progress** — a consistent 4-dimension scoring rubric so you can track improvement over time
- **Archive everything** — reviews and vocabulary are automatically saved to your Obsidian vault

It's designed for a CET-6 level learner who hasn't practiced in a while and wants to regain fluency for daily conversation, travel, and workplace communication.

---

## How It Works

```
You write a diary  →  DeepSeek R1 analyzes it  →  Sentence-by-sentence review  →  Archived to Obsidian
```

1. **Model switch** — The skill automatically switches to `deepseek/deepseek-reasoner` (DeepSeek R1) for reasoning-heavy grammar analysis
2. **Sentence-by-sentence review** — Each sentence gets: original text, error summary, corrected version, Chinese translation, and a numbered breakdown of every mistake
3. **Progress scoring** — A 4-dimension table (Grammar, Vocabulary, Fluency, Coherence) with consistent 1–10 scoring
4. **Vocabulary Q&A** — Ask about any word or phrase from the review and get definitions, collocations, examples in daily/travel/work contexts, and memory hooks
5. **Auto-archiving** — Reviews are saved as `日记点评/YYYY-MM-DD.md`, vocabulary entries go to a running `词汇积累.md` log in your Obsidian vault

---

## File Structure

```
english-diary-skill/
├── SKILL.md                  # Skill definition: workflow, rules, scoring rubric
├── archive_review.py         # Save diary reviews to Obsidian
├── archive_vocab.py          # Append vocabulary entries to Obsidian logs
├── review-template.md        # Template for diary review output format
├── vocab-template.md         # Template for vocabulary Q&A output format
└── README.md
```

---

## Setup

### Prerequisites

- [OpenClaw](https://github.com/openclaw/openclaw) installed and configured
- Python 3.8+
- An Obsidian vault (for archiving reviews and vocabulary)

### Installation

1. **Clone the repo into your OpenClaw skills directory:**

   ```bash
   git clone https://github.com/zasybird/english-diary-skill.git ~/.openclaw/skills/english-diary
   ```

2. **Set your Obsidian vault path** (if different from the default):

   ```bash
   export OBSIDIAN_VAULT="/path/to/your/obsidian-vault"
   ```

   Or update the `VAULT_BASE` variable in `archive_review.py` and `archive_vocab.py`.

3. **Ensure the archive scripts are executable:**

   ```bash
   chmod +x archive_review.py archive_vocab.py
   ```

4. **Verify the setup:**

   ```bash
   python3 archive_review.py --date 2026-01-01 --content "Test review"
   ```

   You should see the file appear at `{OBSIDIAN_VAULT}/英语学习/日记点评/2026-01-01.md`.

---

## Usage

### Writing a Diary

Just paste your English diary into the chat. The skill will:

1. Switch to DeepSeek R1 for analysis
2. Return a full sentence-by-sentence review
3. Give you an overall assessment and progress score
4. Archive the review to your Obsidian vault

```
Today I went to the park with my friend. The weather was very good and we saw many beautiful flower. We decide to come back next weekend.
```

### Asking About Vocabulary

After a review, ask about any word or expression:

> "What does 'collocation' mean?"

You'll get a bilingual explanation with examples, common word partners, and a memory hook — all archived to your vocabulary log.

### Ending a Session

Say **"结束"** to switch back to the default model and resume normal conversation.

---

## Scoring Rubric

Reviews use a consistent 4-dimension scoring system:

| Dimension | What It Measures |
|---|---|
| **Grammar Accuracy** (1–10) | Tense, articles, prepositions, subject-verb agreement |
| **Vocabulary Usage** (1–10) | Word choice accuracy, collocations, range |
| **Fluency & Naturalness** (1–10) | How natural it sounds, Chinglish detection |
| **Coherence & Structure** (1–10) | Narrative logic, paragraph flow, completeness |

| Score | Meaning |
|---|---|
| 5 | Barely understandable, many errors |
| 6–7 | Minor errors but meaning is clear |
| 8 | Very few errors, close to natural |
| 9–10 | Near-native fluency |

---

## Customization

This skill is tuned for a **CET-6 level learner who hasn't practiced in 4 years**. To adapt it for yourself:

1. Edit the **User Profile** section in `SKILL.md` — update your English level, goals, and constraints
2. Adjust the **scoring standards** in the "Scoring Rules" section if you want stricter or more lenient grading
3. Change `VAULT_BASE` in both Python scripts to match your own Obsidian vault path

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

## Credits

Built with [OpenClaw](https://github.com/openclaw/openclaw) and [DeepSeek R1](https://deepseek.com).

