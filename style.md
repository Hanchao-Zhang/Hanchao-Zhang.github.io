<style>
  /* === Flex layout for education + research interests === */
  .container-flex {
    display: flex;
    flex-wrap: wrap;
    gap: 24px;
    align-items: flex-start;
  }

  /* === Timeline container === */
  .timeline-container {
    flex: 1;
    min-width: 280px;
    max-width: 800px;
    position: relative;
  }

  .timeline-container h2 {
    margin-bottom: 16px;
  }

  .timeline-line {
    position: absolute;
    top: 70px;
    left: 14px;
    width: 2px;
    height: calc(100% - 136px);
    background: linear-gradient(to bottom, #57068C 0%, rgba(87, 6, 140, 0.12) 100%);
    border-radius: 2px;
  }

  /* === Timeline entries === */
  .timeline-entry {
    position: relative;
    margin-bottom: 18px;
    padding-left: 44px;
  }

  /* [3] Timeline pulse dots */
  .year-circle {
    position: absolute;
    left: 0;
    top: 6px;
    width: 30px;
    height: 30px;
    background: linear-gradient(135deg, #57068C, #9c27b0);
    color: white;
    font-weight: 700;
    font-size: 0.62rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    z-index: 2;
    letter-spacing: -0.5px;
    box-shadow: 0 0 0 3px rgba(87, 6, 140, 0.14), 0 2px 8px rgba(87, 6, 140, 0.28);
  }

  .year-circle::before {
    content: '';
    position: absolute;
    inset: -5px;
    border-radius: 50%;
    border: 2px solid #57068c;
    animation: pulse-ring 2.2s ease-out infinite;
    opacity: 0;
  }

  @keyframes pulse-ring {
    0%   { transform: scale(0.85); opacity: 0.55; }
    100% { transform: scale(1.7);  opacity: 0; }
  }

  /* === Entry content — glassmorphism card === */
  .entry-content {
    background: rgba(255, 255, 255, 0.76);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(87, 6, 140, 0.1);
    border-radius: 10px;
    padding: 10px 14px;
    box-shadow: 0 2px 10px rgba(87, 6, 140, 0.06);
    transition: box-shadow 0.25s ease, transform 0.25s ease;
  }

  .entry-content:hover {
    box-shadow: 0 5px 22px rgba(87, 6, 140, 0.13);
    transform: translateX(3px);
  }

  .entry-content h3 {
    margin: 0 0 5px 0;
    font-size: 1.05rem;
    line-height: 1.3;
  }

  .entry-content div {
    font-size: 0.95rem;
    color: #666;
    margin: 0;
    line-height: 1.4;
  }

  .entry-content ul {
    margin: 5px 0 0 0;
    padding-left: 18px;
  }

  .entry-content ul li {
    margin-bottom: 4px;
    font-size: 0.95rem;
  }

  /* === Research Interests === */
  .research-interests {
    flex: 1;
    min-width: 280px;
  }

  .research-interests ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .research-interests ul li {
    padding: 8px 12px;
    border-left: 3px solid #57068c;
    margin-bottom: 10px;
    background: rgba(87, 6, 140, 0.03);
    border-radius: 0 7px 7px 0;
    font-size: 0.95rem;
    line-height: 1.55;
    transition: background 0.2s ease, border-left-color 0.2s ease, transform 0.2s ease;
  }

  .research-interests ul li:hover {
    background: rgba(87, 6, 140, 0.07);
    border-left-color: #9c27b0;
    transform: translateX(2px);
  }

  /* === Scroll-reveal base === */
  .reveal {
    opacity: 0;
    transform: translateY(16px);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }

  .reveal.visible {
    opacity: 1;
    transform: translateY(0);
  }

  /* [1] Gradient name shimmer */
  header h1 {
    background: linear-gradient(90deg, #3a006b 0%, #9c27b0 40%, #57068c 70%, #3a006b 100%);
    background-size: 220% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: name-shimmer 4s linear infinite;
  }

  @keyframes name-shimmer {
    0%   { background-position: 0%   center; }
    100% { background-position: 220% center; }
  }

  /* [4] Scroll progress bar */
  #scroll-progress {
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    width: 0%;
    background: linear-gradient(90deg, #57068c, #ab82c5);
    z-index: 9999;
    border-radius: 0 2px 2px 0;
    transition: width 0.08s linear;
    pointer-events: none;
  }


  /* Dark mode overrides */
  @media (prefers-color-scheme: dark) {
    .entry-content {
      background: rgba(55, 30, 75, 0.6);
      border-color: rgba(171, 130, 197, 0.15);
    }

    .entry-content div,
    .entry-content ul li {
      color: #ccc;
    }

    .research-interests ul li {
      background: rgba(87, 6, 140, 0.12);
      color: #ddd;
    }

    .research-interests ul li:hover {
      background: rgba(87, 6, 140, 0.22);
    }

    header h1 {
      background: linear-gradient(90deg, #ab82c5 0%, #e0c8f0 40%, #ab82c5 70%, #7b3fa8 100%);
      background-size: 220% auto;
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: name-shimmer 4s linear infinite;
    }
  }
</style>

<script>
  document.addEventListener('DOMContentLoaded', function () {

    /* [4] Scroll progress bar */
    var bar = document.createElement('div');
    bar.id = 'scroll-progress';
    document.body.prepend(bar);
    window.addEventListener('scroll', function () {
      var el = document.documentElement;
      var pct = el.scrollTop / (el.scrollHeight - el.clientHeight);
      bar.style.width = (pct * 100) + '%';
    }, { passive: true });

    /* Scroll-reveal for sections + pub rows */
    var selectors = [
      '.timeline-container',
      '.timeline-entry',
      '.research-interests',
      '.research-interests ul li',
      '.pub-row'
    ];
    var targets = document.querySelectorAll(selectors.join(', '));
    var revealObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry, i) {
        if (entry.isIntersecting) {
          var el = entry.target;
          setTimeout(function () { el.classList.add('visible'); }, i * 40);
          revealObs.unobserve(el);
        }
      });
    }, { threshold: 0.07 });
    targets.forEach(function (el) {
      el.classList.add('reveal');
      revealObs.observe(el);
    });

  });
</script>
