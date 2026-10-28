# -*- coding: utf-8 -*-
"""Inspire Hub teacher-community deck, built from the 176-page mktech deck.
1 new cover   2 move p103 after p63   3 p52 -> ChatGPT生成圖片
4 drop 26,28,29,53-57,89-135(except 103),174-176, renumber parts, add Q&A
5 fastener examples -> food & beverage / hotel examples (marketing/retail kept)
"""
import re, sys, io, pathlib
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
HERE = pathlib.Path(__file__).parent
SRC = pathlib.Path("D:/Claude AI/行銷科技與數據分析-AI工具簡報-115/index.html")
OUT = HERE / "out" / "index.html"
OUT.parent.mkdir(exist_ok=True)
doc = SRC.read_text(encoding="utf-8")

pat = re.compile(r"<section\b.*?</section>", re.S)
ms = list(pat.finditer(doc))
assert len(ms) == 176
head, tail = doc[:ms[0].start()], doc[ms[-1].end():]
S = {i + 1: m.group(0) for i, m in enumerate(ms)}

# ---------------------------------------------------------------- per-page text
R = {
 4: [("以金屬扣件廠商為例", "以餐飲旅館業者為例"),
     ("快速生成專業中英文的客戶開發信、報價單回覆、訂單確認信。", "快速生成中英文的訂房確認信、團體與宴會報價回覆、旅客詢問回覆。"),
     ("客服問答機器人處理出貨查詢、退換貨政策說明。", "客服問答機器人處理訂房訂位查詢、取消與退款政策說明。"),
     ("技術與研發支援", "產品與服務研發支援"),
     ("協助撰寫產品規格書、技術分析摘要、材料報告。", "協助撰寫菜單與住房專案說明、食材成本分析摘要、過敏原標示資料。"),
     ("利用影像生成模擬新型扣件結構或應用場景。", "利用影像生成模擬新菜色擺盤、客房佈置或餐廳空間情境。"),
     ("製作多語言市場簡報與電子型錄。", "製作多語言住房專案簡介與電子菜單。")],
 5: [("品保訓練測驗題庫", "食品安全與服務禮儀測驗題庫"),
     ("整合產品資料庫、客戶技術需求", "整合產品資料庫、旅客評論與需求")],
 7: [("金屬扣件企業可從接單、詢價、報價、採購、品質與客訴等流程中", "餐飲旅館業者可從訂房訂位、團體詢價、報價、採購、食安與客訴等流程中")],
 11: [("金屬扣件企業導入建議", "餐飲旅館業導入建議"),
      ("業務、採購與品管等核心使用者", "業務、訂房、行銷與餐飲管理等核心使用者")],
 16: [("扣件企業的應用", "餐飲旅館業的應用"),
      ("「客戶詢價單整理」「規格書摘要」「品質異常分析」", "「團體訂房詢價整理」「線上評論摘要」「客訴原因分析」")],
 34: [("扣件產業範例", "餐飲旅館業範例"),
      ("請記住我任職於金屬扣件製造商，常需要整理客戶詢價單、產品規格與報價資料", "請記住我任職於連鎖飯店的業務行銷部，常需要整理團體訂房詢價、住房專案與報價資料")],
 35: [("扣件企業的客戶名單、報價與製程參數", "餐飲旅館業的住客個資、合約房價與獨家食譜配方")],
 36: [("以及生產資料分析的實務建議", "以及營運資料分析的實務建議")],
 51: [("AI工具應用於生產資料分析的實務建議", "AI工具應用於營運資料分析的實務建議")],
 52: [("ChatGPT：Deep Research", "ChatGPT生成圖片"),
      ("以往需花數週至數月完成的繁複研究工作，透過ChatGPT深度研究功能，在幾分鐘內達成高品質的研究整合。",
       "ChatGPT Image 2.0 生圖提示詞範本，以及用萬能公式寫出自己的提示詞。")],
 58: [("扣件企業可套用於產品型錄、展會海報、客戶簡報與流程圖解。", "餐飲旅館業者可套用於菜單設計、住房專案海報、旅展簡報與服務流程圖解。")],
 60: [("扣件產業套用範例", "餐旅業套用範例"),
      ("『金屬扣件選用指南：材質、強度等級與表面處理』做成教學型資訊圖，搭配流程箭頭與簡單icon，適合B2B社群分享。",
       "『旅客入住指南：報到流程、早餐時段與設施使用規範』做成教學型資訊圖，搭配流程箭頭與簡單icon，適合旅客社群分享。"),
      ("請幫我設計一套扣件品牌社群模板，包含新品發布、展會公告、認證取得與客戶案例版型，工業風配色",
       "請幫我設計一套民宿品牌社群模板，包含新菜單發布、節慶住房專案、在地活動公告與旅客好評版型，海洋藍與沙色配色")],
 61: [("扣件產業改寫", "旅館業改寫"),
      ("將「餐飲品牌」換成「金屬扣件製造商」，內容改為產品線布局、認證與品質體系、外銷市場成長路徑、智慧製造升級與客戶旅程，配色改為深藍、鋼灰與銀色。",
       "將「餐飲品牌」換成「海島度假旅館」，內容改為客房產品組合、訂房通路布局、旅客旅程、會員經營與在地體驗行程，配色改為海洋藍、沙色與白色。")],
 62: [("扣件產業套用範例", "餐旅業套用範例"),
      ("『碳鋼、不鏽鋼與合金鋼螺栓』三種方案做成視覺化比較表，欄位包含強度等級、耐蝕性、適用場景與價格帶，使用圖示與重點標示，讓客戶更容易閱讀。",
       "『標準雙人房、海景家庭房與蜜月套房』三種住房方案做成視覺化比較表，欄位包含房型坪數、早餐與加值服務、適合客群與價格帶，使用圖示與重點標示，讓旅客更容易閱讀。")],
 63: [("扣件產業套用範例", "餐旅業套用範例"),
      ("客戶詢價→報價→接單→生產→出貨", "旅客訂房→入住報到→住宿服務→退房→評論回覆")],
 70: [("扣件廠範例", "餐飲旅館業範例"),
      ("依公司格式撰寫週報或 8D 報告", "依公司格式撰寫週報或客訴處理報告"),
      ("讀取 Outlook 詢價信並整理成 Excel", "讀取 Outlook 團體訂房詢價信並整理成 Excel"),
      ("查詢 ERP 庫存與交期後回覆客戶", "查詢訂房系統空房與房價後回覆旅客")],
 72: [("對方報價每千支 1,250 元", "對方食材報價每箱 1,250 元"),
      ("我們明年保證下單 100 萬支", "我們明年保證採購 5,000 箱")],
 78: [("扣件廠應用與治理", "餐旅業應用與治理"),
      ("扣件廠可以建立的六個 Skills", "餐飲旅館業可以建立的六個 Skills"),
      ("rfq-organizer", "group-booking"),
      ("詢價單整理", "團體訂房詢價整理"),
      ("上傳客戶詢價單或 RFQ 時", "收到旅行社或企業的團體訂房詢價時"),
      ("逐筆規格 Excel（尺寸、牙距、長度、材質、等級、表面處理）", "逐筆需求 Excel（日期、房型、間數、餐食、會議室、預算）"),
      ("quote-reply-en", "guest-reply-en"),
      ("英文報價回覆信", "英文旅客回覆信"),
      ("需要回覆海外客戶的詢價或交期時", "需要回覆海外旅客的訂房、加床或接駁詢問時"),
      ("須向客戶確認的事項", "須向旅客確認的事項"),
      ("線材、電鍍或熱處理外包廠調整報價時", "食材、備品或布巾洗滌廠商調整報價時"),
      ("quality-8d-draft", "review-response"),
      ("品質異常 8D 報告草稿", "負評回覆與改善報告"),
      ("發生客訴或製程異常時", "訂房平台出現負評或發生客訴時"),
      ("8D 各步驟草稿；原因分析標示「待驗證」", "回覆草稿＋改善對策；原因標示「待查證」"),
      ("新人詢問 SOP 或公司制度時", "新進櫃檯或外場人員詢問 SOP 時"),
      ("weekly-production-summary", "weekly-revenue-summary"),
      ("生產週報摘要", "營運週報摘要"),
      ("上傳 MES 週報匯出檔時", "上傳訂房系統或 POS 週報匯出檔時"),
      ("稼動率、不良率與三點重點摘要", "住房率、平均房價與三點重點摘要"),
      ("講師依扣件廠常見工作設計；涉及客戶圖面、報價與成本等紅級資料者", "講師依餐飲旅館業常見工作設計；涉及住客個資、合約房價與成本等紅級資料者")],
 79: [("扣件廠應用與治理", "餐旅業應用與治理"),
      ("扣件業務工具包", "訂房業務工具包"),
      ("rfq-organizer 與 quote-reply-en 兩個 Skills，寫好詢價整理與回覆的步驟與格式。",
       "group-booking 與 guest-reply-en 兩個 Skills，寫好團體詢價整理與旅客回覆的步驟與格式。"),
      ("原 GPT 串接 ERP 庫存查詢的自訂動作", "原 GPT 串接訂房系統空房查詢的自訂動作"),
      ("提供業務部安裝使用", "提供業務與訂房部安裝使用")],
 80: [("扣件廠應用與治理", "餐旅業應用與治理"),
      ("客戶圖面與規格書、報價與成本、冷鍛與熱處理參數", "住客個資與訂房紀錄、合約房價與成本、獨家食譜配方"),
      ("資料分級：第二部份〈扣件廠資料分三級〉", "資料分級：講師依餐飲旅館業資料敏感度分為紅、黃、綠三級")],
 84: [("與第三部份的結構化 Prompt", "與第二部份的結構化 Prompt")],
 85: [("扣件廠應用：", "餐飲旅館業應用："),
      ("以公開資訊觀測站的同業財報、財政部關務署的進出口統計作為資料來源，即可比較同業的營收結構與外銷市場布局。",
       "以公開資訊觀測站的觀光餐旅同業財報、交通部觀光署的旅館業營運統計作為資料來源，即可比較同業的營收結構、住房率與平均房價。")],
 86: [("客戶名稱、料號與個資先遮蔽", "客戶名稱、訂單編號與個資先遮蔽")],
 43: [('placeholder="例如：金屬扣件產業"', 'placeholder="例如：餐飲旅館產業"'),
      ("<button>金屬扣件產業</button><button>汽車扣件產業</button><button>航太扣件產業</button><button>建築用扣件產業</button><button>AI 應用於扣件製造產業</button>",
       "<button>餐飲業</button><button>旅館業</button><button>觀光民宿產業</button><button>連鎖咖啡飲料產業</button><button>AI 應用於餐飲旅館產業</button>")],
 44: [('placeholder="例如：台灣扣件製造商"', 'placeholder="例如：台灣連鎖飯店品牌"'),
      ('placeholder="例如：產品等級（標準件-特殊件）"', 'placeholder="例如：服務等級（平價-精品）"')],
 45: [("① 我們是一間＿＿的製造商", "① 我們是一間＿＿的業者"),
      ("② 產品具備＿＿等功能", "② 產品與服務具備＿＿等功能"),
      ('placeholder="例如：汽車扣件"', 'placeholder="例如：海島度假旅館"'),
      ('placeholder="例如：高強度、耐腐蝕"', 'placeholder="例如：海景客房、在地早餐"'),
      ('placeholder="例如：輕量化"', 'placeholder="例如：漁村文化體驗"'),
      ('placeholder="例如：汽車底盤與引擎系統"', 'placeholder="例如：家庭旅遊與蜜月旅行"'),
      ('placeholder="例如：北美與歐洲"', 'placeholder="例如：台灣本島與港澳旅客"'),
      ('placeholder="例如：汽車用高強度螺栓"', 'placeholder="例如：海島度假住宿"'),
      ("帶入扣件範例", "帶入餐旅範例")],
 103: [("第六部份｜Gemini 生圖", "第四部份｜ChatGPT 生成圖片"),
       ('placeholder="例如：一顆 M12 高強度六角螺栓與配套螺帽"', 'placeholder="例如：一盤澎湖海鮮料理與一杯仙人掌冰沙"'),
       ('placeholder="例如：扣件廠的品檢台上"', 'placeholder="例如：海景餐廳靠窗的木質餐桌上"'),
       ('placeholder="例如：柔和的攝影棚側光"', 'placeholder="例如：傍晚的自然光"'),
       ("帶入扣件範例", "帶入餐旅範例"),
       ("貼到 Gemini，選「思考型」模型生成", "貼到 ChatGPT（或 Gemini）生成"),
       ('href="https://gemini.google.com/" target="_blank" rel="noopener" style="text-decoration:none">開啟 Gemini ↗',
        'href="https://chatgpt.com/" target="_blank" rel="noopener" style="text-decoration:none">開啟 ChatGPT ↗')],
 136: [("｜使用注意事項", "")],
 153: [("扣件企業對應", "餐飲旅館業對應"),
       ("經營者與廠長以 Chat 為主，搭配 Cowork 彙整月報；業務／採購／行政以 Chat＋Cowork 處理詢價、報價與請購文件；資訊人員可評估 Claude Code 串接 ERP 報表。",
        "經營者與店長、館長以 Chat 為主，搭配 Cowork 彙整營運月報；業務／訂房／行政以 Chat＋Cowork 處理團體詢價、報價與採購文件；資訊人員可評估 Claude Code 串接訂房系統與 POS 報表。")],
 154: [("扣件企業對應", "餐飲旅館業對應"),
       ("經營者與廠長以 Chat 為主，搭配 Cowork 彙整月報；業務／採購／行政以 Chat＋Cowork 處理詢價、報價與請購文件；資訊人員可評估 Claude Code 串接 ERP 報表。",
        "經營者與店長、館長以 Chat 為主，搭配 Cowork 彙整營運月報；業務／訂房／行政以 Chat＋Cowork 處理團體詢價、報價與採購文件；資訊人員可評估 Claude Code 串接訂房系統與 POS 報表。")],
 169: [("Cowork 五場景 × 金屬扣件企業應用對照", "Cowork 五場景 × 餐飲旅館業應用對照"),
       ("依文章五場景改寫為扣件企業情境", "依文章五場景改寫為餐飲旅館業情境"),
       ("扣件企業對應情境", "餐飲旅館業對應情境"),
       ("整理業務共用槽的客戶圖面與報價單，依客戶／年度歸檔", "整理業務共用槽的團體合約與報價單，依旅行社／年度歸檔"),
       ("請整理「客戶資料」資料夾，依客戶名稱建立子資料夾", "請整理「團體合約」資料夾，依旅行社名稱建立子資料夾"),
       ("彙整多家客戶的規格書，整理共同要求與差異", "彙整訂房平台的旅客評論，整理好評與負評的共同主題"),
       ("請讀取此資料夾所有規格書，整理鍍層、扭力與包裝要求的共同點與差異，輸出比較表。",
        "請讀取此資料夾所有評論匯出檔，整理清潔、早餐與服務三個面向的好評與負評重點，輸出比較表。"),
       ("把品保月報轉為經營會議簡報", "把營運月報轉為經營會議簡報"),
       ("讀取品保月報，轉化為 8 頁的經營會議簡報草稿，重點放在不良率趨勢與對策。",
        "讀取營運月報，轉化為 8 頁的經營會議簡報草稿，重點放在住房率、客訴趨勢與對策。"),
       ("分析各產線不良率與交期達成率", "分析各分店住房率與餐廳翻桌率"),
       ("請讀取生產日報 CSV，清洗後依產線繪製不良率與交期達成率折線圖，輸出 HTML。",
        "請讀取營運日報 CSV，清洗後依分店繪製住房率與翻桌率折線圖，輸出 HTML。"),
       ("整理業務出差與展會的收據", "整理業務出差與旅展的收據")],
 172: [('placeholder="例如：2026 年度品質改善成果"', 'placeholder="例如：2026 年度營運成果"'),
       ("<button>外部稽核人員</button>", "<button>旅行社合作夥伴</button>"),
       ('placeholder="例如：深藍與橘色、使用公司 Logo、字體清楚"', 'placeholder="例如：海洋藍與沙色、使用公司 Logo、字體清楚"'),
       ("<button>客戶稽核</button>", "<button>業務推廣</button>"),
       ("帶入扣件範例", "帶入餐旅範例")],
 173: [("講師補充：扣件企業版", "講師補充：餐飲旅館業版"),
       ("內的產品型錄與品保月報", "內的住房專案介紹與營運月報"),
       ("2026 年度客戶技術交流會", "2027 年度旅行社合作說明會"),
       ("歐美汽車零組件客戶的採購與品保主管", "國內外旅行社與企業獎勵旅遊的採購窗口"),
       ("深藍＋銀灰", "海洋藍＋沙色"),
       ("說明製程能力、品質系統與交期改善成果，爭取年度合約", "說明客房與餐飲產品、服務品質與在地體驗行程，爭取年度合作合約")],
}
for p, pairs in R.items():
    for old, new in pairs:
        n = S[p].count(old)
        assert n >= 1, f"p{p}: not found: {old[:40]}"
        S[p] = S[p].replace(old, new)

