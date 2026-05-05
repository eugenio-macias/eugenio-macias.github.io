---
layout: default
title: Home
---

<!-- Background FX -->
<canvas id="stars" aria-hidden="true"></canvas>
<div class="aurora" aria-hidden="true"></div>
<div class="spotlight" aria-hidden="true"></div>

<!-- ===== HERO ===== -->
<section class="hero">
  <div class="hero-orb hero-orb1" aria-hidden="true"></div>
  <div class="hero-orb hero-orb2" aria-hidden="true"></div>
  <div class="hero-inner">

    <!-- Profile -->
    <div class="pfp-wrap" data-tilt data-magnetic>
      <picture>
        <source type="image/heic" srcset="{{ site.baseurl }}/assets/images/profile_pic.jpg" />
        <source type="image/webp" srcset="{{ site.baseurl }}/assets/images/profile_pic.jpg" />
        <source type="image/jpeg" srcset="{{ site.baseurl }}/assets/images/profile_pic.jpg" />
        <img class="profile-pic"
             src="{{ site.baseurl }}/assets/images/profile_pic.jpg"
             alt="Profile picture">
      </picture>
      <div class="ring"></div>
    </div>

    <!-- Intro -->
    <div class="intro">
      <div class="hero-name" aria-label="Eugenio Macías Orozco">
        <span class="hn-main">Eugenio Macías Orozco</span>
        <span class="hn-gl1" aria-hidden="true">Eugenio Macías Orozco</span>
        <span class="hn-gl2" aria-hidden="true">Eugenio Macías Orozco</span>
      </div>
      <h1 class="title">
        <span class="badge">BS Applied Mathematics–Computer Science (Honors) & BA Mathematics</span>
      </h1>

      <p class="typing" aria-label="Probability × Statistics × PDEs × ML">
        <span>Probability × Statistics × PDEs × ML</span>
      </p>

      <!-- About -->
      <article class="glass about" data-tilt data-magnetic>
        <h2>About me</h2>
        <div class="text-bg">
          <p>
            I'm from <strong>Mexico</strong>, graduating May 2026 from Brown University with a
            <strong>BS in Applied Mathematics–Computer Science (Honors)</strong> and a <strong>BA in Mathematics</strong>.
            After Brown I'm heading to <strong>New York City</strong> — excited to join its quant finance,
            ML research, and startup ecosystems. My work focuses on learning dynamical laws from imperfect data:
            <strong>probability-theory-grounded ML for PDEs</strong>, <strong>Reinforcement Learning</strong>,
            <strong>Physics-Informed Deep Learning</strong>, and <strong>Uncertainty Quantification</strong>.
            My honors thesis (Advisor: Prof. Björn Sandstede) builds
            <strong>shift-aligned reduced-order models</strong> (POD + MVAR/LSTM) and
            <strong>WSINDy weak-form PDE discovery</strong> for collective agent dynamics.
            I also researched self-scaled quasi-Newton optimizers for PINNs (Karniadakis Lab)
            and curiosity-driven transfer learning with Prof. George Konidaris.
          </p>
          <p style="margin:.6rem 0 0;">
            Beyond the math, I'm a devoted traveller — <strong>45 countries</strong> across Europe,
            Asia, Latin America, the Middle East, and Africa, with many more ahead.
            My IB at <strong>UWC Mostar</strong> (Bosnia &amp; Herzegovina) sparked a lifelong love
            for cultural immersion. I speak <strong>Spanish</strong> (native), <strong>English</strong>
            (fluent), conversational <strong>French</strong>, and a few words of Bosnian.
            Wherever I land, I head straight for the food markets:
            mole negro in Oaxaca, ćevapi in Sarajevo, dumplings in Chengdu, tagine in Marrakech.
          </p>
          <p style="margin:.6rem 0 0;">
            I play <strong>classical guitar &amp; flamenco</strong> — the interplay of rhythm,
            tension, and mathematical structure is endlessly fascinating. I'm also a competitive
            <strong>♟ chess</strong> player (2070 ELO) and have run <strong>5 marathons</strong>.
          </p>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- ===== FULL-BLEED HIGHLIGHTS ===== -->
