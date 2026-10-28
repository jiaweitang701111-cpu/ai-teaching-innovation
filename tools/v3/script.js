/* ── 第二輪新增演練：應用場景探索、結構化 Prompt、社群文案、活動企劃 ── */
const joinZh=a=>a.length<=1?(a[0]||''):a.slice(0,-1).join('、')+'與'+a[a.length-1];
(function(){
  const root=$('#ex-scene');if(!root)return;
  const SC={
    train:{role:'餐旅業教育訓練規劃師',out:'教案大綱、練習情境與測驗題（附參考答案）',
      tasks:['生成新人入職的 SOP 教案','製作食品安全與服務禮儀測驗題庫','模擬旅客客訴情境，讓新進員工練習應對','撰寫作業流程變更說明']},
    market:{role:'觀光餐旅產業分析師',out:'重點摘要、數據比較表與三項具體建議',
      tasks:['總結最新觀光產業報告的重點','分析周邊競爭飯店與餐廳的動態','整理線上評論，找出服務改善重點','比較各訂房平台的價格與評價']},
    integ:{role:'餐旅業知識管理顧問',out:'整合表格、負責單位與決策建議',
      tasks:['整合菜單、房型與活動資料，建立旅客問答庫','彙整各部門回饋，提出決策建議','製作跨部門交接與待辦清單','整理旅客常見問題，提供櫃檯與客服使用']}};
  const inp=$('input[data-f=task]',root),tasks=$('.k-tasks',root),out=$('[data-out=main]',root);
  const mk=(v,b)=>v?'<b>'+esc(v)+'</b>':'<u>'+esc(b)+'</u>';
  let sc='train',dept='櫃檯接待';
  function draw(){
    const s=SC[sc],t=inp.value.trim();
    out.innerHTML='你是一位熟悉餐飲旅館業的'+mk(s.role)+'。我在'+mk(dept)+'工作，請協助我'+mk(t,'＿＿（想交給 AI 的任務）')+'。\n'
      +'請依我提供的資料進行；資料不足時，先列出需要補充的問題，不要自行編造。\n'
      +'輸出請用繁體中文，包含'+esc(s.out)+'，最後列出下一步行動。';
    tasks.innerHTML=s.tasks.map(x=>'<button'+(x===t?' class="on"':'')+'>'+esc(x)+'</button>').join('');
  }
  root.addEventListener('click',e=>{
    const b=e.target.closest('button');if(!b)return;
    if(b.parentNode.classList.contains('k-scn')){sc=b.dataset.v;$$('.k-scn button',root).forEach(x=>x.classList.toggle('on',x===b));inp.value=SC[sc].tasks[0];draw();}
    else if(b.parentNode.dataset.pick==='dept'){dept=b.textContent;$$('button',b.parentNode).forEach(x=>x.classList.toggle('on',x===b));draw();}
    else if(b.parentNode===tasks){inp.value=b.textContent;draw();}
    else if(b.dataset.copy){copy(out.textContent,out);}
  });
  inp.addEventListener('input',draw);
  inp.value=SC[sc].tasks[0];draw();
})();
const RULE={'只根據提供資料回答':'只能根據提供的文件、表格或知識庫回答，不要自行推測或編造',
  '資料不足時不推測':'如果資料中沒有提到，請回答「目前資料未提供相關資訊」',
  '附上依據來源':'每個答案都要附上依據來源（文件名稱或條款）',
  '退款、客訴、個資須請主管確認':'涉及退款、客訴、個資或例外處理時，提醒使用者向值班主管確認',
  '回答前自我檢查':'回答前請自行檢查是否有依據、是否過度推論、是否能讓使用者照著執行'};
const FMT={'簡短答案＋操作步驟':'請依「簡短答案、依據來源、操作步驟、注意事項」四段輸出',
  '整理成表格':'請整理成表格：問題｜答案｜依據來源｜是否需要人工確認',
  '中英對照':'請以中英對照方式輸出，方便回覆外籍旅客'};
builder('ex-struct',(v,m)=>({main:'<b>【角色設定】</b>\n你是一位'+m(v.role,'＿＿（角色）')+'，熟悉'+m(v.know,'＿＿（熟悉的領域）')
    +'。你的任務不是自由聊天，而是根據提供資料，協助使用者找到可執行、可檢查、可交接的答案。\n<b>【任務目標】</b>\n請'+m(v.task,'＿＿（要完成的工作）')
    +'。回答內容要讓'+m(v.who,'＿＿（使用對象）')+'可以照著執行，也能讓主管進行確認。\n<b>【執行規範】</b>\n'
    +(v.$rules.length?v.$rules.map(r=>'• '+esc(RULE[r]||r)+'。').join('\n'):'<u>請至少選一項執行規範</u>')
    +'\n• '+esc(FMT[v.fmt]||FMT['簡短答案＋操作步驟'])+'。'}),
  {role:'飯店櫃檯知識助理',know:'訂房規定、入住退房流程、設施使用規範與周邊交通',task:'根據飯店的旅客須知與常見問答，回覆旅客的入住相關問題',who:'櫃檯新進人員'});
builder('ex-social',(v,m)=>({main:'請以一位具有多年經驗的行銷專家及品牌經理，為「'+m(v.biz,'＿＿（店家類型）')+'的'+m(v.theme,'＿＿（節慶）')+'主題活動」撰寫'
    +(v.$plat.length?'<b>'+esc(joinZh(v.$plat))+'</b>':'<u>請選擇平台</u>')+'的文案，包括：'
    +(v.$items.length?'<b>'+esc(v.$items.join('、'))+'</b>':'<u>請選擇輸出項目</u>')+'。\n\n活動主題：一間'+m(v.biz,'＿＿')+'，在'+m(v.theme,'＿＿')
    +'期間推出一個活動，主要針對'+m(v.aud,'＿＿（目標受眾）')+'。活動內容是'+m(v.offer,'＿＿（活動內容）')+'，活動期間從'+m(v.period,'＿＿（活動期間）')+'。'}),
  {biz:'海景飯店',theme:'母親節',aud:'與60歲以上母親同行的家庭旅客',offer:'入住海景雙人房即贈母親節下午茶套餐，並享房價折扣500元',period:'2027年4月24日至5月16日'});
builder('ex-event',(v,m)=>({main:'請以一位具有多年經驗的行銷專家及品牌經理的角色，為慶祝「'+m(v.name,'＿＿（品牌名稱）')+'」'+m(v.theme,'＿＿（慶祝主題）')
    +'，撰寫出「'+m(v.count||'五項','五項')+'」歡慶活動的企劃案。以下為「'+m(v.name,'＿＿')+'」的品牌及商品資訊：\n'
    +'・目標客群：'+m(v.tgt,'＿＿')+'\n・品牌價值：'+m(v.val,'＿＿')+'\n・品牌形象：'+m(v.img,'＿＿')+'\n・市場定位：'+m(v.pos,'＿＿')}),
  {name:'澎科大海景飯店',theme:'開幕十週年紀念',tgt:'25-55歲喜愛海島度假的家庭與情侶旅客',val:'在地海味、友善環境',img:'簡約自然的海島風格，強調在地文化與永續旅行',pos:'中高端度假市場，專注於海景客房與在地體驗行程'});