# ---------------------------------------------------------------- cover & Q&A
def deck_title(eyebrow, lines, after):
    ps = "".join(f'<p class="p1"><span class="r1">{l}</span></p>' for l in lines)
    return ps
COVER = (
 '<section class="s bn" data-src="1" data-t="AI教學賦能創新，從課程發想到教學實踐">'
 '<i class="e" style="left:85.3px;top:205px;width:106.7px;height:5.3px;background:#F0A35E;border-radius:999px"></i>'
 '<div class="e tb" style="left:85.3px;top:237px;width:1142.7px;height:34.4px;--t:1;--x:0.888">'
 '<div class="ti"><p class="p0"><span class="r0">115年 Inspire Hub: 永續教學創新與實踐 教師成長社群活動</span></p></div></div>'
 '<div class="e tb" style="left:85.3px;top:295.3px;width:1142.7px;height:147.2px;--t:1;--x:0.000">'
 '<div class="ti"><p class="p1"><span class="r1">AI教學賦能創新，</span></p><p class="p1"><span class="r1">從課程發想到教學實踐</span></p></div></div>'
 '<i class="e" style="left:85.3px;top:466.5px;width:1030px;height:1.3px;background:#3A4A63"></i>'
 '<div class="e tb" style="left:85.3px;top:485.9px;width:1030px;height:80px;--t:1;--x:1.7">'
 '<div class="ti"><p class="p2"><span class="r2">唐嘉偉 副教授</span></p>'
 '<p class="p3"><span class="r3">國立澎湖科技大學　行銷與物流管理系</span></p></div></div>'
 '</section>')
