# -*- coding: utf-8 -*-
"""第三輪改版（2026-10-29 使用者 17 項調整）。
輸入：已上線的 112 頁版本（git commit 994f348 的 index.html），頁碼一律指 112 頁版本。
輸出：專案根目錄 index.html（110 頁）。樣式在同資料夾 style.css。
"""
import re, sys, io, pathlib, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BASE_COMMIT = "994f348"

doc = subprocess.check_output(["git", "-C", str(ROOT), "show", f"{BASE_COMMIT}:index.html"]).decode("utf-8")
pat = re.compile(r"<section\b.*?</section>", re.S)
ms = list(pat.finditer(doc))
assert len(ms) == 112, len(ms)
head, tail = doc[:ms[0].start()], doc[ms[-1].end():]
S = {i + 1: m.group(0) for i, m in enumerate(ms)}

def sub(p, old, new, n=1):
    c = S[p].count(old)
    assert c == n, f"p{p}: found {c}x (want {n}): {old[:60]}"
    S[p] = S[p].replace(old, new)

def hl(p, text, parts):
    """把一段 r10 文字拆成多段，parts = [(文字, 類別或 None)]"""
    assert "".join(t for t, _ in parts) == text, text
    new = "".join(f'<span class="r10{" " + c if c else ""}">{t}</span>' for t, c in parts)
    sub(p, f'<span class="r10">{text}</span>', new)

# 1 第 4 頁：重點上色
hl(4, "快速生成中英文的訂房確認信、團體與宴會報價回覆、旅客詢問回覆。",
   [("快速生成中英文的", None), ("訂房確認信、團體與宴會報價回覆", "k-hl"), ("、旅客詢問回覆。", None)])
hl(4, "客服問答機器人處理訂房訂位查詢、取消與退款政策說明。",
   [("客服問答機器人", "k-hl2"), ("處理訂房訂位查詢、", None), ("取消與退款政策說明", "k-hl"), ("。", None)])
hl(4, "協助撰寫菜單與住房專案說明、食材成本分析摘要、過敏原標示資料。",
   [("協助撰寫", None), ("菜單與住房專案說明", "k-hl"), ("、食材成本分析摘要、", None), ("過敏原標示資料", "k-hl"), ("。", None)])
hl(4, "利用影像生成模擬新菜色擺盤、客房佈置或餐廳空間情境。",
   [("利用", None), ("影像生成", "k-hl2"), ("模擬新菜色擺盤、客房佈置或餐廳空間情境。", None)])
hl(4, "自動產出產品文案、網站內容、社群貼文素材。",
   [("自動產出", None), ("產品文案、網站內容、社群貼文素材", "k-hl"), ("。", None)])
hl(4, "製作多語言住房專案簡介與電子菜單。",
   [("製作", None), ("多語言", "k-hl2"), ("住房專案簡介與電子菜單", "k-hl"), ("。", None)])

# 6、8 第 31、33 頁標題；8 活動數量改自填
sub(31, "演練：套用模板寫社群媒體文案 Prompt", "演練：撰寫社群媒體文案 Prompt", 2)
sub(33, "演練：套用模板寫活動企劃案 Prompt", "演練：撰寫活動企劃案 Prompt", 2)
sub(33, '<div class="fld"><span>活動數量</span>\n          <div class="chips" data-pick="count"><button>三項</button><button class="on">五項</button><button>十項</button></div></div>',
    '<label class="fld"><span>活動數量</span><input data-f="count" value="五項" placeholder="例如：五項" autocomplete="off"></label>')

# 11 第 37 頁：分析面向下方加自填欄
sub(37, '<div class="foot">',
    '<label class="fld"><span>其他分析面向 <small>（自行填寫，多項請用頓號分隔）</small></span>'
    '<input data-f="aspect" placeholder="例如：數位行銷與社群口碑" autocomplete="off"></label>\n        <div class="foot">')

# 12 第 42 頁：前三張卡片
for n in "123":
    sub(42, f'<div class="k-ncard"><i class="n">{n}</i>', f'<div class="k-ncard lg"><i class="n">{n}</i>')

# 13 第 51 頁
sub(51, "把八個提示詞串成一份筆電銷售分析工作包", "把七個提示詞串成一份筆電銷售分析工作包", 2)

# 15 第 68–72 頁：改為餐飲旅館業案例
for p, k in zip(range(68, 73), "一二三四五"):
    sub(p, f"第五部份｜ChatGPT Skills：案例{k}", f"第五部份｜ChatGPT Skills：餐旅案例{k}")