<section class="highlights-bleed">
  <div class="highlights-inner">
    <h2 class="section-title">Highlights</h2>

    <div class="cards">
      <!-- Citi Markets -->
      <article class="card glow tilt-card" data-tilt data-magnetic>
        <header>Citi Markets — Quantitative Analyst Intern (NYC, Summer 2025)</header>
        <ul>
          <li>Built <strong>Python–C++ Monte Carlo & PDE solvers</strong>; validated pricing/Greeks and accelerated runtimes.</li>
          <li>Trained <strong>LightGBM-DART</strong> & <strong>neural nets</strong> with Bayesian optimization on <strong>6M+ structured-note</strong> rows; used <strong>SHAP</strong> for diagnostics.</li>
          <li><strong>1st place</strong> out of 540 in the firm-wide ML Quant competition.</li>
        </ul>
      </article>

      <!-- DE Shaw / Bridgewater / Buddywise -->
      <article class="card tilt-card" data-tilt data-magnetic>
        <header>D. E. Shaw · Bridgewater · Buddywise</header>
        <ul>
          <li><strong>Latitude Fellowship</strong> at The D. E. Shaw Group (NYC): multivariate time-series & sector forecasting.</li>
          <li><strong>Investment Immersion</strong> at Bridgewater Associates: macro indicators & stat-arb backtests.</li>
          <li>Intern at <strong>Buddywise</strong> (Berlin): data tooling for safety-critical computer vision.</li>
        </ul>
      </article>

      <!-- Current paths -->
      <article class="card tilt-card" data-tilt data-magnetic>
        <header>What I’m pursuing</header>
        <ul>
          <li><strong>Option</strong> A: <em>MSc in Mathematical Statistics / Applied Mathematics</em>.</li>
          <li><strong>Option</strong> B: <em>Quant full-time</em> (research / trading / developer) starting 2026.</li>
          <li><strong>Option</strong> C: <em>AI startup with my brother</em> — applied ML systems & decision-intelligence tooling.</li>
        </ul>
        <div class="badges">
          <span class="badge">Quant</span><span class="badge">Stat ML</span><span class="badge">PDEs</span>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- Floating Math Symbols (toggle layer) -->
<div id="symbolLayer" class="symbol-layer" aria-hidden="true"></div>
<!-- Particle explosions -->
<div id="boomLayer" class="boom-layer" aria-hidden="true"></div>

<!-- Top-right toggle button -->
<button id="coolBtn" class="cool-btn" type="button" aria-pressed="false" title="Toggle floating math">
  ✨ Click Here!
</button>