QA = (
 '<section class="s bn" data-src="999" data-t="Q&amp;A｜感謝聆聽、歡迎詢問交流">'
 '<i class="e" style="left:85.3px;top:247.7px;width:106.7px;height:5.3px;background:#F0A35E;border-radius:999px"></i>'
 '<div class="e tb" style="left:85.3px;top:279.7px;width:1142.7px;height:34.4px;--t:1;--x:0.888">'
 '<div class="ti"><p class="p0"><span class="r0">Q&amp;A</span></p></div></div>'
 '<div class="e tb" style="left:85.3px;top:338px;width:1142.7px;height:76.3px;--t:1;--x:0.000">'
 '<div class="ti"><p class="p1"><span class="r1">感謝聆聽、歡迎詢問交流</span></p></div></div>'
 '<i class="e" style="left:85.3px;top:438.3px;width:1030px;height:1.3px;background:#3A4A63"></i>'
 '<div class="e tb" style="left:85.3px;top:457.7px;width:1030px;height:80px;--t:1;--x:1.7">'
 '<div class="ti"><p class="p2"><span class="r2">唐嘉偉 副教授</span></p>'
 '<p class="p3"><span class="r3">國立澎湖科技大學　行銷與物流管理系</span></p></div></div>'
 '</section>')
S[1] = COVER

