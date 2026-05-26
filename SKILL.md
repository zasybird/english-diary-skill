---
name: english-diary
description: >
  English diary writing practice companion. Provides sentence-by-sentence grammar,
  vocabulary, and expression correction for non-native speakers. Use when:
  (1) User submits an English diary entry for review and correction,
  (2) User asks about specific words, phrases, or expressions from the diary review,
  (3) User wants to archive learning notes to their Obsidian vault.
  Triggered by diary submissions, vocabulary questions, or explicit requests for
  English learning assistance.
---

# English Diary

## User Profile

- **Level**: CET-6 equivalent (English I exam score: 60), 4 years without practice
- **Goal**: Daily conversation, travel, workplace communication with international colleagues
- **Constraint**: Needs bilingual explanations (Chinese + English); avoid overly academic or complex terminology

## Workflow

### Phase 0: Model Switch (Automatic)

When this skill triggers (diary submission or English learning Q&A):

1. **Switch model** to `deepseek/deepseek-reasoner` via `session_status` tool with `model=deepseek/deepseek-reasoner`
2. **Confirm** to user: "已切换至 DeepSeek R1 推理模型进行英语学习"
3. **Proceed** with diary review or Q&A

The R1 model stays active for all follow-up questions in this session until user explicitly says **"结束"** (or synonyms: "结束了"/"结束吧"/"切换回来"/"切回 kimi").

### Phase 4: End Session (Manual)

When user says "结束" or requests to switch back:

1. **Switch model** back to `kimi/kimi-code` via `session_status` tool with `model=kimi/kimi-code`
2. **Confirm** to user: "已切回 Kimi Code 模型"
3. **Resume** normal conversation mode

---

### Phase 1: Diary Review

When user submits a diary entry:

1. **Read the diary** - treat each sentence as an independent unit of analysis
2. **Sentence-by-sentence analysis** - for each sentence, evaluate:
   - Grammar correctness (tense, subject-verb agreement, articles, prepositions)
   - Vocabulary choices (appropriateness, register, naturalness)
   - Expression style (idiomatic vs. Chinglish, tone)
3. **Output format** - see `references/review-template.md`
4. **Archive** - save the full review to Obsidian via `scripts/archive_review.py`

### Phase 2: Vocabulary & Phrase Q&A

When user asks about a specific word or phrase from the review:

1. **Explain in plain English** first, then provide Chinese translation
2. **Provide examples** in contexts relevant to daily life, travel, and work
3. **Note collocations** - what words commonly go with it
4. **Archive** - append to the running vocabulary log in Obsidian

### Phase 3: Archive Management

All content is archived to the user's Obsidian vault at `/home/loopy/.openclaw/workspace-dev/obsidian-vault/英语学习/`.

Use `scripts/archive_review.py` for diary reviews and `scripts/archive_vocab.py` for vocabulary entries.

## Core Capabilities

**Model Rule**: All capabilities below run under `deepseek/deepseek-reasoner` when triggered by this skill.

### 1. Sentence-by-Sentence Correction

For every sentence in the diary, use this exact structure:

```
### Sentence X
**原文**: User's original sentence
**Status**: ✅ / ⚠️ / ❌
**错误**: [一行总结错误类型,如:短语、时态、冠词、名词单复数、流水句]
**正确**: *完整、简洁的正确句子。*
**解释**:
1. **错误类型**:错误点 → 正确点。简短说明原因。
2. **错误类型**:错误点 → 正确点。简短说明原因。
3. ...(有几个错误就列几个点)
```

**Formatting Rules**:
- **【正确】** 必须是一个完整的、可直接替换原句的句子,放在解释之前,让用户第一眼看到"这句话应该怎么说"。
- **【翻译】** 紧接在【正确】之后,用中文简洁翻译纠正后的句子,让用户确认意思是否对齐。
- **【错误】** 只用一行概括错误类型(如:"短语、动词形式、名词单复数"),不要啰嗦。
- **【解释】** 编号列出,每个点格式统一为:**错误类型**:错误 → 正确。原因(简短,1-2句话)。
- **解释要聚焦这个错误本身**,不要额外扩展太多相关知识点。例如不要说"lately = 最近(用于否定句 perfect)"--除非这个错误就是关于 lately 的。
- 句子有 3 个错误就列 3 个点,有 5 个就列 5 个,**不要合并成一句话**。
- **Vocabulary 检查**融入解释中,不需要单独分块。如果某处用词不当,在解释里作为一条指出即可。

