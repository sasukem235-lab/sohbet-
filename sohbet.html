<!doctype html>

<html lang="tr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>iPhone-styled Chat — Demo</title>
  <style>
    :root{
      --bg:#f2f5f7;
      --phone-bg:linear-gradient(180deg,#0f1724 0%, #071428 100%);
      --bubble-me:#0b93f6;
      --bubble-you:#e5e7eb;
      --glass: rgba(255,255,255,0.06);
      --accent:#34d399;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    html,body{height:100%;margin:0;background:var(--bg);display:grid;place-items:center}/* Phone frame */
.phone{
  width:360px;
  height:720px;
  border-radius:36px;
  padding:20px;
  box-sizing:border-box;
  background:var(--phone-bg);
  box-shadow: 0 30px 60px rgba(2,6,23,0.5), inset 0 -10px 30px rgba(0,0,0,0.4);
  position:relative;
  overflow:hidden;
  transform-origin:center center;
  animation: float 6s ease-in-out infinite;
}
@keyframes float{
  0%{transform: translateY(0) rotate(-1deg)}
  50%{transform: translateY(-8px) rotate(1deg)}
  100%{transform: translateY(0) rotate(-1deg)}
}

/* notch */
.notch{position:absolute;left:50%;transform:translateX(-50%);top:6px;width:160px;height:30px;background:rgba(0,0,0,0.35);border-radius:14px}

/* header */
.top{color:#fff;text-align:center;padding:8px 0;font-weight:600}

/* chat area */
.screen{height:580px;background:linear-gradient(180deg, rgba(255,255,255,0.02), transparent 30%), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200"><g fill="none" stroke="rgba(255,255,255,0.02)" stroke-width="1"><circle cx="100" cy="100" r="60"/><circle cx="40" cy="40" r="20"/><circle cx="160" cy="160" r="10"/></g></svg>') no-repeat right top/180px auto; border-radius:20px; padding:16px; box-sizing:border-box; overflow:auto; scroll-behavior:smooth}

.messages{display:flex;flex-direction:column;gap:12px;padding-bottom:16px}

.msg{max-width:80%;padding:10px 14px;border-radius:18px;line-height:1.2;box-shadow:0 6px 14px rgba(2,6,23,0.35);opacity:0;transform:translateY(18px) scale(0.98);animation:appear .45s forwards cubic-bezier(.22,1,.36,1)}
@keyframes appear{to{opacity:1;transform:none}}

.me{align-self:flex-end;background:linear-gradient(180deg,var(--bubble-me), #005fbf);color:white;border-bottom-right-radius:6px}
.you{align-self:flex-start;background:var(--bubble-you);color:#111;border-bottom-left-radius:6px}

/* subtle typing indicator */
.typing{display:inline-flex;gap:6px;align-items:center;padding:8px 12px;border-radius:16px;background:var(--bubble-you);}
.dot{width:8px;height:8px;border-radius:50%;background:#7b7b7b;opacity:0.85;animation:blink 1s infinite}
.dot:nth-child(2){animation-delay:.15s}
.dot:nth-child(3){animation-delay:.3s}
@keyframes blink{0%,80%{opacity:.15;transform:translateY(0)}40%{opacity:1;transform:translateY(-4px)}}

/* input area */
.composer{display:flex;gap:10px;align-items:center;padding-top:12px}
.input{flex:1;background:rgba(255,255,255,0.06);backdrop-filter:blur(6px);padding:12px 14px;border-radius:999px;color:#fff;border:1px solid rgba(255,255,255,0.03);outline:none}
.btn{background:var(--accent);border:none;padding:10px 14px;border-radius:12px;color:#042;cursor:pointer;font-weight:600}

/* small screens */
@media(max-width:420px){.phone{width:92vw;height:86vh}}

/* message bubble slide-in directions */
.me{animation-name:slide-me, appear;animation-duration:.42s,.45s;animation-timing-function:cubic-bezier(.2,.9,.35,1),cubic-bezier(.22,1,.36,1)}
.you{animation-name:slide-you, appear;animation-duration:.42s,.45s;animation-timing-function:cubic-bezier(.2,.9,.35,1),cubic-bezier(.22,1,.36,1)}
@keyframes slide-me{from{transform:translateX(30px) scale(.98);opacity:0}to{transform:none;opacity:1}}
@keyframes slide-you{from{transform:translateX(-30px) scale(.98);opacity:0}to{transform:none;opacity:1}}

/* small chrome for cursor */
.meta{font-size:12px;color:rgba(255,255,255,0.6);text-align:center;margin-top:8px}

  </style>
</head>
<body>
  <div class="phone" role="application" aria-label="iPhone chat demo">
    <div class="notch"></div>
    <div class="top">Sohbet — iPhone Demo</div><div id="screen" class="screen" aria-live="polite">
  <div class="messages" id="messages"></div>
</div>

<div class="composer">
  <input id="input" class="input" placeholder="Bir şey yaz..." maxlength="360" />
  <button id="send" class="btn">Gönder</button>
</div>
<div class="meta">Yerel demo · Mesajlar tarayıcıda saklanır</div>

  </div>  <script>
    // Basit sohbet demo: yerelde saklama + iPhone benzeri animasyon
    const messagesEl = document.getElementById('messages');
    const inputEl = document.getElementById('input');
    const sendBtn = document.getElementById('send');
    const screen = document.getElementById('screen');

    // yükle
    const STORAGE_KEY = 'iphone-chat-demo-msgs-v1';
    let state = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');

    function render(){
      messagesEl.innerHTML = '';
      state.forEach((m, i) => {
        const el = document.createElement('div');
        el.className = 'msg ' + (m.from === 'me' ? 'me' : 'you');
        el.innerHTML = `<div>${escapeHtml(m.text)}</div>`;
        // staggered animation delay for a more 'live' feel
        el.style.animationDelay = (i * 40) + 'ms';
        messagesEl.appendChild(el);
      });
      // scroll bottom
      requestAnimationFrame(()=> screen.scrollTop = screen.scrollHeight);
    }

    function escapeHtml(str){
      return str.replace(/[&<>"']/g, s => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[s]));
    }

    function pushMessage(text, from = 'me'){
      const msg = {text: text.trim(), from, t: Date.now()};
      state.push(msg);
      if(state.length > 250) state.shift();
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
      render();
    }

    sendBtn.addEventListener('click', send);
    inputEl.addEventListener('keydown', e => { if(e.key === 'Enter') send(); });

    function send(){
      const text = inputEl.value.trim();
      if(!text) return; inputEl.value = '';
      pushMessage(text, 'me');
      // simulate reply with typing indicator + iPhone-style delay
      showTyping(() => {
        const reply = autoReply(text);
        pushMessage(reply, 'you');
      });
    }

    function showTyping(cb){
      const typing = document.createElement('div');
      typing.className = 'msg you';
      typing.innerHTML = `<div class="typing"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>`;
      messagesEl.appendChild(typing);
      screen.scrollTop = screen.scrollHeight;
      // timing scales with message length
      const ms = 700 + Math.min(2500, inputEl.value.length * 60);
      setTimeout(()=>{
        typing.remove(); cb && cb();
      }, ms);
    }

    function autoReply(userText){
      // Çok basit: aynısını yazma + birkaç sabit cevap
      const lower = userText.toLowerCase();
      if(lower.includes('merhaba') || lower.includes('selam')) return 'Merhaba! Nasılsın?';
      if(lower.includes('nerede') || lower.includes('konum')) return 'Ben sanalım, fiziksel bir yerde değilim :)';
      if(lower.includes('github')) return 'GitHub'da nasıl yayınlayacağına yardım edebilirim — repo oluştur, index.html ekle, Pages ayarla.';
      // ters çeviri gibi eğlenceli dönüş
      return userText.split('').reverse().join('').slice(0, 240) + ' — (otomatik cevap)';
    }

    // başlangıç mesajları
    if(state.length === 0){
      pushMessage('Selam! Bu iPhone-stil sohbet demosu. Bir şey yaz ve gönder :)', 'you');
    } else {
      render();
    }

    // küçük UX: tıklayınca input focus
    document.querySelector('.phone').addEventListener('click', e => { if(e.target === screen || e.target === messagesEl) inputEl.focus(); });
  </script></body>
</html>