# ---------------------------------------------------------------- order
ORDER = (list(range(1, 26)) + [27] + list(range(30, 53)) + list(range(58, 64)) + [103]
         + list(range(64, 89)) + list(range(136, 174)))
assert len(ORDER) == 119 and len(set(ORDER)) == 119
body = "\n".join(S[p] for p in ORDER) + "\n" + QA
body = body.replace("第七部份", "第六部份")   # Gemini part removed: Claude 7 -> 6
assert "第七部份" not in body
# 第六部份 must now only belong to the Claude part (p136-173)
new_secs = pat.findall(body)
assert len(new_secs) == 120
for i, s in enumerate(new_secs, 1):
    if "第六部份" in s:
        assert ORDER[i - 1] >= 136 if i <= 119 else False, f"slide {i} has 第六部份"

out = head + body + tail

# ---------------------------------------------------------------- JS / meta
def sub1(old, new, s, n=1):
    c = s.count(old)
    assert c == n, f"expected {n} got {c}: {old[:50]}"
    return s.replace(old, new)

out = sub1("<title>行銷科技與數據分析｜115 學年度 Marketing Technology × Data Analytics</title>",
           "<title>AI教學賦能創新，從課程發想到教學實踐｜115年 Inspire Hub 教師成長社群活動</title>", out)
