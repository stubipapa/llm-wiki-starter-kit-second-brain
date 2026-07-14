---
name: version
description: >
  版本檢查與架構自動升級。當用戶輸入 /version、詢問「目前版本」、「檢查更新」、
  「升級知識庫」時觸發。透過 GitHub Raw URL 比對本地與遠端版本號，
  若有新版本則引導使用者安全升級架構（絕不觸碰使用者資料）。
user-invocable: true
---

# version 技能：版本檢查與架構自動升級

## 1. 核心目標
讓使用者透過 `/version` 指令，即時得知當前知識庫架構版本，並與 GitHub 遠端倉庫比對。若有新版本可用，引導使用者進行**安全的架構升級**——只更新骨架檔案，絕不觸碰使用者的知識資料。

## 2. 觸發邏輯
- 用戶執行 `/version`：啟動版本檢查流程。
- 隱式觸發：用戶提及「目前版本」、「檢查更新」、「升級知識庫」、「有沒有新版」時自動觸發。

## 3. 核心常數
- **本地版本檔案**：Vault 根目錄 `./VERSION`
- **遠端版本 URL**：`https://raw.githubusercontent.com/stubipapa/llm-wiki-starter-kit-second-brain/main/VERSION`
- **遠端變更日誌 URL**：`https://raw.githubusercontent.com/stubipapa/llm-wiki-starter-kit-second-brain/main/CHANGELOG.md`
- **遠端倉庫 Clone URL**：`https://github.com/stubipapa/llm-wiki-starter-kit-second-brain.git`

## 4. 版本檢查流水線 (SOP)

### 步驟 1：讀取本地版本
讀取 Vault 根目錄的 `VERSION` 檔案內容（去除首尾空白）。
- 若 `VERSION` 檔案不存在，回報：「⚠️ 未偵測到版本標記檔。您的知識庫可能是在 v2.3 之前安裝的。建議執行升級以獲取最新架構。」
- 將缺失版本視為 `v0.0`（強制觸發升級流程）。

### 步驟 2：讀取遠端版本
透過 HTTP 請求讀取遠端 `VERSION` 檔案的 Raw 內容：
`https://raw.githubusercontent.com/stubipapa/llm-wiki-starter-kit-second-brain/main/VERSION`
- 若網路無法連線或讀取失敗，回報：「⚠️ 無法連線至 GitHub，請確認網路狀態。當前本地版本為 [本地版本]。」並終止流程。

### 步驟 3：比對版本
將本地版本與遠端版本進行字串比較。

#### 情況 A：版本相同
向使用者回報：
> ✅ 您的知識庫架構已是最新版本：**[版本號]**
> 無需更新。

終止流程。

#### 情況 B：版本不同
向使用者回報差異，並讀取遠端 `CHANGELOG.md` 顯示更新內容：
> 🔔 發現新版本！
> - 本地版本：**[本地版本]**
> - 遠端版本：**[遠端版本]**
>
> **更新內容：**
> [從 CHANGELOG.md 擷取新版本的變更摘要]
>
> 是否要升級？（升級只會更新架構檔案，您的知識資料完全不受影響）

**暫停並等待使用者確認。** 若使用者拒絕，終止流程。

### 步驟 4：Clone 遠端倉庫
使用者確認升級後，執行：
```bash
git clone --depth 1 https://github.com/stubipapa/llm-wiki-starter-kit-second-brain.git _upgrade_temp
```
`--depth 1` 只抓最新一層 commit，速度最快。

### 步驟 5：比對並列出變更清單
逐一比對以下**架構白名單**中的檔案，找出差異：

**架構白名單（可覆寫）：**
```
VERSION
CHANGELOG.md
README.md
WIKI_SCHEMA.md
CLAUDE.md
.agyrules
scaffold.sh
.agents/skills/*/SKILL.md
.agents/skills/*/scripts/*
.claude/skills/*/skill.md
.claude/skills/*/scripts/*
```

比對邏輯：
1. 對每個白名單檔案，比較本地與遠端的內容差異。
2. 若遠端有新增的 skill 資料夾（本地不存在），標記為「新增」。
3. 向使用者展示變更清單：

> **即將執行的變更：**
> - 🔄 更新：`WIKI_SCHEMA.md`（規範有修正）
> - 🔄 更新：`.agents/skills/ingest/SKILL.md`（新增功能）
> - ➕ 新增：`.agents/skills/export/SKILL.md`（新技能）
> - ➕ 新增：`.claude/skills/export/skill.md`（新技能）
> - ⏭️ 無變化：`CLAUDE.md`
>
> ⚠️ 以下檔案**不會被觸碰**：`wiki/`、`raw/`、`assets/`、`.obsidian/`
>
> 確認執行嗎？

**暫停並等待使用者最終確認。**

### 步驟 6：執行安全覆寫
逐一將有差異的檔案從 `_upgrade_temp/` 複製到 Vault 根目錄，覆寫對應檔案。
- 新增的 skill 資料夾：完整建立目錄並複製。
- **硬約束**：此步驟中任何目標路徑若位於 `wiki/`、`raw/`、`assets/`、`.obsidian/` 內，立即中止並報錯。

### 步驟 7：追加升級日誌
在 `wiki/log.md` 最底部追加一筆記錄：
```markdown
## [YYYY-MM-DD] version | 架構從 [舊版本] 升級至 [新版本]
- 更新檔案：[列出所有被更新的檔案]
- 新增檔案：[列出所有新增的檔案]
```

### 步驟 8：清理暫存目錄
```bash
rm -rf _upgrade_temp
```

### 步驟 9：完成報告
向使用者回報：
> 🎉 升級完成！
> - **舊版本**：[舊版本] → **新版本**：[新版本]
> - 已更新 X 個檔案，新增 Y 個檔案
> - 您的知識資料（wiki/、raw/）完全未受影響 ✅

## 5. 安全邊界（硬約束）

### 🔴 絕對禁止觸碰的路徑（使用者資料黑名單）
- `wiki/**/*`（包含 index.md、log.md、所有知識頁面）
  - **唯一例外**：步驟 7 中對 `wiki/log.md` 的**追加寫入**（Append-only），不可覆寫。
- `raw/**/*`
- `assets/**/*`
- `.obsidian/**/*`

### ✅ 允許更新的路徑（架構白名單）
- `VERSION`
- `CHANGELOG.md`
- `README.md`
- `WIKI_SCHEMA.md`
- `CLAUDE.md`
- `.agyrules`
- `scaffold.sh`
- `.agents/skills/**/SKILL.md`
- `.agents/skills/**/scripts/**`
- `.claude/skills/**/skill.md`
- `.claude/skills/**/scripts/**`

### ⚠️ 防護機制
- 升級前必須經過**兩次使用者確認**（步驟 3 + 步驟 5）。
- 每次覆寫前驗證目標路徑不在黑名單中。
- 操作完成後必須清理暫存目錄。

## 注意事項
- 使用繁體中文編寫所有回報訊息。
- 若遠端版本號格式異常（非 `vX.Y` 格式），回報錯誤並終止。
- 若 `git clone` 失敗，回報網路或權限錯誤並終止。
