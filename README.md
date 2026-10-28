# AI教學賦能創新，從課程發想到教學實踐｜網頁簡報

115年 Inspire Hub：永續教學創新與實踐 教師成長社群活動。講者：唐嘉偉 副教授（國立澎湖科技大學 行銷與物流管理系）。

由 `mktech-ai-course`（行銷科技與數據分析，176 頁）改版而來的單檔網頁簡報，共 120 頁、六個部份。

- 線上網址：https://jiaweitang701111-cpu.github.io/ai-teaching-innovation/
- `index.html`：成品，單一檔案，可直接用瀏覽器開啟（離線可用）。
- `share/QRcode.png`、`share/分享卡.png`：掃碼開啟線上簡報。分享卡由 `tools/share-card.html` 截圖，QR code 由 `tools/make_qr.py` 產生。
- `AI教學賦能創新_簡報.pdf`：120 頁 PDF（不放進 repo）。

## 2026-10-28 改版內容

1. 封面改為「115年 Inspire Hub: 永續教學創新與實踐 教師成長社群活動／AI教學賦能創新，從課程發想到教學實踐」。
2. 原第 103 頁「演練：用萬能公式寫一段生圖提示詞」移到原第 63 頁之後，眉標改為「第四部份｜ChatGPT 生成圖片」，按鈕改為開啟 ChatGPT。
3. 原第 52 頁章名改為「ChatGPT生成圖片」，副標一併改為生圖內容。
4. 刪除原第 26、28、29、53–57、89–135（第 103 頁除外）、174–176 頁；Gemini 部份整段移除，Claude 由第七部份改為第六部份；新增最後一頁「Q&A／感謝聆聽、歡迎詢問交流」。
5. 金屬扣件範例全部改為餐飲旅館業範例（共約 30 頁，含互動演練的「帶入範例」資料）；行銷、品牌、零售案例保留不動。

## 重新產生

- 改版腳本：`tools/build.py`（輸入為 mktech-ai-course 的 176 頁 `index.html`，逐頁替換清單都在檔案裡）。
- PDF：`msedge --headless=new --no-pdf-header-footer --print-to-pdf=簡報.pdf "file:///…/index.html?print=1"`（不要加 `--virtual-time-budget`）。
- QR code：`python tools/make_qr.py <網址> share/QRcode.png`，再用無頭瀏覽器以 1920×1080 截圖 `tools/share-card.html`。

## 部份與頁碼

| 部份 | 頁碼 |
|------|------|
| 封面 | 1 |
| 第一部份 生成式AI介紹與工具指南 | 2–17 |
| 第二部份 Prompt 的法則與要素 | 18–32 |
| 第三部份 ChatGPT 文案生成與數據分析 | 33–48 |
| 第四部份 ChatGPT 生成圖片 | 49–56 |
| 第五部份 ChatGPT Skills 與 Work | 57–81 |
| 第六部份 Claude 功能與使用全攻略 | 82–119 |
| Q&A | 120 |

## 操作

← → 換頁、M 目錄、O 總覽、G 跳頁、F 全螢幕；網址後加 `#35` 可直接開到第 35 頁。手機上可左右滑動換頁，並有「放大」按鈕。
