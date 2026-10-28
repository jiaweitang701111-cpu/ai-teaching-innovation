# -*- coding: utf-8 -*-
"""第四輪（最後）調整（2026-10-29 使用者 5 項＋全面檢查修正）。
輸入：已上線的 110 頁版本（git commit c430b9e 的 index.html），頁碼一律指 110 頁版本。
"""
import re, sys, io, pathlib, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BASE_COMMIT = "c430b9e"

doc = subprocess.check_output(["git", "-C", str(ROOT), "show", f"{BASE_COMMIT}:index.html"]).decode("utf-8")
pat = re.compile(r"<section\b.*?</section>", re.S)
ms = list(pat.finditer(doc))
assert len(ms) == 110, len(ms)
head, tail = doc[:ms[0].start()], doc[ms[-1].end():]
S = {i + 1: m.group(0) for i, m in enumerate(ms)}

def sub(p, old, new, n=1):
    c = S[p].count(old)
    assert c == n, f"p{p}: found {c}x (want {n}): {old[:60]}"
    S[p] = S[p].replace(old, new)

def cell(p, old, new):
    """只換整段 span 文字完全相同者（避免 US$1 誤中 US$10）"""
    sub(p, f">{old}</span>", f">{new}</span>")

# 3 第 70 頁：拿掉「範本（assets/）」一行
sub(70, '<p class="p13"><span class="r15">範本（assets/）：</span><span class="r10">飯店品牌色票與標誌使用規範</span></p>', "")

# 4 第 73 頁：比照第 60 頁的部份封面版型
S[73] = ('<section class="s bn" data-src="501" data-t="Claude 功能與使用全攻略">'
 '<i class="e" style="left:85.3px;top:247.7px;width:106.7px;height:5.3px;background:#F0A35E;border-radius:999px"></i>'
 '<div class="e tb" style="left:85.3px;top:279.7px;width:1142.7px;height:34.4px;--t:1;--x:0.888"><div class="ti"><p class="p0"><span class="r0">第六部份</span></p></div></div>'
 '<div class="e tb" style="left:85.3px;top:338px;width:1142.7px;height:76.3px;--t:1;--x:0.000"><div class="ti"><p class="p1"><span class="r1">Claude 功能與使用全攻略</span></p></div></div>'
 '<div class="e tb" style="left:85.3px;top:438.3px;width:1030px;height:96.4px"><div class="ti"><p class="p48"><span class="r16">'
 'Claude 核心功能｜Chat、Cowork、Code 三模式｜模型與方案怎麼選｜Cowork 數位同事｜用 Cowork 做簡報</span></p></div></div></section>')
S[73] = S[73].replace('left:85.3px;top:438.3px;width:1030px;height:96.4px', 'left:85.3px;top:438.3px;width:1142.7px;height:96.4px')

# 全面檢查修正：第 57 頁卡片 6 文字超出卡片
sub(57, "「請幫我把『標準雙人房、海景家庭房與蜜月套房』三種住房方案做成視覺化比較表，欄位包含房型坪數、早餐與加值服務、適合客群與價格帶，使用圖示與重點標示，讓旅客更容易閱讀。」",
         "「請幫我把『標準雙人房、海景家庭房與蜜月套房』做成視覺化比較表，欄位包含坪數、早餐與加值服務、適合客群與價格帶，使用圖示與重點標示，讓旅客更容易閱讀。」")

# 5 第六部份：拿掉「單元一～五」，各單元封面改為置中
for p in range(74, 110):
    S[p] = re.sub(r"第六部份｜單元[一二三四五](｜| )", "第六部份｜", S[p])

def unit(src, title, lines, sub_, desc=""):
    """單元封面：比照第 73 頁（部份封面）的左對齊版型；標題兩行時整組上移一行"""
    up = 73.6 * (len(lines) - 1)
    t = lambda y: f"{y - up:.1f}"
    h1 = "".join(f'<p class="p1"><span class="r1">{l}</span></p>' for l in lines)
    d = (f'<div class="e tb" style="left:85.3px;top:484px;width:1142.7px;height:96px"><div class="ti">'
         f'<p class="p2"><span class="r14">{desc}</span></p></div></div>') if desc else ""
    return (f'<section class="s bn" data-src="{src}" data-t="{title}">'
            f'<i class="e" style="left:85.3px;top:{t(247.7)}px;width:106.7px;height:5.3px;background:#F0A35E;border-radius:999px"></i>'
            f'<div class="e tb" style="left:85.3px;top:{t(279.7)}px;width:1142.7px;height:34.4px;--t:1;--x:0.888"><div class="ti"><p class="p0"><span class="r0">第六部份</span></p></div></div>'
            f'<div class="e tb" style="left:85.3px;top:{t(338)}px;width:1142.7px;height:{76.3 + up:.1f}px;--t:1;--x:0.000"><div class="ti">{h1}</div></div>'
            f'<div class="e tb" style="left:85.3px;top:438.3px;width:1142.7px;height:40px"><div class="ti"><p class="p48"><span class="r16">{sub_}</span></p></div></div>'
            f'{d}</section>')
