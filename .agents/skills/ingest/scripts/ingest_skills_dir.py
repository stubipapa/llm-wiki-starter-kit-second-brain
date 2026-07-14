import os
import shutil

sources_dir = 'wiki/sources'
entities_dir = 'wiki/entities'
concepts_dir = 'wiki/concepts'
raw_dir = 'raw/04-clipper'
archive_dir = 'raw/09-archive'
index_file = 'wiki/index.md'
log_file = 'wiki/log.md'

os.makedirs(sources_dir, exist_ok=True)
os.makedirs(entities_dir, exist_ok=True)
os.makedirs(concepts_dir, exist_ok=True)
os.makedirs(archive_dir, exist_ok=True)

source_name = "摘要-awesome-agent-skills-社群精選目錄"
source_content = """---
title: "摘要-awesome-agent-skills-社群精選目錄"
type: source
tags: [來源, 目錄, AI助手, 擴充技能]
sources: [raw/09-archive/這是一個社群精選的 AI 代理技能（Agent Skills）目錄.md]
last_updated: 2026-07-13
---

## 核心摘要
本文介紹了由 Hailey Cheng 維護的開源專案 `awesome-agent-skills`。這是一份由社群精選的 Agent Skills 清單，專注於收錄實際工程團隊使用的真實技能，而非大量生成的劣質內容。
文章詳細說明了 Agent Skills 的載入機制（瀏覽、載入、使用），並介紹了如 SkillsMP 市場、skills.sh 等尋找技能的工具。同時整理了包含 Anthropic, OpenAI, Google Gemini 等官方釋出的高品質技能清單（涵蓋文檔處理、前端設計、雲端部署等）。
最後，文章點出了 2026 年 AI Agent 生態的三大發展趨勢：自主執行 (Autonomous Execution)、多代理編排 (Multi-agent Orchestration) 與 Agentic IDE（如 Cursor、Windsurf、Claude Code 等原生支援終端與 MCP 存取的環境）。

## 關聯連接
- [[Hailey Cheng]] — 關聯實體
- [[SkillsMP]] — 關聯實體
- [[Claude Code]] — 關聯實體
- [[Codex CLI]] — 關聯實體
- [[skill-architecture]] — 關聯概念
- [[agentic-ide]] — 關聯概念
- [[Model Context Protocol (MCP)]] — 關聯實體
"""

entity1 = "Hailey Cheng"
entity1_content = """---
title: "Hailey Cheng"
type: entity
tags: [人物, 開源開發者]
sources: [wiki/sources/摘要-awesome-agent-skills-社群精選目錄.md]
last_updated: 2026-07-13
---
## 定義
開源專案 `awesome-agent-skills` 的維護者與策展人。

## 關鍵資訊
- 整理並維護了由社群精選的真實世界 Agent 技能目錄，幫助 AI 助理如 Claude、Copilot 等按需學習新能力。
- 專注於收集實際工程團隊建立並使用的技能，而非大量生成的內容。

## 關聯連接
- [[摘要-awesome-agent-skills-社群精選目錄]] — 來源
- [[skill-architecture]] — 相關知識節點
"""

entity2 = "SkillsMP"
entity2_content = """---
title: "SkillsMP"
type: entity
tags: [平台, 市場, Agent]
sources: [wiki/sources/摘要-awesome-agent-skills-社群精選目錄.md]
last_updated: 2026-07-13
---
## 定義
一個自動索引 GitHub 上所有 Skill 專案的 Agent Skills 市場平台。

## 關鍵資訊
- 提供按類別、更新時間、星數和其他標籤進行組織的技能目錄。
- 是發現和評估實用 Agent 技能最簡單的平台之一。

## 關聯連接
- [[摘要-awesome-agent-skills-社群精選目錄]] — 來源
- [[skill-architecture]] — 相關知識節點
"""

concept1 = "agentic-ide"
concept1_content = """---
title: "agentic-ide"
type: concept
tags: [開發環境, 趨勢, IDE]
sources: [wiki/sources/摘要-awesome-agent-skills-社群精選目錄.md]
last_updated: 2026-07-13
---
## 定義
2026 年 AI 發展的重要趨勢之一。代表整合了深度 AI 代理能力的整合開發環境。

## 關鍵資訊
- 包含 Cursor, Windsurf, Claude Code, GitHub Copilot 等工具。
- AI 代理可在這類環境中原生執行終端命令、監控遙測並通過 MCP (Model Context Protocol) 直接存取文件系統，具備高度自主性與多代理編排能力。

## 關聯連接
- [[摘要-awesome-agent-skills-社群精選目錄]] — 來源
- [[Model Context Protocol (MCP)]] — 相關實體
- [[Claude Code]] — 相關實體
"""

with open(os.path.join(sources_dir, source_name + '.md'), 'w', encoding='utf-8') as f: f.write(source_content)
with open(os.path.join(entities_dir, entity1 + '.md'), 'w', encoding='utf-8') as f: f.write(entity1_content)
with open(os.path.join(entities_dir, entity2 + '.md'), 'w', encoding='utf-8') as f: f.write(entity2_content)
with open(os.path.join(concepts_dir, concept1 + '.md'), 'w', encoding='utf-8') as f: f.write(concept1_content)

# Update index.md
with open(index_file, 'r', encoding='utf-8') as f:
    index_lines = f.readlines()

new_index_lines = []
for line in index_lines:
    new_index_lines.append(line)
    if line.strip() == "## Sources":
        new_index_lines.append("- `摘要-awesome-agent-skills-社群精選目錄` — 社群精選 Agent Skills 的整理與發展趨勢\n")
    if line.strip() == "## Entities":
        new_index_lines.append("- `Hailey Cheng` — awesome-agent-skills 的維護者\n")
        new_index_lines.append("- `SkillsMP` — Agent Skills 市場平台\n")
    if line.strip() == "## Concepts":
        new_index_lines.append("- `agentic-ide` — 深度整合 AI 代理能力的整合開發環境\n")

with open(index_file, 'w', encoding='utf-8') as f:
    f.writelines(new_index_lines)

# Log to log.md
with open(log_file, 'a', encoding='utf-8') as f:
    f.write("## [2026-07-13] ingest | 處理了 raw/04-clipper/ 下 awesome-agent-skills 目錄文章\n")
    f.write("- **新增 Sources**: `摘要-awesome-agent-skills-社群精選目錄`\n")
    f.write("- **新增 Entities**: `Hailey Cheng`, `SkillsMP`\n")
    f.write("- **新增 Concepts**: `agentic-ide`\n")
    f.write("- **修改**: `index.md`\n")

# Move file to archive
for file in os.listdir(raw_dir):
    if file.endswith('.md'):
        shutil.move(os.path.join(raw_dir, file), os.path.join(archive_dir, file))
