<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Guruprasad GP — Profile</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Sora:wght@300;400;600;700&display=swap" rel="stylesheet"/>
  <style>
    *{box-sizing:border-box;margin:0;padding:0}
    :root{
      --rose:#bf616a;--pine:#31748f;--foam:#9ccfd8;--gold:#f6c177;
      --love:#eb6f92;--iris:#c4a7e7;--muted:#6e6a86;
      --base:#faf4ed;--surface:#fffaf3;--overlay:#f2e9de;
      --text:#575279;--subtle:#797593;
      --wa:#25D366;--wa-dark:#128C7E;
    }
    body{font-family:'Sora',sans-serif;background:var(--base);color:var(--text);min-height:100vh}

    .profile{max-width:860px;margin:0 auto;padding:2.5rem 1.5rem}

    /* HERO */
    .hero{text-align:center;padding:2.5rem 1rem 2rem;position:relative;overflow:hidden}
    .hero::before{content:'';position:absolute;inset:0;
      background:radial-gradient(ellipse at 30% 20%,rgba(196,167,231,.15) 0%,transparent 60%),
                radial-gradient(ellipse at 70% 80%,rgba(156,207,216,.12) 0%,transparent 60%);
      pointer-events:none}
    .hero-gif{width:100%;max-width:520px;height:200px;object-fit:cover;border-radius:12px;border:1px solid var(--overlay)}
    .hero-name{font-size:2.4rem;font-weight:700;color:var(--rose);letter-spacing:-.5px;margin:1.2rem 0 .3rem}
    .hero-sub{font-size:.85rem;color:var(--subtle);font-family:'JetBrains Mono',monospace;letter-spacing:.5px}

    /* SECTIONS */
    .section{margin:2rem 0}
    .section-title{font-size:.65rem;font-weight:600;text-transform:uppercase;letter-spacing:2px;
      color:var(--muted);border-bottom:1px solid var(--overlay);padding-bottom:.5rem;margin-bottom:1rem}

    /* ABOUT */
    .about-grid{display:grid;gap:.65rem}
    .about-item{display:flex;gap:.6rem;align-items:flex-start;font-size:.83rem;line-height:1.55}
    .about-emoji{min-width:1.4rem;font-size:1rem}
    .about-text strong{color:var(--rose);font-weight:600}

    /* FUN FACT */
    .fun-fact{background:linear-gradient(135deg,rgba(196,167,231,.12),rgba(156,207,216,.1));
      border:1px solid var(--iris);border-radius:10px;padding:1rem 1.2rem;
      font-size:.82rem;color:var(--text);line-height:1.6}
    .fun-fact strong{color:var(--iris)}

    /* BADGES */
    .badges-row{display:flex;flex-wrap:wrap;gap:.45rem}
    .badge{display:inline-flex;align-items:center;gap:.35rem;padding:.28rem .7rem;border-radius:6px;
      font-size:.75rem;font-family:'JetBrains Mono',monospace;font-weight:600;text-decoration:none;
      transition:transform .15s,filter .15s;border:1px solid rgba(0,0,0,.08)}
    .badge:hover{transform:translateY(-1px);filter:brightness(1.08)}
    .badge-li{background:#0a66c2;color:#fff}
    .badge-gm{background:#d93025;color:#fff}
    .badge-lc{background:#ffa116;color:#1a1a1a}
    .badge-gfg{background:#2f8d46;color:#fff}
    .badge-nc{background:#ff6b6b;color:#fff}

    /* TECH STACK */
    .tech-group{margin-bottom:1rem}
    .tech-label{font-size:.68rem;color:var(--subtle);font-family:'JetBrains Mono',monospace;
      margin-bottom:.4rem;text-transform:uppercase;letter-spacing:1px}
    .tech-chips{display:flex;flex-wrap:wrap;gap:.35rem}
    .chip{padding:.22rem .55rem;border-radius:5px;font-size:.72rem;font-weight:600;
      font-family:'JetBrains Mono',monospace;border:1px solid}
    .chip-java{background:#fff3e0;color:#e65100;border-color:#ffcc80}
    .chip-py{background:#e8f4f8;color:#1565c0;border-color:#90caf9}
    .chip-js{background:#fffde7;color:#f57f17;border-color:#ffe082}
    .chip-cpp{background:#ede7f6;color:#4527a0;border-color:#ce93d8}
    .chip-html{background:#fbe9e7;color:#bf360c;border-color:#ffab91}
    .chip-css{background:#e3f2fd;color:#1565c0;border-color:#90caf9}
    .chip-spring{background:#e8f5e9;color:#1b5e20;border-color:#a5d6a7}
    .chip-react{background:#e3f2fd;color:#01579b;border-color:#81d4fa}
    .chip-django{background:#e8f5e9;color:#194d33;border-color:#a5d6a7}
    .chip-vue{background:#e8f5e9;color:#2e7d32;border-color:#a5d6a7}
    .chip-node{background:#f9fbe7;color:#558b2f;border-color:#c5e1a5}
    .chip-pg{background:#e3f2fd;color:#1565c0;border-color:#90caf9}
    .chip-mongo{background:#e8f5e9;color:#1b5e20;border-color:#a5d6a7}
    .chip-docker{background:#e3f2fd;color:#0277bd;border-color:#81d4fa}
    .chip-k8s{background:#ede7f6;color:#4527a0;border-color:#ce93d8}
    .chip-fig{background:#fce4ec;color:#880e4f;border-color:#f48fb1}
    .chip-neutral{background:var(--overlay);color:var(--subtle);border-color:#ddd8d0}

    /* STATS */
    .stats-grid{display:grid;grid-template-columns:1fr 1fr;gap:.75rem}
    .stat-card{background:var(--surface);border:1px solid var(--overlay);border-radius:10px;padding:.75rem;text-align:center;overflow:hidden}
    .stat-img{width:100%;border-radius:6px;display:block}
    .stat-full{margin-top:.75rem;background:var(--surface);border:1px solid var(--overlay);border-radius:10px;padding:.75rem;overflow:hidden}

    hr.divider{border:none;border-top:1px solid var(--overlay);margin:2.5rem 0}

    /* WHATSAPP SECTION */
    .wa-section{background:var(--surface);border:1px solid var(--overlay);border-radius:14px;overflow:hidden;box-shadow:0 4px 24px rgba(87,82,121,.07)}
    .wa-header{background:linear-gradient(135deg,var(--wa-dark),var(--wa));padding:1.8rem;text-align:center;color:#fff}
    .wa-icon-circle{width:56px;height:56px;background:rgba(255,255,255,.25);border-radius:50%;
      display:flex;align-items:center;justify-content:center;margin:0 auto .75rem;font-size:1.8rem}
    .wa-header h2{font-size:1.4rem;font-weight:700;margin-bottom:.25rem}
    .wa-header p{font-size:.82rem;opacity:.92}

    .wa-body{padding:1.5rem}

    .form-group{margin-bottom:1.1rem}
    .form-label{display:block;font-size:.7rem;font-weight:600;color:var(--subtle);
      text-transform:uppercase;letter-spacing:.8px;margin-bottom:.4rem}
    .form-input{width:100%;padding:.6rem .9rem;border:1.5px solid var(--overlay);border-radius:8px;
      font-size:.85rem;font-family:'Sora',sans-serif;color:var(--text);background:var(--base);
      transition:border-color .2s,box-shadow .2s;outline:none}
    .form-input:focus{border-color:var(--wa);box-shadow:0 0 0 3px rgba(37,211,102,.12)}
    textarea.form-input{min-height:110px;resize:vertical}

    .char-bar{display:flex;justify-content:flex-end;font-size:.7rem;color:var(--muted);margin-top:.25rem}

    .templates{margin-bottom:1.2rem}
    .templates-label{font-size:.68rem;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin-bottom:.5rem}
    .tpl-btns{display:flex;flex-wrap:wrap;gap:.4rem}
    .tpl-btn{padding:.28rem .7rem;border-radius:6px;font-size:.73rem;cursor:pointer;
      background:var(--base);border:1px solid var(--overlay);color:var(--text);
      transition:border-color .15s,background .15s;font-family:'Sora',sans-serif}
    .tpl-btn:hover{border-color:var(--wa);background:rgba(37,211,102,.06)}

    .wa-btn{width:100%;padding:.8rem;background:linear-gradient(135deg,var(--wa-dark),var(--wa));
      color:#fff;border:none;border-radius:9px;font-size:.95rem;font-weight:700;
      font-family:'Sora',sans-serif;cursor:pointer;display:flex;align-items:center;
      justify-content:center;gap:.5rem;transition:opacity .2s,transform .15s;
      box-shadow:0 6px 20px rgba(37,211,102,.25)}
    .wa-btn:hover{opacity:.92;transform:translateY(-1px)}
    .wa-btn:active{transform:translateY(0)}

    .wa-note{margin-top:.8rem;background:rgba(37,211,102,.08);border-left:3px solid var(--wa);
      border-radius:6px;padding:.55rem .8rem;font-size:.73rem;color:#1b5e20}

    .footer{text-align:center;padding:1.5rem 0 .5rem;font-size:.7rem;
      color:var(--muted);font-family:'JetBrains Mono',monospace}

    @media(max-width:560px){
      .stats-grid{grid-template-columns:1fr}
      .hero-name{font-size:1.8rem}
      .wa-body{padding:1rem}
    }
  </style>
</head>
<body>
<div class="profile">

  <!-- ── HERO ── -->
  <div class="hero">
    <img class="hero-gif"
      src="https://media.giphy.com/media/dWesBcTLavkZuG35MI/giphy.gif"
      alt="coding animation"
      onerror="this.style.display='none'"/>
    <div class="hero-name">Guruprasad GP</div>
    <div class="hero-sub">@ Sony India Software Centre &nbsp;·&nbsp; Spring Boot &nbsp;·&nbsp; React.js &nbsp;·&nbsp; AI/ML</div>
  </div>

  <!-- ── ABOUT ── -->
  <div class="section">
    <div class="section-title">About Me</div>
    <div class="about-grid">
      <div class="about-item">
        <span class="about-emoji">🔭</span>
        <span class="about-text">Working on scalable RESTful APIs &amp; full-stack apps using <strong>Spring Boot &amp; React.js</strong></span>
      </div>
      <div class="about-item">
        <span class="about-emoji">👯</span>
        <span class="about-text">Looking to collaborate on full-stack Java, open source Spring Boot, or AI/ML powered web apps</span>
      </div>
      <div class="about-item">
        <span class="about-emoji">🤝</span>
        <span class="about-text">Seeking help with advanced system design, microservices architecture &amp; deep learning optimization</span>
      </div>
      <div class="about-item">
        <span class="about-emoji">🌱</span>
        <span class="about-text">Currently learning <strong>Spring AI, Generative AI</strong> integration with Java &amp; advanced PostgreSQL performance tuning</span>
      </div>
      <div class="about-item">
        <span class="about-emoji">💬</span>
        <span class="about-text">Ask me about Spring Boot, RESTful API design, PostgreSQL, React.js, Java, or building AI-powered apps</span>
      </div>
    </div>
  </div>

  <!-- ── FUN FACT ── -->
  <div class="fun-fact">
    <strong>⚡ Fun fact:</strong> I built a real-time Rock Paper Scissors game that reads your hand gestures using a webcam and beats you with AI — and it still beats me sometimes!
  </div>

  <!-- ── SOCIALS & PROFILES ── -->
  <div class="section">
    <div class="section-title">Socials &amp; Coding Profiles</div>
    <div class="badges-row">
      <a class="badge badge-li" href="https://linkedin.com/in/guruprasadgp22" target="_blank" rel="noopener">in &nbsp;LinkedIn</a>
      <a class="badge badge-gm" href="mailto:guruprasad6200@gmail.com">✉ &nbsp;Gmail</a>
      <a class="badge badge-lc" href="https://leetcode.com/u/guruprasadgp22/" target="_blank" rel="noopener">⬡ &nbsp;LeetCode</a>
      <a class="badge badge-gfg" href="https://www.geeksforgeeks.org/profile/guruprasadgp22" target="_blank" rel="noopener">◈ &nbsp;GeeksforGeeks</a>
      <a class="badge badge-nc" href="https://neetcode.io/profile" target="_blank" rel="noopener">▶ &nbsp;NeetCode</a>
    </div>
  </div>

  <!-- ── TECH STACK ── -->
  <div class="section">
    <div class="section-title">Tech Stack</div>

    <div class="tech-group">
      <div class="tech-label">Languages</div>
      <div class="tech-chips">
        <span class="chip chip-java">Java</span>
        <span class="chip chip-py">Python</span>
        <span class="chip chip-js">JavaScript</span>
        <span class="chip chip-cpp">C++</span>
        <span class="chip chip-html">HTML5</span>
        <span class="chip chip-css">CSS3</span>
      </div>
    </div>

    <div class="tech-group">
      <div class="tech-label">Frameworks &amp; Libraries</div>
      <div class="tech-chips">
        <span class="chip chip-spring">Spring Boot</span>
        <span class="chip chip-react">React.js</span>
        <span class="chip chip-django">Django</span>
        <span class="chip chip-vue">Vue.js</span>
        <span class="chip chip-node">Node.js</span>
        <span class="chip chip-neutral">Express.js</span>
      </div>
    </div>

    <div class="tech-group">
      <div class="tech-label">Databases &amp; Caching</div>
      <div class="tech-chips">
        <span class="chip chip-pg">PostgreSQL</span>
        <span class="chip chip-mongo">MongoDB</span>
        <span class="chip chip-neutral">MySQL</span>
        <span class="chip chip-neutral">Firebase</span>
      </div>
    </div>

    <div class="tech-group">
      <div class="tech-label">DevOps &amp; Tools</div>
      <div class="tech-chips">
        <span class="chip chip-docker">Docker</span>
        <span class="chip chip-k8s">Kubernetes</span>
        <span class="chip chip-neutral">Git</span>
        <span class="chip chip-neutral">GitHub</span>
        <span class="chip chip-neutral">Postman</span>
        <span class="chip chip-neutral">Apache Tomcat</span>
        <span class="chip chip-fig">Figma</span>
        <span class="chip chip-neutral">Hibernate</span>
        <span class="chip chip-neutral">JWT</span>
        <span class="chip chip-neutral">Netlify</span>
        <span class="chip chip-neutral">Anaconda</span>
      </div>
    </div>
  </div>

  <!-- ── GITHUB STATS ── -->
  <div class="section">
    <div class="section-title">GitHub Stats</div>
    <div class="stats-grid">
      <div class="stat-card">
        <img class="stat-img"
          src="https://github-readme-stats.shion.dev/api?username=guruprasadgp22&theme=rose_pine&hide_border=true&include_all_commits=true&count_private=true"
          alt="GitHub stats"/>
      </div>
      <div class="stat-card">
        <img class="stat-img"
          src="https://github-readme-stats.shion.dev/api/top-langs/?username=guruprasadgp22&theme=rose_pine&hide_border=true&layout=compact"
          alt="Top languages"/>
      </div>
    </div>
    <div class="stat-full">
      <img class="stat-img"
        src="https://streak-stats.demolab.com/?user=guruprasadgp22&theme=rose_pine&hide_border=true"
        alt="Contribution streak"/>
    </div>
    <div class="stat-full">
      <img class="stat-img"
        src="https://github-readme-activity-graph.vercel.app/graph?username=guruprasadgp22&theme=rose-pine&hide_border=true"
        alt="Contribution graph"/>
    </div>
    <div class="stat-full">
      <img class="stat-img"
        src="https://github-profile-trophy.vercel.app/?username=guruprasadgp22&theme=prussian&no-frame=true&no-bg=false&margin-w=4&column=7"
        alt="GitHub trophies"/>
    </div>
    <div class="stat-full">
      <img class="stat-img"
        src="https://github-contributor-stats.vercel.app/api?username=guruprasadgp22&limit=5&theme=merko&combine_all_yearly_contributions=true"
        alt="Top contributed repos"/>
    </div>
  </div>

  <hr class="divider"/>

  <!-- ── WHATSAPP CONTACT FORM ── -->
  <div class="section">
    <div class="section-title">Contact Me</div>
    <div class="wa-section">

      <div class="wa-header">
        <div class="wa-icon-circle">💬</div>
        <h2>Let's Connect!</h2>
        <p>Send me a message on WhatsApp — I'll get back to you as soon as possible.</p>
      </div>

      <div class="wa-body">

        <!-- Quick Templates -->
        <div class="templates">
          <div class="templates-label">📝 Quick Templates</div>
          <div class="tpl-btns">
            <button class="tpl-btn"
              onclick="fillTemplate('Hi Guruprasad, I am interested in collaborating on a Spring Boot project.')">
              💼 Collaboration
            </button>
            <button class="tpl-btn"
              onclick="fillTemplate('Hello, I would like to discuss a freelance opportunity with you.')">
              🚀 Freelance
            </button>
            <button class="tpl-btn"
              onclick="fillTemplate('Hi, I have a question about your portfolio projects.')">
              ❓ Question
            </button>
          </div>
        </div>

        <!-- Name Field -->
        <div class="form-group">
          <label class="form-label" for="wa-name">Your Name</label>
          <input class="form-input" type="text" id="wa-name"
            placeholder="e.g. Ananya Sharma" maxlength="80" autocomplete="name"/>
        </div>

        <!-- Message Field -->
        <div class="form-group">
          <label class="form-label" for="wa-msg">Your Message</label>
          <textarea class="form-input" id="wa-msg"
            placeholder="Tell me about your project or inquiry..." maxlength="500"></textarea>
          <div class="char-bar"><span id="wa-count">0</span> / 500</div>
        </div>

        <!-- Send Button -->
        <button class="wa-btn" id="wa-send-btn" onclick="sendWhatsApp()">
          <span>📱</span> Open in WhatsApp
        </button>

        <div class="wa-note">
          ✓ Your message will open WhatsApp directly. No data is stored on this website.
        </div>

      </div>
    </div>
  </div>

  <div class="footer">
    Proudly created with GPRM &nbsp;·&nbsp; guruprasadgp22
  </div>
</div>

<script>
  /* ── Character counter ── */
  const msgEl   = document.getElementById('wa-msg');
  const countEl = document.getElementById('wa-count');

  msgEl.addEventListener('input', function () {
    countEl.textContent = this.value.length;
  });

  /* ── Fill quick template ── */
  function fillTemplate(text) {
    msgEl.value = text;
    countEl.textContent = text.length;
    document.getElementById('wa-name').focus();
    msgEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  /* ── Send via WhatsApp ── */
  function sendWhatsApp() {
    const name    = document.getElementById('wa-name').value.trim();
    const message = msgEl.value.trim();

    if (!name || !message) {
      alert('Please fill in both your name and message.');
      return;
    }

    /* 🔴 Replace with your real WhatsApp number (country code + digits, no + or spaces) */
    const phoneNumber = '919876543210';

    const fullText     = '*Name:* ' + name + '\n*Message:* ' + message;
    const encodedText  = encodeURIComponent(fullText);
    const whatsappUrl  = 'https://wa.me/' + phoneNumber + '?text=' + encodedText;

    window.open(whatsappUrl, '_blank');

    /* Reset form */
    document.getElementById('wa-name').value = '';
    msgEl.value = '';
    countEl.textContent = '0';
  }
</script>
</body>
</html>