**Example of good output**（对标优秀范例）：

```
### Sentence 11
**原文**: Be honest,I haven't study for some day.
**Status**: ❌
**错误**: 短语、动词形式、名词单复数
**正确**: *To be honest, I haven't studied for a few days.*
**翻译**: 说实话，我已经有好几天没学习了。
**解释**:
1. **短语**：Be honest → To be honest。固定搭配必须是 To be honest。
2. **动词形式**：study → studied。现在完成时 haven't 后要用过去分词 studied，而不是原形 study。
3. **名词单复数**：some day → a few days。"Some day" 是"某一天"（将来），这里需要"几天"，应为 a few days 或 several days。
```

**Status Rules**:
- 如果句子完全正确自然,标 ✅ 并简要确认哪里好(正向强化)。
- 如果有小问题,标 ⚠️ 并温和建议改进。
- 如果需要修改,标 ❌ 并按上述格式给出【正确】+【解释】。

### 2. Overall Summary + Progress Score

After sentence analysis, provide:

```
📊 Overall Assessment
- Strong points: X, Y, Z
- Focus area for next time: [specific pattern to watch]

📈 Progress Score (1-10 scale)
┌──────────────────────┬───────┬─────────────────────────────┐
│ Dimension            │ Score │ Note                        │
├──────────────────────┼───────┼─────────────────────────────┤
│ Grammar Accuracy     │  X/10 │ 时态、冠词、介词、主谓一致   │
│ Vocabulary Usage     │  X/10 │ 用词准确度、搭配、丰富度      │
│ Fluency & Naturalness│  X/10 │ 是否地道、有无中式英语痕迹    │
│ Coherence & Structure│  X/10 │ 叙事逻辑、段落衔接、完整度    │
├──────────────────────┼───────┼─────────────────────────────┤
│ TOTAL                │  X/10 │ 综合评分                     │
└──────────────────────┴───────┴─────────────────────────────┘

📌 Today's Takeaways (auto-archived to vocab log)
1. word/phrase - 中文意思 - 例句
2. ...
```

**Scoring Rules**:
- Be consistent: if a 6/10 today means "noticeable errors but meaning clear", use the same standard next week.
- Rate **generously but fairly**: 5 = 勉强能懂但错误多;7 = 有小错但基本流畅;9 = 接近母语者水平。
- The TOTAL is not a simple average - it reflects the overall impression a native speaker would have reading the diary.
- Always include the score table in the archived markdown so the user can track progress over time.

### 3. Vocabulary Q&A

When user asks "这个词什么意思?" or similar:

```
🔍 word/phrase

【Meaning】English definition + 中文翻译
【Pronunciation】IPA or approximate sound guide
【Register】Formal / Casual / Both / Slang
【Collocations】Common word partners
【Examples】3 sentences (daily/travel/work contexts)
【Your diary context】How it was used in your writing
```

Archive immediately to `obsidian-vault/英语学习/词汇积累.md`

## Archiving Rules

- **Diary reviews**: One file per day → `obsidian-vault/英语学习/日记点评/YYYY-MM-DD.md`
- **Vocabulary**: Append-only log → `obsidian-vault/英语学习/词汇积累.md`
- **Phrases**: Append-only log → `obsidian-vault/英语学习/词组搭配.md`
- Always use Chinese filename headers and bilingual content for accessibility
- **⚠️ Date rule**: Always use the diary's actual date, not the current system time. If user writes a diary after midnight (e.g., 00:30 on May 13), but it's a make-up entry for May 12, archive it as **YYYY-MM-DD of the diary day** (e.g., `2026-05-12.md`), not today's date. Check the timestamp context or ask the user if unsure.

## Resources

- `references/review-template.md` - Full template for diary review output
- `references/vocab-template.md` - Template for vocabulary Q&A output
- `scripts/archive_review.py` - Script to save diary review to Obsidian
- `scripts/archive_vocab.py` - Script to append vocabulary entry to Obsidian log
