# AI教學賦能創新，從課程發想到教學實踐｜網頁簡報

115年 Inspire Hub：永續教學創新與實踐 教師成長社群活動。講者：唐嘉偉 副教授（國立澎湖科技大學 行銷與物流管理系）。

由 `mktech-ai-course`（行銷科技與數據分析，176 頁）改版而來的單檔網頁簡報，目前共 110 頁、六個部份。

- 線上網址：https://jiaweitang701111-cpu.github.io/ai-teaching-innovation/
- `index.html`：成品，單一檔案，可直接用瀏覽器開啟（離線可用）。
- `share/QRcode.png`：掃碼開啟線上簡報。
- `share/講義下載QRcode.png`：掃碼開啟講義資料夾（https://drive.google.com/drive/folders/1QMNTzN4XUz1vCEbzG4f3tmNb11SHgT3d）。
- `share/分享卡.png`：兩個 QR code 並排的分享卡，由 `tools/share-card.html` 截圖；QR code 由 `tools/make_qr.py` 產生。
- `AI教學賦能創新_簡報.pdf`：110 頁 PDF（不放進 repo）。

## 部份與頁碼

| 部份 | 頁碼 |
|------|------|
| 封面 | 1 |
| 第一部份 生成式AI介紹與工具指南 | 2–15 |
| 第二部份 Prompt 的法則與要素 | 16–28 |
| 第三部份 ChatGPT 文案生成、市場調查、數據分析與 ChatGPT Work | 29–51 |
| 第四部份 ChatGPT 生成圖片 | 52–59 |
| 第五部份 ChatGPT Skills介紹 | 60–70 |
| 第六部份 Claude 功能與使用全攻略 | 71–109 |
| Q&A | 110 |

互動演練頁：5（應用場景）、24（結構化 Prompt）、31（社群文案）、33（活動企劃）、37–39（市場調查）、59（生圖萬能公式）、91（Claude 三模式）、108（Cowork 簡報指令）。

## 改版紀錄

### 2026-10-29 第三輪（112 → 110 頁）

- 刪除第 63 頁（GPTs 移轉）、第 67 頁（上線前測試情境）；Skills 五個案例（第 68–72 頁）改為餐飲旅館業案例。
- 第 4 頁重點詞上色；第 5 頁任務選項每個場景增為 8 個、說明卡放大；第 33 頁活動數量改自填；第 37 頁加入自填的分析面向。
- 第 31、33 頁標題改為「演練：撰寫…Prompt」；第 51 頁改為「七個提示詞」。
- 第 22、30、32、34、35、42、107 頁放大字級；段落加上避免孤字的換行設定。
- 分享卡加入講義下載 QR code。

### 2026-10-28 第二輪（120 → 112 頁）

- 刪除原第 6、15、31、32、45、46、58、73、109 頁；原第 36、37 頁合併為「實作演練：廣告文案生成」。
- 原第 5 頁改為互動頁；原第 26 頁改為結構化 Prompt 互動頁；社群文案與活動企劃案之後各新增一頁互動頁。
- 原第 74–81 頁（ChatGPT Work）移到「營運資料分析的注意事項」之後，歸入第三部份。
- 第 12 頁表格改以 ChatGPT 為第一欄，更新三家最新模型與 ChatGPT、Claude 的指標性工具；第 20 頁 LLM 清單更新（依各官方公告，2026-10-28 查證）。
- 第四部份「ChatGPT Image 2.0」全改為「ChatGPT Image 2.5」。
- 文案生成、活動企劃、廣告文案、影音腳本改為餐飲旅館業案例（澎科大海景飯店）。
- 修正跑版：四大角色、LLM × AI Tools 表格、結構化 Prompt、文案生成各頁、Excel 運算、Cowork 五場景表格、STEP 4–5。

### 2026-10-28 第一輪（176 → 120 頁）

新封面、搬移生圖演練頁、刪除指定頁與 Gemini 部份、新增 Q&A；金屬扣件範例全部改為餐飲旅館業範例。

## 重新產生

- 第三輪腳本：`python tools/v4/build4.py`。輸入為 git commit `994f348` 的 112 頁 `index.html`；樣式在 `tools/v4/style.css`。
- 第二輪腳本：`python tools/v3/build3.py`。輸入為 git commit `b7f4982` 的 120 頁 `index.html`；新頁面在 `tools/v3/slides.html`、樣式在 `tools/v3/style.css`、互動程式在 `tools/v3/script.js`。
- 第一輪腳本：`tools/build.py`（輸入為 mktech-ai-course 的 176 頁 `index.html`）。
- 版面檢查：以本機伺服器開啟 `index.html?check=1`，結果顯示在頁面最下方（`tools/check.js`）。
- PDF：`msedge --headless=new --no-pdf-header-footer --print-to-pdf=簡報.pdf "file:///…/index.html?print=1"`（不要加 `--virtual-time-budget`；Edge 可能在背景執行，檔案會晚幾十秒才寫出）。
- QR code：`python tools/make_qr.py <網址> share/QRcode.png`，再用無頭瀏覽器以 1920×1080 截圖 `tools/share-card.html`。

## 操作

← → 換頁、M 目錄、O 總覽、G 跳頁、F 全螢幕；網址後加 `#35` 可直接開到第 35 頁。手機上可左右滑動換頁，互動頁會改成可捲動的單欄版面。