out = sub1("+'｜行銷科技與數據分析'", "+'｜AI教學賦能創新'", out)
out = sub1("localStorage.getItem('fastener-ai:'+k)", "localStorage.getItem('ai-teaching:'+k)", out)
out = sub1("localStorage.setItem('fastener-ai:'+k,", "localStorage.setItem('ai-teaching:'+k,", out)

# dead exercises whose slides are gone (classify / safe / mask / research)
a = out.index("/* ── 分類演練（資料分級、Claude 資料安全） ── */")
b = out.index("/* ── 演練：Claude 三模式測驗 ── */")
out = out[:a] + out[b:]
a = out.index("/* ── 演練二：遮蔽資訊 ── */")
b = out.index("/* ── 演練三～五：Prompt 產生器 ── */")
out = out[:a] + out[b:]
a = out.index("builder('ex-research',")
b = out.index("builder('ex-cowork',")
out = out[:a] + out[b:]

out = sub1("{ind:'金屬扣件產業'}", "{ind:'餐飲旅館產業'}", out)
out = sub1("的製造商，產品具備'", "的業者，產品與服務具備'", out)
out = sub1("{a:'汽車扣件',b:'高強度、耐腐蝕',c:'輕量化',d:'汽車底盤與引擎系統',e:'北美與歐洲',f:'汽車用高強度螺栓'}",
           "{a:'海島度假旅館',b:'海景客房、在地早餐與跳島行程代訂',c:'漁村文化體驗',d:'家庭旅遊與蜜月旅行',e:'台灣本島與港澳旅客',f:'海島度假住宿'}", out)
