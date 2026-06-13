<!-- Beyond Research — personal gallery (Mounted Scrolls).
     To add a photo later: drop the file in assets/img/calligraphy or /swimming
     and copy one <figure class="work"> block, updating src/data-full/title/meta. -->
<div class="beyond">
<style>
  .beyond{
    --purple:#57068c; --purple-d:#3a006b; --orchid:#9c27b0; --soft:#ab82c5;
    --ink:#1a1320; --cinnabar:#c1352b;
    --zh:"Songti SC","STSong","Noto Serif SC",serif;
    color:var(--ink);
  }
  .beyond *{ box-sizing:border-box; }

  /* ---------- hero ---------- */
  .beyond .hero{ display:flex; align-items:center; gap:16px; margin:6px 0 6px; }
  .beyond .hero .bar{ width:5px; align-self:stretch; min-height:64px; border-radius:3px;
    background:linear-gradient(var(--cinnabar),#7d1f18); }
  .beyond .hero .eyebrow{ font-family:'Caveat',cursive; font-size:1.4rem; color:var(--orchid);
    font-weight:600; line-height:1; }
  .beyond .hero h1{ font-size:2.6rem; font-weight:800; margin:2px 0 0; line-height:1;
    background:linear-gradient(90deg,var(--purple-d),var(--orchid) 45%,var(--purple) 72%,var(--purple-d));
    background-size:220% auto; -webkit-background-clip:text; background-clip:text;
    -webkit-text-fill-color:transparent; animation:beyond-shimmer 4s linear infinite; }
  .beyond .lede{ max-width:34em; color:#5e5566; font-size:1rem; line-height:1.6; margin:14px 0 4px; }

  /* ---------- section label ---------- */
  .beyond .sec{ display:flex; align-items:baseline; gap:11px; margin:34px 0 4px; }
  .beyond .sec .en{ font-size:1.3rem; font-weight:700; color:var(--purple); letter-spacing:-.3px; }
  .beyond .sec .zh{ font-family:var(--zh); font-size:.95rem; color:var(--orchid); letter-spacing:.14em; }
  .beyond .sec::after{ content:''; flex:1; height:1px; align-self:center;
    background:linear-gradient(90deg,rgba(87,6,140,.3),transparent); }
  .beyond .seclede{ font-size:.82rem; color:#7a7280; margin:6px 0 18px; }

  /* ---------- mounted scrolls (calligraphy) ---------- */
  .beyond .scrolls{ display:grid; grid-template-columns:repeat(3,1fr); gap:26px; align-items:start; }
  .beyond .scroll{ position:relative; background:linear-gradient(#f3ecf6,#efe6f4);
    border-radius:3px; padding:15px 13px 11px; box-shadow:0 9px 26px rgba(58,0,107,.16);
    cursor:zoom-in; transition:transform .3s cubic-bezier(.2,.7,.2,1), box-shadow .3s; }
  .beyond .scroll::before, .beyond .scroll::after{ content:''; position:absolute; left:-4px; right:-4px;
    height:10px; background:linear-gradient(var(--purple-d),#23004a); border-radius:5px;
    box-shadow:0 2px 6px rgba(0,0,0,.32); }
  .beyond .scroll::before{ top:-4px; } .beyond .scroll::after{ bottom:-4px; }
  .beyond .scroll:hover{ transform:translateY(-5px); box-shadow:0 18px 40px rgba(58,0,107,.28); }
  .beyond .scroll:focus-visible{ outline:3px solid var(--orchid); outline-offset:3px; }
  .beyond .scroll .silk{ background:#fff; border:1px solid rgba(87,6,140,.18); padding:5px; overflow:hidden; }
  .beyond .scroll .silk img{ display:block; width:100%; height:auto;
    transition:transform .55s cubic-bezier(.2,.7,.2,1); }
  .beyond .scroll:hover .silk img{ transform:scale(1.03); }
  .beyond .scroll .cap{ display:flex; align-items:flex-end; justify-content:space-between; gap:8px; margin-top:11px; }
  .beyond .scroll .ttl{ font-size:.86rem; font-weight:600; color:var(--ink); line-height:1.25; }
  .beyond .scroll .meta{ font-family:var(--zh); font-size:.78rem; color:var(--purple); white-space:nowrap; }
  .beyond .seal{ flex:0 0 auto; width:30px; height:30px; border-radius:5px;
    border:2px solid var(--cinnabar); color:var(--cinnabar); font-family:var(--zh); font-weight:700;
    font-size:.82rem; display:flex; align-items:center; justify-content:center; transform:rotate(-4deg);
    box-shadow:inset 0 0 0 1px rgba(193,53,43,.25); }

  /* ---------- swimming ---------- */
  .beyond .swim{ display:grid; grid-template-columns:1fr 1fr; gap:18px; margin-top:6px; }
  .beyond .frame{ position:relative; border-radius:7px; overflow:hidden; cursor:zoom-in;
    box-shadow:0 7px 22px rgba(58,0,107,.15); transition:transform .3s cubic-bezier(.2,.7,.2,1), box-shadow .3s; }
  .beyond .frame:hover{ transform:translateY(-4px); box-shadow:0 16px 38px rgba(58,0,107,.26); }
  .beyond .frame:focus-visible{ outline:3px solid var(--orchid); outline-offset:3px; }
  .beyond .frame img{ display:block; width:100%; height:240px; object-fit:cover;
    transition:transform .55s cubic-bezier(.2,.7,.2,1); }
  .beyond .frame:hover img{ transform:scale(1.04); }
  .beyond .frame .t{ position:absolute; left:0; right:0; bottom:0; padding:24px 14px 11px; color:#fff;
    background:linear-gradient(to top,rgba(20,0,35,.82),transparent); }
  .beyond .frame .t b{ display:block; font-size:.92rem; }
  .beyond .frame .t small{ font-size:.74rem; opacity:.88; }

  /* ---------- lightbox ---------- */
  .beyond-lb{ position:fixed; inset:0; z-index:9998; display:none; align-items:center; justify-content:center;
    background:rgba(18,4,30,.86); backdrop-filter:blur(3px); padding:34px; }
  .beyond-lb.open{ display:flex; }
  .beyond-lb img{ max-width:92vw; max-height:82vh; border-radius:4px; box-shadow:0 20px 60px rgba(0,0,0,.6); }
  .beyond-lb .lbcap{ position:absolute; bottom:20px; left:0; right:0; text-align:center; color:#fff;
    font-size:.9rem; }
  .beyond-lb .lbcap .zh{ font-family:var(--zh); color:#e8c9ff; }
  .beyond-lb .x{ position:absolute; top:18px; right:24px; width:40px; height:40px; border:0; cursor:pointer;
    border-radius:50%; background:rgba(255,255,255,.14); color:#fff; font-size:1.5rem; line-height:1; }
  .beyond-lb .x:hover{ background:rgba(255,255,255,.26); }

  /* ---------- reveal ---------- */
  .beyond .reveal{ opacity:0; transform:translateY(16px); transition:opacity .55s ease, transform .55s ease; }
  .beyond .reveal.vis{ opacity:1; transform:none; }

  @keyframes beyond-shimmer{ 0%{background-position:0% center} 100%{background-position:220% center} }

  /* ---------- responsive ---------- */
  @media (max-width:760px){
    .beyond .scrolls{ grid-template-columns:1fr 1fr; }
    .beyond .hero h1{ font-size:2.1rem; }
  }
  @media (max-width:520px){
    .beyond .scrolls{ grid-template-columns:1fr; }
    .beyond .swim{ grid-template-columns:1fr; }
  }
  @media (prefers-reduced-motion: reduce){
    .beyond .hero h1{ animation:none; }
    .beyond .scroll, .beyond .scroll .silk img, .beyond .frame, .beyond .frame img,
    .beyond .reveal{ transition:none; transform:none; }
    .beyond .reveal{ opacity:1; }
  }

  /* dark mode — keep parity with the home page */
  @media (prefers-color-scheme: dark){
    .beyond{ color:#e9e2ef; }
    .beyond .lede{ color:#c3b8cf; }
    .beyond .scroll{ background:linear-gradient(#2a1140,#23103a); }
    .beyond .scroll .silk{ background:#f7f2fb; }
    .beyond .scroll .ttl{ color:#ece4f3; }
  }
</style>

  <div class="hero">
    <span class="bar" aria-hidden="true"></span>
    <span>
      <span class="eyebrow">an exhibition of —</span>
      <h1>Beyond Research</h1>
    </span>
  </div>
  <p class="lede">Two practices that ask the opposite of a proof: patience with a brush, and
  stubbornness in the water. A small, growing record of both.</p>

  <!-- ===== Calligraphy ===== -->
  <div class="sec reveal"><span class="en">Chinese Calligraphy</span><span class="zh">书法</span></div>
  <p class="seclede reveal">Left to right, the three move forward in time — how the script itself evolved.</p>
  <div class="scrolls">

    <figure class="scroll reveal" tabindex="0" role="button" aria-label="Spring Verses, clerical script — enlarge"
      data-full="{{ '/assets/img/calligraphy/IMG_6331.jpeg' | relative_url }}" data-cap="Spring Verses — Clerical <span class='zh'>隶书</span>">
      <div class="silk"><img src="{{ '/assets/img/calligraphy/IMG_6331.jpeg' | relative_url }}" alt="Clerical script calligraphy, 隶书"></div>
      <figcaption class="cap"><span><span class="ttl">Spring Verses</span></span><span class="meta">隶书</span><span class="seal" aria-hidden="true">趣</span></figcaption>
    </figure>

    <figure class="scroll reveal" tabindex="0" role="button" aria-label="The character 賢, regular script — enlarge"
      data-full="{{ '/assets/img/calligraphy/IMG_3157.jpeg' | relative_url }}" data-cap="賢 &ldquo;the worthy&rdquo; — Regular <span class='zh'>楷书</span>">
      <div class="silk"><img src="{{ '/assets/img/calligraphy/IMG_3157.jpeg' | relative_url }}" alt="The character 賢 in regular script, 楷书"></div>
      <figcaption class="cap"><span><span class="ttl">賢 — &ldquo;the worthy&rdquo;</span></span><span class="meta">楷书</span><span class="seal" aria-hidden="true">趣</span></figcaption>
    </figure>

    <figure class="scroll reveal" tabindex="0" role="button" aria-label="Orchid Pavilion Preface, running script — enlarge"
      data-full="{{ '/assets/img/calligraphy/save-new.jpeg' | relative_url }}" data-cap="Orchid Pavilion Preface — Running <span class='zh'>行书</span>">
      <div class="silk"><img src="{{ '/assets/img/calligraphy/save-new.jpeg' | relative_url }}" alt="Orchid Pavilion Preface in running script, 行书"></div>
      <figcaption class="cap"><span><span class="ttl">Orchid Pavilion Preface</span></span><span class="meta">行书</span><span class="seal" aria-hidden="true">趣</span></figcaption>
    </figure>

  </div>

  <!-- ===== Swimming ===== -->
  <div class="sec reveal"><span class="en">Swimming</span><span class="zh">游泳</span></div>
  <div class="swim">

    <figure class="frame reveal" tabindex="0" role="button" aria-label="Swim team photo, 2016 — enlarge"
      data-full="{{ '/assets/img/swimming/IMG_6769.jpeg' | relative_url }}" data-cap="The Team — Capital University of Economics &amp; Business, 2016">
      <img src="{{ '/assets/img/swimming/IMG_6769.jpeg' | relative_url }}" alt="University swim team group photo, 2016">
      <figcaption class="t"><b>The Team</b><small>Capital Univ. of Economics &amp; Business · 2016</small></figcaption>
    </figure>

    <figure class="frame reveal" tabindex="0" role="button" aria-label="On the podium, 2016 — enlarge"
      data-full="{{ '/assets/img/swimming/IMG_6727.jpeg' | relative_url }}" data-cap="On the Podium — 2016 Beijing Collegiate Swimming Championship">
      <img src="{{ '/assets/img/swimming/IMG_6727.jpeg' | relative_url }}" alt="On the podium with trophy, 2016 championship">
      <figcaption class="t"><b>On the Podium</b><small>2016 Beijing Collegiate Championship</small></figcaption>
    </figure>

  </div>
</div>

<!-- lightbox + reveal -->
<div class="beyond-lb" id="beyondLb" aria-hidden="true">
  <button class="x" id="beyondLbX" aria-label="Close">&times;</button>
  <img id="beyondLbImg" alt="">
  <div class="lbcap" id="beyondLbCap"></div>
</div>
<script>
(function(){
  var lb=document.getElementById('beyondLb'), img=document.getElementById('beyondLbImg'),
      cap=document.getElementById('beyondLbCap'), x=document.getElementById('beyondLbX');
  function open(full,c){ img.src=full; cap.innerHTML=c||''; lb.classList.add('open'); lb.setAttribute('aria-hidden','false'); }
  function close(){ lb.classList.remove('open'); lb.setAttribute('aria-hidden','true'); img.src=''; }
  document.querySelectorAll('.beyond [data-full]').forEach(function(el){
    el.addEventListener('click', function(){ open(el.getAttribute('data-full'), el.getAttribute('data-cap')); });
    el.addEventListener('keydown', function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); open(el.getAttribute('data-full'), el.getAttribute('data-cap')); } });
  });
  x.addEventListener('click', close);
  lb.addEventListener('click', function(e){ if(e.target===lb) close(); });
  document.addEventListener('keydown', function(e){ if(e.key==='Escape' && lb.classList.contains('open')) close(); });

  var io=new IntersectionObserver(function(es){ es.forEach(function(en,i){ if(en.isIntersecting){
    var t=en.target; setTimeout(function(){ t.classList.add('vis'); }, i*60); io.unobserve(t); } }); }, {threshold:.08});
  document.querySelectorAll('.beyond .reveal').forEach(function(el){ io.observe(el); });
})();
</script>