<style>
  :root{
    --bg:#0a0b0e; --ink:#ffffff; --muted:#e5e7eb; --line:#23262d; --card:#0f1115;
    --g1:#7c83ff; --g2:#22d3ee; --g3:#34d399; --g4:#f59e0b;
    --shadow:0 24px 60px rgba(0,0,0,.55);
    --mouse-x: 50%; --mouse-y: 50%;
  }
  html{ scroll-behavior:smooth; }
  body { background: transparent; color: var(--ink); overflow-x:hidden; }

  /* Stars, Aurora, Spotlight */
  #stars{ position:fixed; inset:0; width:100%; height:100%; z-index:-3; display:block; }
  .aurora{
    position:fixed; inset:-10vmax; z-index:-2; pointer-events:none;
    filter: blur(55px) saturate(120%);
    background:
      radial-gradient(60% 50% at 20% 20%, rgba(124,131,255,.18), transparent 60%),
      radial-gradient(45% 40% at 80% 30%, rgba(34,211,238,.14), transparent 60%),
      radial-gradient(55% 45% at 50% 75%, rgba(52,211,153,.12), transparent 70%),
      conic-gradient(from 210deg at 50% 50%, rgba(245,158,11,.10), transparent 70%);
    animation: drift 22s ease-in-out infinite alternate;
    will-change: transform;
  }
  @keyframes drift{ 0%{ transform: translate3d(0,0,0) scale(1); } 100%{ transform: translate3d(2vw,-1vh,0) scale(1.04); } }
  .spotlight {
    position: fixed; inset: 0; z-index: -1; pointer-events: none;
    background: radial-gradient(circle at var(--mouse-x) var(--mouse-y), rgba(255, 255, 255, 0.045), transparent 35%);
  }

  /* Hero */
  .hero{ position:relative; padding: clamp(20px, 4.5vw, 40px) 16px; padding-bottom: clamp(8px, 2vw, 10px); }
  .hero-inner{
    max-width:min(1400px, 94vw);
    margin:0 auto;
    display:grid; grid-template-columns:1fr; gap:18px; align-items:flex-start;
  }
  @media (min-width:980px){
    .hero-inner{ grid-template-columns:.95fr 1.65fr; gap:28px; }
  }

  /* Profile */
  .pfp-wrap{
    position:relative; width:min(360px,78vw); aspect-ratio:1/1; margin:0 auto;
    border-radius:24px; overflow:hidden; border:1px solid var(--line);
    background: linear-gradient(145deg, rgba(255,255,255,.04), rgba(255,255,255,.01));
    box-shadow:var(--shadow); transform-style:preserve-3d;
    transition:transform .25s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    will-change: transform;
  }
  .profile-pic{ width:100%; height:100%; object-fit:cover; display:block; opacity:.98; transform:scale(1.02); transition:transform .35s ease, opacity .35s ease; }
  .pfp-wrap:hover .profile-pic{ transform:scale(1.06); opacity:1; }
  .ring{
    position:absolute; inset:0; pointer-events:none;
    background: conic-gradient(from 180deg, var(--g1), var(--g2), var(--g3), var(--g1));
    mask: radial-gradient(farthest-side, transparent calc(100% - 6px), #000 0);
    mix-blend-mode: screen; opacity:.38; animation: spin 10s linear infinite;
  }
  @keyframes spin { to { transform: rotate(360deg); } }

  /* Intro */
  .intro{ position:relative; }
  .title{ margin:0 0 .35rem; font-size:clamp(1.6rem,3.2vw,2.2rem); line-height:1.08; color:var(--ink); }
  .title::after{ content:""; display:block; height:2px; width:86px; margin-top:.4rem; background:linear-gradient(90deg,var(--g1),var(--g2),var(--g3)); border-radius:2px; }
  .badge{ display:inline-block; font-size:.92rem; font-weight:700; padding:6px 12px; border-radius:999px; color:#0b1220; background:linear-gradient(90deg,var(--g2),var(--g3)); }

  /* ===== Hero name glitch title ===== */
  .hero-name{
    position:relative; display:block;
    font-size:clamp(2rem,4vw,3rem);
    font-weight:900; letter-spacing:-.5px; line-height:1.1;
    margin:0 0 .55rem;
    background: linear-gradient(90deg, var(--g1), var(--g2), var(--g3), var(--g1));
    background-size: 300% 100%;
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent; color: transparent;
    animation: gradientShift 5s linear infinite;
    filter: drop-shadow(0 0 22px rgba(124,131,255,.45));
  }
  .hn-gl1, .hn-gl2{
    position:absolute; inset:0; pointer-events:none;
    background: inherit; -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent; color: transparent;
    opacity:0;
  }
  .hn-gl1{ animation: glitchA  9s 0s  infinite linear; }
  .hn-gl2{ animation: glitchB 11s 2s  infinite linear; }

  /* ===== Floating light orbs in hero ===== */
  .hero-orb{ position:absolute; border-radius:50%; pointer-events:none; mix-blend-mode:screen; z-index:0; overflow:hidden; }
  .hero-orb1{
    width:440px; height:440px;
    background: radial-gradient(circle at 40% 40%, rgba(124,131,255,.22), transparent 68%);
    top:-100px; right:4%;
    animation: orbFloat1 11s ease-in-out infinite alternate;
  }
  .hero-orb2{
    width:320px; height:320px;
    background: radial-gradient(circle at 60% 60%, rgba(34,211,238,.18), transparent 68%);
    bottom:30px; left:1%;
    animation: orbFloat2 15s ease-in-out infinite alternate;
  }
  @keyframes orbFloat1{
    from{ transform:translate(0,0) scale(1); }
    to  { transform:translate(18px,-28px) scale(1.12); }
  }
  @keyframes orbFloat2{
    from{ transform:translate(0,0) scale(1); }
    to  { transform:translate(-14px,20px) scale(1.1); }
  }

  .typing{ margin:.4rem 0 1.0rem; color:var(--ink); opacity:.95; font-size:clamp(1rem,1.6vw,1.1rem); min-height:1.4em; }
  .typing span{ display:inline-block; white-space:nowrap; overflow:hidden; border-right:2px solid currentColor; animation: typing 3s steps(42,end) infinite alternate, caret 700ms steps(1) infinite; }
  @keyframes typing { from { width: 0; } to { width: 42ch; } }
  @keyframes caret { 50% { border-color: transparent; } }

  .glass{ background: linear-gradient(180deg, rgba(255,255,255,.08), rgba(255,255,255,.04)); border:1px solid var(--line); border-radius:16px; padding:18px 20px; box-shadow:var(--shadow); backdrop-filter: blur(8px); transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease; }
  .glass:hover{ transform: translateY(-2px) rotateX(1deg); border-color:#2a2f39; box-shadow:0 24px 60px rgba(0,0,0,.35); }
  .about h2{ margin:.2rem 0 .5rem; font-size:1.15rem; letter-spacing:.2px; color:var(--ink); }
  .text-bg{
    position:relative; padding:12px 14px; border-radius:14px;
    background: linear-gradient(180deg, rgba(124,131,255,.18), rgba(34,211,238,.14) 50%, rgba(52,211,153,.12) 100%);
    border:1px solid #2a2f39;
  }
  .text-bg::before{
    content:""; position:absolute; inset:-1px; border-radius:14px;
    background: conic-gradient(from 0deg, var(--g1), var(--g2), var(--g3), var(--g1));
    filter: blur(14px); opacity:.16; pointer-events:none;
  }
  .about p{ margin:0; color:var(--ink); opacity:.98; }

  /* ===== Top-right Cool Button ===== */
  .cool-btn{
    position: fixed; top: 90px; right: 22px; z-index: 6;
    appearance:none; border:1px solid #2a2f39; border-radius:999px;
    padding:10px 16px; font-weight:800; letter-spacing:.2px; cursor:pointer;
    color:#0b1220; background:linear-gradient(90deg,var(--g2),var(--g3));
    transition: transform .15s ease, box-shadow .15s ease, filter .15s ease, opacity .2s ease;
  }
  .cool-btn:hover{ transform: translateY(-2px) scale(1.02); box-shadow: 0 10px 24px rgba(0,0,0,.30); filter:saturate(1.1); }
  .cool-btn[aria-pressed="true"]{ background:linear-gradient(90deg,var(--g1),var(--g2)); }

  /* ===== Full-bleed Highlights ===== */
  .highlights-bleed{
    position:relative; width:100vw;
    left:50%; right:50%;
    margin-left:-50vw; margin-right:-50vw;
    padding: clamp(8px, 2vw, 12px) clamp(10px, 3vw, 22px) clamp(24px, 4vw, 44px);
  }
  .highlights-inner{
    max-width: min(1680px, 96vw);
    margin: 0 auto;
  }
  .section-title{
    margin: 4px 0 14px; font-size:1.22rem; letter-spacing:.2px; color:var(--ink);
  }
  .section-title::after{ content:""; display:block; height:2px; width:86px; margin-top:.35rem; background:linear-gradient(90deg,var(--g1),var(--g2),var(--g3)); border-radius:2px; }

  /* 3 big edge-to-edge cards */
  .cards{
    display:grid;
    grid-template-columns: 1fr;
    gap: clamp(12px, 2vw, 18px);
    perspective:1000px;
  }
  @media (min-width: 900px){
    .cards{ grid-template-columns: repeat(3, minmax(0,1fr)); }
  }
  .card{
    background:var(--card); border:1px solid var(--line); border-radius:18px; padding: clamp(18px, 2vw, 26px);
    color:var(--ink); position:relative; overflow:hidden; font-size:1.08rem;
    min-height: 220px;
    will-change: transform;
    transition: transform .5s cubic-bezier(0.215, 0.610, 0.355, 1), box-shadow .25s ease, border-color .25s ease;
    box-shadow: var(--shadow);
  }
  .card header{ font-weight:900; margin-bottom:10px; color:var(--ink); font-size:1.12rem; }
  .card ul{ margin:.2rem 0 0 1.1rem; }
  .card li{ margin:.42rem 0; color:var(--ink); opacity:.95; line-height:1.42; }
  .card::after{
    content:""; position:absolute; inset:-1px; border-radius:20px; pointer-events:none; opacity:0;
    background: conic-gradient(from 0deg, var(--g1), var(--g2), var(--g3), var(--g1));
    transition: opacity .25s ease; filter: blur(16px);
  }
  .card:hover{
    transform: translateY(-3px) rotateX(0.6deg) rotateY(-0.6deg) scale(1.02);
    border-color:#2a2f39;
  }
  .card:hover::after{ opacity:.25; }
  .card:hover:before{
    content:""; position:absolute; top:0; left:-40%; width:40%; height:100%; transform:skewX(-20deg);
    background: linear-gradient(90deg, transparent, rgba(255,255,255,.10), transparent);
    animation: sheen .9s ease;
  }
  @keyframes sheen{ from{ left:-40%; } to{ left:120%; } }
  .tilt-card:hover{ transform: translateY(-3px) rotateX(1.2deg) rotateY(-1.2deg) scale(1.025); }
  .badges{ margin-top:10px; display:flex; gap:8px; flex-wrap:wrap; }
  .badge{ display:inline-block; font-size:.88rem; font-weight:700; padding:6px 12px; border-radius:999px; color:#0b1220; background:linear-gradient(90deg,var(--g2),var(--g3)); }

  /* Math symbols layer */
  .symbol-layer{ position: fixed; inset: 0; z-index: 4; pointer-events: none; display: none; }
  .symbol-layer.active{ display:block; }
  .symbol{
    position:absolute; pointer-events:auto; user-select:none;
    color: rgba(255,255,255,.92); text-shadow: 0 0 8px rgba(255,255,255,.28);
    font-weight: 900; filter: drop-shadow(0 6px 20px rgba(0,0,0,.35));
    transform: translate3d(0,0,0) rotate(var(--rot,0deg));
    animation: float var(--dur,12s) ease-in-out var(--delay,0s) infinite alternate;
    will-change: transform, opacity, filter;
  }
  @keyframes float{ to{ transform: translate3d(var(--tx, 20px), var(--ty, -30px), 0) rotate(calc(var(--rot,0deg) + 12deg)); } }
  .symbol.pop{ animation: pop .45s ease-out forwards; }
  .symbol.pop::after{
    content:""; position:absolute; inset:-6px; border-radius:999px; border:2px solid rgba(255,255,255,.5);
    animation: ripple .45s ease-out forwards;
  }
  @keyframes pop{
    0%   { transform: scale(1) translateZ(0); opacity:.95; filter: drop-shadow(0 8px 26px rgba(0,0,0,.35)); }
    60%  { transform: scale(1.25) translateZ(0); }
    100% { transform: scale(.3) translateZ(0); opacity:0; filter: drop-shadow(0 0 0 rgba(0,0,0,0)); }
  }
  @keyframes ripple{
    0%   { opacity:.35; transform: scale(1); }
    100% { opacity:0;  transform: scale(1.8); }
  }

  /* Particle explosion */
  .boom-layer{ position: fixed; inset:0; pointer-events:none; z-index: 7; }
  .particle{
    position: absolute; width: 8px; height: 8px; border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, #fff, var(--c1));
    box-shadow: 0 0 14px var(--c1);
    transform: translate(-50%, -50%) translate(0,0) scale(1);
    animation: burst var(--t,700ms) cubic-bezier(.17,.67,.55,1.24) forwards;
  }
  @keyframes burst{
    60%{ transform: translate(-50%, -50%) translate(var(--dx), var(--dy)) scale(1.1); opacity:1; }
    100%{ transform: translate(-50%, -50%) translate(calc(var(--dx) * 1.25), calc(var(--dy) * 1.25)) scale(.1); opacity:0; box-shadow: 0 0 0 transparent; }
  }

  /* ===== Card text legibility ===== */
  .card header {
    color: #ffffff !important;
    font-weight: 900;
    font-size: 1.12rem;
    text-shadow: 0 1px 0 rgba(0,0,0,.85), 0 0 10px rgba(255,255,255,.15);
  }
  .card li {
    color: #ffffff !important;
    opacity: 1 !important;
  }
  .card strong {
    color: #38f0ff !important;
    text-shadow: 0 0 10px rgba(34,211,238,.5) !important;
  }
  .card li em { color: #c4b5fd !important; }

  /* Reduced motion */
  @media (prefers-reduced-motion: reduce){
    .aurora, .ring, .profile-pic, .glass, .card, .symbol, .spotlight, .particle,
    .hero-orb, .hero-name { animation: none !important; transition: none !important; }
    .typing span{ animation: none; border-right: none; }
  }
</style>

<script>
/* ===== Stars ===== */
(function(){
  const canvas = document.getElementById('stars');
  if(!canvas) return;
  const ctx = canvas.getContext('2d', { alpha: true });
  let w, h, dpr = Math.min(window.devicePixelRatio || 1, 1.35);
  let stars = [], N = 120;
  let paused = false;
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function resize(){
    w = canvas.width  = Math.floor(innerWidth * dpr);
    h = canvas.height = Math.floor(innerHeight * dpr);
    canvas.style.width = innerWidth + 'px';
    canvas.style.height = innerHeight + 'px';
    spawn();
  }
  function rnd(a,b){ return a + Math.random()*(b-a); }
  function spawn(){
    stars = Array.from({length: N}, ()=>({
      x: rnd(0, w), y: rnd(0, h),
      r: rnd(0.4, 1.6)*dpr, a: rnd(.3,.9),
      vx: rnd(-.02,.02)*dpr, vy: rnd(.02,.10)*dpr
    }));
  }
  function draw(){
    ctx.clearRect(0,0,w,h);
    ctx.save(); ctx.globalCompositeOperation = 'lighter';
    for(const s of stars){
      ctx.globalAlpha = s.a;
      ctx.fillStyle = '#ffffff';
      ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI*2); ctx.fill();
    }
    ctx.restore();
  }
  function update(){
    for(const s of stars){
      s.x += s.vx; s.y += s.vy;
      if(s.x < -5 || s.x > w+5 || s.y > h+5) { s.x = rnd(0,w); s.y = -5; }
    }
  }
  function step(){ draw(); if(!paused) update(); if(!reduce) requestAnimationFrame(step); }
  addEventListener('scroll', ()=>{ paused = (scrollY > innerHeight * 0.7); }, { passive:true });
  addEventListener('resize', resize, { passive: true });
  resize(); if(!reduce) step();
})();

/* ===== 3D Tilt (gentle) ===== */
(function(){
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduce) return;
  document.querySelectorAll('[data-tilt]').forEach(el=>{
    const r = el.hasAttribute('data-magnetic') ? 3 : 8;
    const m = el.hasAttribute('data-magnetic') ? 0.15 : 0;
    el.addEventListener('mousemove', (e)=>{
      const b = el.getBoundingClientRect();
      const cx = b.left + b.width / 2, cy = b.top + b.height / 2;
      const dx = (e.clientX - cx) / (b.width / 2);
      const dy = (e.clientY - cy) / (b.height / 2);
      const tx = dx * b.width * m, ty = dy * b.height * m;
      el.style.transform = `translate3d(${tx}px, ${ty}px, 0) rotateX(${(-dy*r).toFixed(2)}deg) rotateY(${(dx*r).toFixed(2)}deg)`;
    });
    el.addEventListener('mouseleave', ()=>{ el.style.transform = ''; });
  });
})();

/* ===== Floating Math Symbols (toggle + pop) ===== */
(function(){
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const layer = document.getElementById('symbolLayer');
  const btn = document.getElementById('coolBtn');
  if(!layer || !btn) return;

  const SYMBOLS = ["∑","∫","π","ℝ","ℂ","ℕ","∇","∂","λ","μ","σ","ϕ","ψ","ε","δ","Θ","∞","≈","≡","⊗","⊕","→","↦","∀","∃","𝔼","𝒩","√","≤","≥"];
  const MIN = 18, MAX = 42;
  const ACTIVE_COUNT = 40;

  function rand(a,b){ return a + Math.random()*(b-a); }
  function choose(arr){ return arr[Math.floor(Math.random()*arr.length)]; }

  function spawnOne(){
    const s = document.createElement('span');
    s.className = 'symbol';
    s.textContent = choose(SYMBOLS);
    const size = rand(MIN, MAX);
    const x = rand(0, window.innerWidth - size);
    const y = rand(0, window.innerHeight - size);

    s.style.left = x + 'px';
    s.style.top  = y + 'px';
    s.style.fontSize = size + 'px';
    const tx = (Math.random() > .5 ? 1 : -1) * rand(20, 140);
    const ty = (Math.random() > .5 ? 1 : -1) * rand(20, 140);
    const rot = rand(-18, 18) + 'deg';
    const dur = rand(9, 16) + 's';
    const delay = rand(-4, 2) + 's';
    s.style.setProperty('--tx', tx + 'px');
    s.style.setProperty('--ty', ty + 'px');
    s.style.setProperty('--rot', rot);
    s.style.setProperty('--dur', dur);
    s.style.setProperty('--delay', delay);
    s.addEventListener('mouseenter', ()=>{
      if(reduce) return;
      s.classList.add('pop');
      s.addEventListener('animationend', function handler(){
        s.classList.remove('pop');
        s.style.left = rand(0, window.innerWidth - size) + 'px';
        s.style.top  = rand(0, window.innerHeight - size) + 'px';
        s.textContent = choose(SYMBOLS);
        s.removeEventListener('animationend', handler);
      });
    });
    layer.appendChild(s);
  }
  function spawnMany(n){ for(let i=0;i<n;i++) spawnOne(); }

  let active = false;
  btn.addEventListener('click', (e)=>{
    // Toggle state
    active = !active;
    btn.setAttribute('aria-pressed', String(active));

    // Explosion at click point
    boom(e.clientX || innerWidth-40, e.clientY || 100);

    if(active){
      layer.classList.add('active');
      layer.innerHTML = '';
      spawnMany(ACTIVE_COUNT);
      btn.textContent = '✨ Hide Math';
    }else{
      layer.classList.remove('active');
      layer.innerHTML = '';
      btn.textContent = '✨ Cool Math';
    }
  });

  addEventListener('resize', ()=>{
    if(!active) return;
    const syms = layer.querySelectorAll('.symbol');
    syms.forEach(s=>{
      const size = parseFloat(s.style.fontSize) || 24;
      s.style.left = Math.min(parseFloat(s.style.left)||0, innerWidth - size) + 'px';
      s.style.top  = Math.min(parseFloat(s.style.top)||0, innerHeight - size) + 'px';
    });
  });

  /* Particle boom */
  const boomLayer = document.getElementById('boomLayer');
  function boom(x, y){
    if(!boomLayer) return;
    const n = 36;
    for(let i=0;i<n;i++){
      const p = document.createElement('span');
      p.className = 'particle';
      const ang = (Math.PI * 2) * (i / n) + Math.random() * 0.5;
      const dist = 40 + Math.random() * 140;
      const dx = Math.cos(ang) * dist;
      const dy = Math.sin(ang) * dist;
      const t  = 500 + Math.random()*500;

      // random accent color
      const palette = ['#7c83ff','#22d3ee','#34d399','#f59e0b','#ffffff'];
      const c1 = palette[Math.floor(Math.random()*palette.length)];

      p.style.left = x + 'px';
      p.style.top  = y + 'px';
      p.style.setProperty('--dx', dx + 'px');
      p.style.setProperty('--dy', dy + 'px');
      p.style.setProperty('--t', t + 'ms');
      p.style.setProperty('--c1', c1);

      p.addEventListener('animationend', ()=> p.remove());
      boomLayer.appendChild(p);
    }
  }
})();

/* ===== Spotlight Cursor ===== */
(function() {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) return;
  window.addEventListener('mousemove', (e) => {
    document.documentElement.style.setProperty('--mouse-x', e.clientX + 'px');
    document.documentElement.style.setProperty('--mouse-y', e.clientY + 'px');
  }, {passive:true});
})();

/* ===== Hero name scramble ===== */
(function(){
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduce) return;
  const el = document.querySelector('.hn-main');
  if(!el) return;
  const CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ∑∫∂∇αβγδεζθλμπσφψω#$%01289';
  function scramble(){
    const orig = el.dataset.orig || el.textContent;
    el.dataset.orig = orig;
    let f = 0; const total = orig.length * 2;
    const iv = setInterval(()=>{
      el.textContent = orig.split('').map((ch, i)=>{
        if(ch === ' ') return ch;
        return i < ((f/2)|0) ? ch : CHARS[Math.floor(Math.random()*CHARS.length)];
      }).join('');
      if(++f >= total){ el.textContent = orig; clearInterval(iv); }
    }, 14);
  }
  setTimeout(scramble, 500);
  setInterval(scramble, 10000);
})();
</script>
