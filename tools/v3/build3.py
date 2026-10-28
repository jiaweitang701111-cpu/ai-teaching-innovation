# -*- coding: utf-8 -*-
"""第二輪改版（2026-10-28 使用者 33 項調整）。
輸入：已上線的 120 頁版本（git commit b7f4982 的 index.html）
輸出：專案根目錄 index.html
新頁面 HTML 在 slides.html（以 <!--#key--> 分段），新樣式 style.css，新互動 script.js。
頁碼一律指 120 頁版本的頁碼。
"""
import re, sys, io, pathlib, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BASE_COMMIT = "b7f4982"

doc = subprocess.check_output(["git", "-C", str(ROOT), "show", f"{BASE_COMMIT}:index.html"]).decode("utf-8")
pat = re.compile(r"<section\b.*?</section>", re.S)
ms = list(pat.finditer(doc))
assert len(ms) == 120, len(ms)
head, tail = doc[:ms[0].start()], doc[ms[-1].end():]
S = {i + 1: m.group(0) for i, m in enumerate(ms)}

frag = {}
for m in re.finditer(r"<!--#(\w+)-->\s*(<section\b.*?</section>)", (HERE / "slides.html").read_text(encoding="utf-8"), re.S):
    frag[m.group(1)] = m.group(2)
print("fragments:", sorted(frag))

def sub(p, old, new, n=None):
    c = S[p].count(old)
    assert c >= 1 and (n is None or c == n), f"p{p}: found {c}x: {old[:50]}"
    S[p] = S[p].replace(old, new)

# ---------------------------------------------------------------- 原地修改
sub(24, 'class="s cx"', 'class="s cx k-fit24"', 1)                       # 9
for k in ("角色設定", "任務目標", "執行規範"):                              # 10
    sub(25, f"【{k}】範例", f"【{k}】", 1)
sub(33, "運用 ChatGPT 進行文案生成與數據分析", "運用 ChatGPT 進行文案生成", 2)    # 13
sub(33, '<p class="p66"><span class="r69">數據分析實作：數據圖像化、Excel 檔整理、分析與運算，以及營運資料分析的實務建議</span></p>', "", 1)
sub(40, "<button class=\"on\">競爭對手分析</button>",                         # 19
    "<button class=\"on\">競爭對手分析</button><button>市場規模與成長率</button><button>目標客群輪廓</button>"
    "<button>銷售通路與訂房平台</button><button>價格與營收結構</button><button>政策法規影響</button><button>永續與ESG趨勢</button>", 1)
sub(41, '<span class="lab">說明 01</span>', '<span class="lab">說明</span>', 1)  # 20
sub(43, "運用 ChatGPT 進行數據分析與策略擬定", "ChatGPT 數據分析與ChatGPT Work運用", 2)  # 21
sub(43, '<span class="r68">ChatGPT 數據分析與ChatGPT Work運用</span></p>',
    '<span class="r68">ChatGPT 數據分析與</span></p><p class="p65"><span class="r68">ChatGPT Work運用</span></p>', 1)
sub(48, "AI工具應用於營運資料分析的實務建議", "AI工具應用於營運資料分析的注意事項", 2)    # 24
for p in range(49, 57):                                                    # 25
    if "Image 2.0" in S[p]:
        S[p] = S[p].replace("Image 2.0", "Image 2.5")
sub(57, "ChatGPT：Skills 與 Work", "ChatGPT Skills介紹", 2)                 # 27
sub(57, '<p class="p21"><span class="r16">ChatGPT Work：運用生成式AI進行數據分析與策略擬定，從交辦任務到可交付的分析成果</span></p>', "", 1)
for p in range(74, 82):                                                    # 24 Work 頁移到第三部份
    sub(p, "第五部份｜ChatGPT Work", "第三部份｜ChatGPT Work")
sub(116, '<div class="e tb" style="left:85.3px;top:370.2px;width:905.9px;height:83.2px"><div class="ti"><p class="p2"><span class="r14">為什麼不用 Gemini 或 NotebookLM？環境準備、指令五要素、等待期間的注意事項，以及讓每次產出都穩定的兩個習慣</span></p></div></div>', "", 1)  # 30
for n in "123":                                                            # 31
    sub(117, f'<span class="r23">{n}  </span>', "", 1)

# ---------------------------------------------------------------- 換成新版頁面
for p, key in ((3, "s3"), (5, "s5"), (8, "s8"), (12, "s12"), (20, "s20"), (26, "s26"),
               (34, "s34"), (35, "s35"), (36, "s36"), (38, "s38"), (47, "s47"), (115, "s115"), (119, "s119")):
    S[p] = frag[key]
S["34b"], S["35b"] = frag["s34b"], frag["s35b"]

# ---------------------------------------------------------------- 頁序
DROP = {6, 15, 31, 32, 37, 45, 46, 58, 73, 109}          # 37 已併入 36；26 原地換成互動頁
WORK = list(range(74, 82))
order = []
for p in range(1, 121):
    if p in DROP or p in WORK:
        continue
    if 49 <= p <= 56 and p == 49:          # 第四部份前先放 Work（原 74–81 移到原 48 之後）
        order += WORK
    order.append(p)
    if p == 34: order.append("34b")
    if p == 35: order.append("35b")
assert len(order) == len(set(order)) == 112, len(order)
body = "\n".join(S[p] for p in order)
out = head + body + tail

# ---------------------------------------------------------------- 樣式與互動
css = (HERE / "style.css").read_text(encoding="utf-8")
i = out.index("</style>")
out = out[:i] + css + out[i:]
js = (HERE / "script.js").read_text(encoding="utf-8")
i = out.index("/* ── 啟動 ── */")
out = out[:i] + js + "\n" + out[i:]

(ROOT / "index.html").write_text(out, encoding="utf-8", newline="\n")
secs = pat.findall(out)
print("slides:", len(secs), "bytes:", len(out.encode("utf-8")))

# ---------------------------------------------------------------- 檢查
titles = [re.search(r'data-t="([^"]*)"', s).group(1) for s in secs]
for i, (s, t) in enumerate(zip(secs, titles), 1):
    ey = re.search(r"第[一二三四五六七]部份", s)
    print(f"{i:>3} {ey.group(0) if ey else '      '} {t}")
assert "Image 2.0" not in "".join(secs)
assert "第五部份｜ChatGPT Work" not in out