out = sub1("再生成 3 張不同場景的圖：生產線上、出貨包裝中、裝配在成品上。",
           "再生成 3 張不同場景的圖：主廚出餐的廚房檯面上、客房送餐服務的托盤上、戶外沙灘的野餐墊上。", out)
out = sub1("{sub:'一顆 M12 高強度六角螺栓與配套螺帽',scene:'潔淨的現代化扣件廠品檢台上',style:'寫實商品攝影',light:'柔和的攝影棚側光',comp:'45 度俯視特寫、背景虛化'}",
           "{sub:'一盤澎湖在地海鮮料理與一杯仙人掌冰沙',scene:'海景餐廳靠窗的木質餐桌上',style:'寫實商品攝影',light:'傍晚柔和的自然夕陽光',comp:'45 度俯視特寫、背景虛化'}", out)
out = sub1("{pages:'20',topic:'2026 年度品質改善成果',aud:'經營層',style:'深藍與橘色、使用公司 Logo、字體清楚',goal:'年度報告'}",
           "{pages:'20',topic:'2026 年度住房率與顧客滿意度成果',aud:'經營層',style:'海洋藍與沙色、使用公司 Logo、字體清楚',goal:'年度報告'}", out)

OUT.write_text(out, encoding="utf-8", newline="\n")
print("slides:", len(pat.findall(out)), "bytes:", len(out.encode("utf-8")))

# ---------------------------------------------------------------- leftovers
KW = r"扣件|螺栓|螺絲|螺帽|金屬|熱處理|鍍|模具|產線|品保|製程|8D|MES|稼動|不良率|料號|RFQ|汽車|廠長|外銷|出貨|交期|fastener"
for i, s in enumerate(pat.findall(out), 1):
    t = re.sub(r"<[^>]+>", " ", re.sub(r'src="data:[^"]*"', "", s))
    t += " " + " ".join(re.findall(r'(?:placeholder|value|title)="([^"]*)"', s))
    h = sorted(set(re.findall(KW, t)))
    if h:
        print(f"  leftover slide {i}: {h}")
js = out[out.index("<script>\n(function(){"):]
print("  leftover JS:", sorted(set(re.findall(KW, js))))
