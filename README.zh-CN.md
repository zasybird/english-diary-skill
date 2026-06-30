# English Diary Skill

> 一个 [OpenClaw](https://github.com/openclaw/openclaw) Skill，帮助非英语母语者通过每日日记批改、词汇追踪和进步评分来练习英文写作。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 项目简介

这个 Skill 能把你的 AI 助手变成私人英语写作教练。提交你的每日日记，它会：

- **逐句批改** — 语法、词汇、表达方式，一句一句来
- **解释原因** — 每个错误附带中英双语编号详解
- **量化评分** — 四个维度的统一评分标准，方便追踪长期进步
- **自动归档** — 批改记录和词汇笔记自动存入你的 Obsidian 知识库

目标用户是需要重拾英语的 CET-6 水平学习者，场景覆盖日常对话、旅行游历和职场沟通。

---

## 工作流程

```
你提交日记  →  DeepSeek R1 逐句分析  →  逐句反馈批改结果  →  自动归档到 Obsidian
```

1. **模型切换** — 自动切换到 `deepseek/deepseek-reasoner`（DeepSeek R1），利用其推理能力进行语法分析
2. **逐句批改** — 每句话输出：原文、错误摘要、修正版、中文翻译、逐条错误编号详解
3. **进步评分** — 四维评分表（语法准确性、词汇使用、流利自然度、连贯与结构），统一 1–10 分制
4. **词汇问答** — 对批改中出现的任意单词或短语提问，获取释义、常见搭配、生活/旅行/工作场景例句和记忆技巧
5. **自动归档** — 批改记录存为 `日记点评/YYYY-MM-DD.md`，词汇条目追加到 `词汇积累.md` 日志中

---

## 文件结构

```
english-diary-skill/
├── SKILL.md                  # Skill 定义：工作流、规则、评分标准
├── archive_review.py         # 将批改结果保存到 Obsidian
├── archive_vocab.py          # 将词汇条目追加到 Obsidian 日志
├── review-template.md        # 日记批改输出格式模板
├── vocab-template.md         # 词汇问答输出格式模板
├── README.md                 # 英文说明
├── README.zh-CN.md           # 中文说明（本文件）
└── LICENSE                   # MIT 开源协议
```

---

## 安装配置

### 前置条件

- 已安装并配置好 [OpenClaw](https://github.com/openclaw/openclaw)
- Python 3.8+
- 一个 Obsidian 知识库（用于存放批改记录和词汇笔记）

### 安装步骤

1. **克隆仓库到 OpenClaw 的 skills 目录：**

   ```bash
   git clone https://github.com/zasybird/english-diary-skill.git ~/.openclaw/skills/english-diary
   ```

2. **设置 Obsidian 知识库路径**（如果默认路径不适合你）：

   ```bash
   export OBSIDIAN_VAULT="/path/to/your/obsidian-vault"
   ```

   或者直接修改 `archive_review.py` 和 `archive_vocab.py` 中的 `VAULT_BASE` 变量。

3. **确保归档脚本可执行：**

   ```bash
   chmod +x archive_review.py archive_vocab.py
   ```

4. **验证安装是否成功：**

   ```bash
   python3 archive_review.py --date 2026-01-01 --content "测试归档"
   ```

   如果一切正常，你会在 `{OBSIDIAN_VAULT}/英语学习/日记点评/2026-01-01.md` 看到刚创建的文件。

---

## 使用方法

### 写日记

直接把英文日记贴到聊天窗口。Skill 会自动：

1. 切换到 DeepSeek R1 进行分析
2. 返回逐句批改结果
3. 给出总体评价和进步评分
4. 将批改记录归档到你的 Obsidian 知识库

```
Today I went to the park with my friend. The weather was very good and we saw many beautiful flower. We decide to come back next weekend.
```

### 提问词汇

批改结束后，对任意单词或表达方式提问：

> "collocation 是什么意思？"

你会得到双语解释、常见搭配、场景例句和记忆技巧——全部自动归档到你的词汇积累日志。

### 结束会话

说 **"结束"** 即可切换回默认模型，恢复正常对话。

---

## 评分标准

批改使用统一的四维评分体系：

| 维度 | 衡量内容 |
|---|---|
| **语法准确性**（1–10） | 时态、冠词、介词、主谓一致 |
| **词汇使用**（1–10） | 用词准确度、搭配、词汇丰富度 |
| **流利自然度**（1–10） | 表达是否自然地道、中式英语检测 |
| **连贯与结构**（1–10） | 叙事逻辑、段落衔接、内容完整度 |

| 分数 | 含义 |
|---|---|
| 5 | 勉强可懂，错误较多 |
| 6–7 | 有小错但意思清晰 |
| 8 | 极少错误，接近地道 |
| 9–10 | 接近母语水平 |

---

## 个性化配置

本 Skill 默认配置了 **已放下英语 4 年的 CET-6 水平学习者**。如需调整：

1. 编辑 `SKILL.md` 中的 **User Profile** 部分，更新自己的英语水平、学习目标和约束条件
2. 修改「评分规则」章节中的标准，收紧或放宽评分尺度
3. 在两个 Python 脚本中改 `VAULT_BASE` 为你自己的 Obsidian 路径

---

## 开源协议

MIT — 详见 [LICENSE](LICENSE) 文件。

---

## 致谢

基于 [OpenClaw](https://github.com/openclaw/openclaw) 构建，分析引擎由 [DeepSeek R1](https://deepseek.com) 驱动。