sub(68, "以｛新品上市｝為題目", "以｛新菜單上市｝為題目")
sub(68, "讓更多人知道品牌新資訊。文案強調｛產品亮點｝", "讓更多旅客知道餐廳與飯店的新資訊。文案強調｛餐點或房型亮點｝")
sub(68, "當使用者提供一或多個貼文題目與產品亮點，需要撰寫社群貼文時使用",
         "當使用者提供一或多個貼文題目與餐點、房型或住房專案亮點，需要撰寫社群貼文時使用")
sub(68, "題目清單（如新品上市、限時優惠）、產品亮點、發布平台；缺少產品亮點時先提問。",
         "題目清單（如新菜單上市、連假住房優惠）、餐點或房型亮點、發布平台；缺少亮點時先提問。")
sub(68, "以社群經營專家的角色撰寫", "以餐旅業社群經營專家的角色撰寫")
sub(68, "未提供的價格、優惠期限與功效不得自行編造。", "未提供的價格、優惠期限與空房狀況不得自行編造。")
sub(68, "references/產品資料.md", "references/菜單與房型資料.md")

sub(69, "你是位實務經驗豐富｛產業專家｝", "你是位實務經驗豐富｛觀光餐旅產業專家｝")
sub(69, "提出｛主要市場趨勢與報告摘要｝", "提出｛主要旅遊趨勢與報告摘要｝")
sub(69, "當使用者上傳產業或市場調查報告，需要摘要市場趨勢、重點洞察與營運風險並分享給團隊時使用。",
         "當使用者上傳觀光、旅宿或餐飲市場報告，需要摘要旅遊趨勢、重點洞察與營運風險並分享給團隊時使用。")
sub(69, "報告檔案、所屬產業、團隊關心的議題", "報告檔案、業態（飯店、民宿或餐廳）、團隊關心的議題")
sub(69, "以實務經驗豐富的產業專家角色", "以實務經驗豐富的觀光餐旅產業專家角色")
sub(69, "另列預期的營運風險。", "另列預期的營運風險（如淡旺季、人力與食材成本）。")
sub(69, "references/公司產品線與目標市場.md（讓洞察對應公司的業務）", "references/本店客群與房型.md（讓洞察對應本店的客群與產品）")

sub(70, "為公司爭取到更有利的價格和條件。 目前收到的報價和條件：｛對方提供的報價｝。希望的報價和條件：｛自己期待的報價和`議價理由｝。 撰寫回覆的議價信，包含開頭問候、強調公司的價值",
         "為飯店爭取到更有利的價格和條件。目前收到的報價和條件：｛食材或客房備品供應商的報價｝。希望的報價和條件：｛自己期待的報價和議價理由，例如年度採購量｝。撰寫回覆的議價信，包含開頭問候、強調飯店的價值")
sub(70, "當使用者收到報價並希望爭取更有利的價格與條件",
         "當使用者收到食材、客房備品或布巾洗滌等供應商報價，並希望爭取更有利的價格與條件")
sub(70, "對方提供的報價、自己期待的報價與條件、議價理由、收件對象與語言。",
         "供應商的報價、自己期待的報價與條件、議價理由（如年度採購量、付款條件）、收件對象與語言。")
sub(70, "公司價值與長期合作潛力", "飯店價值與長期合作潛力")
sub(70, "不寫入未經授權的承諾。", "不寫入未經授權的採購承諾。")
sub(70, "references/議價原則與授權範圍.md", "references/採購議價原則與授權範圍.md")

sub(71, "部屬的具體問題是：｛描述部屬的具體問題或行為｝", "部屬的具體問題是：｛描述部屬的具體問題或行為，例如櫃檯人員多次未依 SOP 辦理入住｝")
sub(71, "當主管準備與表現不佳的部屬面談", "當餐廳或飯店主管準備與表現不佳的部屬面談")
sub(71, "部屬的具體問題或行為、發生期間、已採取的措施",
         "部屬的具體問題或行為（如外場多次遲到、櫃檯未依 SOP 辦理入住）、發生期間、已採取的措施")
sub(71, "references/公司績效面談規範.md", "references/員工考核與面談規範.md")

