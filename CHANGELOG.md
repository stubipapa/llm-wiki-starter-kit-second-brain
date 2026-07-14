# Changelog

本檔案記錄 LLM Wiki Starter Kit - Second Brain 的所有版本更新。

---

## [v2.4.1] - 2026-07-14
### 修復
- `scaffold.sh`：修正 Bash 運算子優先權 Bug，確保目標目錄已存在時亦可順利安裝。

---

## [v2.4] - 2026-07-14
### 新增
- **`/version` 技能**：支援一鍵版本檢查與架構自動升級，透過 GitHub Raw URL 比對版本號，僅更新架構檔案，絕不觸碰使用者資料。
- **`VERSION` 檔案**：根目錄新增純文字版本標記檔，作為版本號的單一真相來源。
- **`CHANGELOG.md`**：新增獨立的變更日誌，追蹤每個版本的具體修改。

### 變更
- `CLAUDE.md`、`.agyrules` 新增 `/version` 路由。
- `scaffold.sh` 新增 `VERSION` 檔案複製與 version skill 目錄建立。
- `README.md` 升級至 v2.4，新增 `/version` 技能說明與架構圖更新。

---

## [v2.3] - 2026-07-14
### 修復
- **雙軌架構對齊**：同步 `.agents/skills/` 與 `.claude/skills/` 的所有技能內容，解決 `ingest` 的防呆機制與 `scaffold` 的完整 SOP 在兩邊不一致的問題。
- **Python 腳本歸檔**：將根目錄散落的 4 個 Python 腳本（`fix_links.py`、`lint_check.py`、`ingest_script.py`、`ingest_skills_dir.py`）移至對應 skill 的 `scripts/` 子目錄。
- **全域雙鏈格式優化**：將 `index.md` 與 scaffold 範本中的反引號格式統一修正為 Obsidian 雙鏈 `[[ ]]` 格式。
- **Syntheses 格式修正**：為 `總結-產品數據調查10位理論框架.md` 補上遺漏的 `## 關聯連接` 區塊。

---

## [v2.2] - 2026-07-08
### 新增
- **防呆與正規化比對 (Pre-Ingest Normalization)**：升級 `/ingest` 技能，攝取前強制檢索 `wiki/index.md`，自動對齊現有實體與概念的命名（大小寫、縮寫），徹底杜絕死鏈與重複頁面。

---

## [v2.1] - 2026-07-07
### 新增
- **Scaffold 安裝精靈升級**：支援一鍵無痛部署（免互動確認），用戶可在 Prompt 中直接指定目標路徑。
- **Claude Code 路由補齊**：`CLAUDE.md` 新增完整的斜線指令路由表。
- **架構結構圖**：`README.md` 新增 Vault 初始化後的完整目錄樹狀圖。

---

## [v2.0] - 2026-07-07
### 新增
- 初始版本發佈。
- 三大核心 Skills：`/ingest`、`/query`、`/lint`。
- `scaffold` 安裝精靈（Shell 腳本 + AI 互動式）。
- 完整的目錄架構：`raw/`、`wiki/`、`assets/`。
- 雙平台支援：Claude Code (`.claude/skills/`) + Antigravity (`.agents/skills/`)。
- `WIKI_SCHEMA.md` 核心規範契約。
