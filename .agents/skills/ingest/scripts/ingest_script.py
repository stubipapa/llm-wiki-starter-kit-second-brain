import os

sources_dir = 'wiki/sources'
entities_dir = 'wiki/entities'
raw_dir = 'raw/04-clipper'
archive_dir = 'raw/09-archive'
index_file = 'wiki/index.md'
log_file = 'wiki/log.md'

os.makedirs(sources_dir, exist_ok=True)
os.makedirs(entities_dir, exist_ok=True)
os.makedirs(archive_dir, exist_ok=True)

source1 = "摘要-vercel-agent-skills-擴充包集合"
source1_content = """---
title: "摘要-vercel-agent-skills-擴充包集合"
type: source
tags: [來源, AI助手, 擴充技能]
sources: [raw/09-archive/一套由 Vercel 官方維護、專為 AI 編碼助手（AI coding agents）設計的技能擴充包集合，旨在延伸並增強 AI 助手的開發、優化與部署能力.md]
last_updated: 2026-07-13
---

## 核心摘要
Agent Skills 是一套由 Vercel 官方維護、專為 AI 編碼助手（如 Claude Code 等）設計的開源技能擴充包集合（vercel-labs/agent-skills）。其核心目標是延伸並增強 AI 助手的開發、優化與部署能力。該技能庫包含多樣化的開發與優化模組（如效能優化 `vercel-optimize`、React/Next.js 最佳實踐、網頁設計規範、寫作指南、以及一鍵部署功能 `vercel-deploy-claimable`）。所有技能均採用標準化的架構設計，包含提供給 AI 閱讀的 `SKILL.md` 操作說明書、輔助腳本與參考文檔，使 AI 能夠快速理解並精準執行任務。

## 關聯連接
- [[Vercel Labs]] — 關聯實體
- [[skill-architecture]] — 關聯概念
"""

source2 = "摘要-notebooklm-py-非官方api與工具"
source2_content = """---
title: "摘要-notebooklm-py-非官方api與工具"
type: source
tags: [來源, NotebookLM, API, AI工具]
sources: [raw/09-archive/notebooklm-py。 一個非官方的 Google NotebookLM Python API、命令列工具（CLI）與 AI 代理工具，讓開發者能完整透過程式控制 NotebookLM，甚至使用網頁版 UI 未公開的進階功能.md]
last_updated: 2026-07-13
---

## 核心摘要
`notebooklm-py` 是一個由 teng-lin 開發的非官方 Google NotebookLM Python API、CLI 及 AI 代理工具。它允許開發者透過程式碼完整控制 NotebookLM，並能使用網頁版 UI 未公開的進階功能（如批次下載、測驗/閃卡匯出等多種格式）。
此工具不僅支援建立筆記本與問答，更具備強大的資料導出與自動化能力，能將生成的語音導讀、影片、心智圖等產物儲存至本地。此外，專案內建專為 Claude Code、Codex 設計的 Skill 模組，並支援以 MCP 伺服器的方式進行多元部署，非常適合與 AI 代理協同工作，作為零 Token 消耗的底層記憶體與綜合分析引擎。

## 關聯連接
- [[teng-lin]] — 關聯實體
- [[NotebookLM]] — 關聯實體
- [[Claude Code]] — 關聯實體
- [[Codex CLI]] — 關聯實體
- [[Model Context Protocol (MCP)]] — 關聯實體
- [[skill-architecture]] — 關聯概念
- [[RAG]] — 關聯概念
"""

entity1 = "Vercel Labs"
entity1_content = """---
title: "Vercel Labs"
type: entity
tags: [組織, 開源]
sources: [wiki/sources/摘要-vercel-agent-skills-擴充包集合.md]
last_updated: 2026-07-13
---
## 定義
Vercel 旗下的開源實驗室，負責開發與維護專為 AI 編碼助手設計的技能擴充包集合（Agent Skills）。

## 關鍵資訊
- 提供標準化的技能擴充包（如 `vercel-optimize`, `react-best-practices` 等），增強 AI 代理在效能優化與專案部署上的能力。
- 倡導標準化的技能檔案架構（SKILL.md, scripts/, references/）。

## 關聯連接
- [[摘要-vercel-agent-skills-擴充包集合]] — 來源
- [[skill-architecture]] — 相關知識節點
"""

entity2 = "teng-lin"
entity2_content = """---
title: "teng-lin"
type: entity
tags: [人物, 開源開發者]
sources: [wiki/sources/摘要-notebooklm-py-非官方api與工具.md]
last_updated: 2026-07-13
---
## 定義
開源專案 `notebooklm-py` 的開發者。

## 關鍵資訊
- 開發了非官方的 Google NotebookLM API、CLI 工具及 AI 代理擴充模組。
- 將 NotebookLM 功能與 AI 開發環境（如 Claude Code, Codex, MCP 等）進行深度整合。

## 關聯連接
- [[摘要-notebooklm-py-非官方api與工具]] — 來源
- [[NotebookLM]] — 相關知識節點
"""

with open(os.path.join(sources_dir, source1 + '.md'), 'w', encoding='utf-8') as f: f.write(source1_content)
with open(os.path.join(sources_dir, source2 + '.md'), 'w', encoding='utf-8') as f: f.write(source2_content)
with open(os.path.join(entities_dir, entity1 + '.md'), 'w', encoding='utf-8') as f: f.write(entity1_content)
with open(os.path.join(entities_dir, entity2 + '.md'), 'w', encoding='utf-8') as f: f.write(entity2_content)

# Read index.md and insert at appropriate sections
with open(index_file, 'r', encoding='utf-8') as f:
    index_lines = f.readlines()

new_index_lines = []
for line in index_lines:
    new_index_lines.append(line)
    if line.strip() == "## Sources":
        new_index_lines.append("- `摘要-vercel-agent-skills-擴充包集合` — 關於 Vercel Labs 專為 AI 代理設計的技能擴充包\n")
        new_index_lines.append("- `摘要-notebooklm-py-非官方api與工具` — 關於非官方 Google NotebookLM API 與工具的實作介紹\n")
    if line.strip() == "## Entities":
        new_index_lines.append("- `Vercel Labs` — Vercel 旗下的開源實驗室，維護 Agent Skills 專案\n")
        new_index_lines.append("- `teng-lin` — 開源專案 notebooklm-py 的開發者\n")

with open(index_file, 'w', encoding='utf-8') as f:
    f.writelines(new_index_lines)

# Log to log.md
with open(log_file, 'a', encoding='utf-8') as f:
    f.write("## [2026-07-13] ingest | 處理了 raw/04-clipper/ 下的 notebooklm-py 與 vercel agent skills 文章\n")
    f.write("- **新增 Sources**: `摘要-vercel-agent-skills-擴充包集合`, `摘要-notebooklm-py-非官方api與工具`\n")
    f.write("- **新增 Entities**: `Vercel Labs`, `teng-lin`\n")
    f.write("- **修改**: `index.md`\n")

# Move files to archive
import shutil
for file in os.listdir(raw_dir):
    if file.endswith('.md'):
        shutil.move(os.path.join(raw_dir, file), os.path.join(archive_dir, file))