sub(72, "例如周末瑜珈課程", "例如海景客房早鳥優惠")
sub(72, "例如Flat Illustration", "例如寫實攝影")
sub(72, "例如16:9", "例如4:5")
sub(72, "例如在公園中進行瑜伽的場景，多名年輕人參與，背景是陽光明媚的早晨", "例如面海客房的陽台早餐，一對情侶在晨光中用餐")
sub(72, "當使用者需要為社群平台貼文生成圖片", "當使用者需要為飯店或餐廳的社群貼文生成圖片")
sub(72, "不使用他人商標或名人肖像。", "不使用他人商標或名人肖像；餐點與客房畫面不得誇大實際樣貌。")
sub(72, "<span class=\"r10\">品牌色票與標誌使用規範</span>", "<span class=\"r10\">飯店品牌色票與標誌使用規範</span>")

# 16 第 107 頁表格字放大
sub(107, '<table class="k-tbl" style="font-size:17px">', '<table class="k-tbl" style="font-size:19px">')
sub(107, '<colgroup><col style="width:186px"><col style="width:372px"><col></colgroup>',
         '<colgroup><col style="width:196px"><col style="width:380px"><col></colgroup>')

# 14 刪除第 63、67 頁
order = [p for p in range(1, 113) if p not in (63, 67)]
assert len(order) == 110
out = head + "\n".join(S[p] for p in order) + tail

# ---------------------------------------------------------------- 樣式與程式
def osub(old, new, n=1):
    global out
    c = out.count(old)
    assert c == n, f"script: found {c}x: {old[:70]}"
    out = out.replace(old, new)

i = out.index("</style>")
out = out[:i] + (HERE / "style.css").read_text(encoding="utf-8") + out[i:]

# 3 第 5 頁：任務選項增加到每個場景 8 個
osub("tasks:['生成新人入職的 SOP 教案','製作食品安全與服務禮儀測驗題庫','模擬旅客客訴情境，讓新進員工練習應對','撰寫作業流程變更說明']",
     "tasks:['生成新人入職 SOP 教案','製作食安與服務禮儀題庫','模擬客訴情境讓新人練習','撰寫作業流程變更說明','設計櫃檯接待角色扮演腳本','製作新人第一週學習清單','整理常見客訴回應話術','製作外語接待常用句卡']")
osub("tasks:['總結最新觀光產業報告的重點','分析周邊競爭飯店與餐廳的動態','整理線上評論，找出服務改善重點','比較各訂房平台的價格與評價']",
     "tasks:['總結最新觀光產業報告','分析周邊競爭飯店動態','整理線上評論找改善重點','比較訂房平台價格與評價','彙整連假與節慶訂房趨勢','分析目標客群旅遊偏好','整理周邊景點與活動資訊','整理觀光補助與政策重點']")
osub("tasks:['整合菜單、房型與活動資料，建立旅客問答庫','彙整各部門回饋，提出決策建議','製作跨部門交接與待辦清單','整理旅客常見問題，提供櫃檯與客服使用']",
     "tasks:['建立菜單房型活動問答庫','彙整各部門回饋提出建議','製作跨部門交接待辦清單','整理旅客常見問題給客服','統整採購與庫存需求','整理各部門月報成經營摘要','建立房務與櫃檯交班格式','彙整旅客回饋分派改善任務']")
# 8 活動數量改自填
osub("+'，撰寫出「'+m(v.count||'五項','五項')+'」歡慶活動的企劃案。", "+'，撰寫出「'+m(v.count,'＿＿（活動數量）')+'」歡慶活動的企劃案。")
osub("{name:'澎科大海景飯店',theme:'開幕十週年紀念',tgt:", "{name:'澎科大海景飯店',theme:'開幕十週年紀念',count:'五項',tgt:")
# 11 市場調查：自填的分析面向一併列入
osub("+(v.$on.length?'<b>'+v.$on.map(esc).join('、')+'</b>':'<u>請至少選一個分析面向</u>')+'等。'}),",
     "+((a=>a.length?'<b>'+a.map(esc).join('、')+'</b>':'<u>請至少選一個分析面向</u>')(v.$on.concat((v.aspect||'').split(/[、,，]/).map(s=>s.trim()).filter(Boolean))))+'等。'}),")

(ROOT / "index.html").write_text(out, encoding="utf-8", newline="\n")
secs = pat.findall(out)
print("slides:", len(secs), "bytes:", len(out.encode("utf-8")))
for i in (4, 5, 31, 33, 37, 49, 61, 64, 65, 66, 67, 68, 69, 70, 105, 110):
    print(f"{i:>3}", re.search(r'data-t="([^"]*)"', secs[i - 1]).group(1))