S[85] = unit("513", "Claude 三模式： Chat、Cowork、Code", ["Claude 三模式：", "Chat、Cowork、Code"],
             "一張表看懂三種使用方式與適合對象",
             "同一個 Claude 模型、三種工作方式：2023 年的 Chat、2025 年 2 月的 Claude Code、2026 年 1 月的 Cowork；2026 年 9 月起 Chat 與 Cowork 合併為同一對話入口。理解三者的分工，才能依角色與任務發揮 AI 的效益")
S[92] = unit("519", "Claude 模型怎麼選？", ["Claude 模型怎麼選？"],
             "Fable 5.1、Opus 5.5、Sonnet 5.5、Haiku 5.5 一表看懂",
             "模型陣容為四個層級，由快到強依序是 Haiku 5.5、Sonnet 5.5、Opus 5.5 與 Fable 5.1；2026 年 9 月下旬起陸續推出的 Claude 5.5 系列在提升效能的同時降低使用成本。最貴與最便宜的輸出成本相差 100 倍，依任務複雜度切換模型，才能兼顧品質與成本")
S[100] = unit("528", "Claude Cowork： 會替你做事的數位同事", ["Claude Cowork：", "會替你做事的數位同事"],
              "定義、核心差異、開始使用與 5 個實戰場景",
              "Cowork 能存取本機檔案，先制定計畫、再自動執行並動態回報；從整理資料夾、提取文件重點到自動產出報帳表格，「AI 不只講道理，而是真的幫你幹活」")
S[106] = unit("534", "用 Cowork 做出 100 頁簡報", ["用 Cowork 做出 100 頁簡報"], "可編輯的 .pptx，5 個步驟")

# 全面檢查修正：Claude Haiku 5.5 已於 2026-10-07 推出（官方模型文件，2026-10-29 查證）
sub(94, ">Claude Haiku 4.5</span>", ">Claude Haiku 5.5</span>")
sub(94, "發布時間：2025 年 10 月", "發布時間：2026 年 10 月 7 日")
sub(94, "回應最快、單次成本最低，定位是「以最經濟的價格取得接近前沿效能」；同樣支援延伸思考，需基本推理的場景表現可圈可點。官方已預告將推出 Haiku 5.5，推出時間以官方公告為準。",
         "回應最快、單次成本最低，專為大量且講求速度的任務設計，例如分類、資料擷取與分流；是第一款支援自適應思考與 effort 參數的 Haiku，上下文擴大到 1M tokens。")
sub(94, "輸入 1／輸出 5 美元。", "輸入 0.1／輸出 0.5 美元起。")
sub(94, "2026.10.05 查核更新", "2026.10.29 查核更新")
cell(95, "Haiku 4.5", "Haiku 5.5")
cell(95, "2025 年 10 月", "2026 年 10 月 7 日")
cell(95, "即時互動、批次處理、原型開發", "即時互動、大量批次、子代理任務")
cell(95, "手動延伸思考", "自適應思考（預設啟用）")
cell(95, "200K／64K Tokens", "1M／128K Tokens")
cell(95, "US$1", "US$0.1 起")
cell(95, "US$5", "US$0.5 起")
sub(95, "資料截至 2026.10.05", "資料截至 2026.10.29")
sub(95, "2026.10.05 查核更新", "2026.10.29 查核更新")
# ChatGPT Work 的驅動模型（OpenAI Deployment Safety Hub：Work 使用 GPT-6 系列）
cell(44, "GPT-5.6", "GPT-6 系列")

out = head + "\n".join(S[p] for p in range(1, 111)) + tail
i = out.index("</style>")
out = out[:i] + (HERE / "style.css").read_text(encoding="utf-8") + out[i:]
(ROOT / "index.html").write_text(out, encoding="utf-8", newline="\n")
secs = pat.findall(out)
print("slides:", len(secs), "bytes:", len(out.encode("utf-8")))
assert "單元一" not in out and "單元五" not in out and "Haiku 4.5" not in "".join(secs)
