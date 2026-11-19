(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var bar = document.getElementById("scrollBar");
  var score = document.getElementById("scoreLines");
  var canvas = document.getElementById("strings");
  var scrollQueued = false;

  function onScroll() {
    var el = document.documentElement;
    var max = el.scrollHeight - el.clientHeight;
    var top = el.scrollTop || document.body.scrollTop || 0;
    if (bar) {
      var t = max > 0 ? top / max : 0;
      bar.style.transform = "scaleX(" + t.toFixed(4) + ")";
    }
    if (score && !reduce) {
      var shift = -((top * 0.18) % 48);
      score.style.transform = "translate3d(0," + shift.toFixed(2) + "px,0)";
    }
  }

  if (reduce) {
    if (bar) bar.style.display = "none";
  } else {
    window.addEventListener("scroll", function () {
      if (scrollQueued) return;
      scrollQueued = true;
      requestAnimationFrame(function () {
        scrollQueued = false;
        onScroll();
      });
    }, { passive: true });
    onScroll();
  }

  var here = location.pathname.replace(/\/$/, "") || "/";
  document.querySelectorAll(".primary-nav a").forEach(function (a) {
    var path = (a.pathname || "").replace(/\/$/, "") || "/";
    if (path === here) a.setAttribute("aria-current", "page");
  });

  var veil = document.getElementById("dimVeil");
  if (veil && !reduce) {
    var gx = window.innerWidth * 0.5;
    var gy = 160;
    var dimQueued = false;
    window.addEventListener("pointermove", function (e) {
      gx = e.clientX;
      gy = e.clientY;
      if (dimQueued) return;
      dimQueued = true;
      requestAnimationFrame(function () {
        dimQueued = false;
        veil.style.setProperty("--gx", gx.toFixed(0) + "px");
        veil.style.setProperty("--gy", gy.toFixed(0) + "px");
      });
    }, { passive: true });
  }

  function bindTilt(selector, maxDeg) {
    if (reduce) return;
    document.querySelectorAll(selector).forEach(function (card) {
      card.addEventListener("mousemove", function (e) {
        var r = card.getBoundingClientRect();
        var dx = (e.clientX - (r.left + r.width / 2)) / (r.width / 2);
        var dy = (e.clientY - (r.top + r.height / 2)) / (r.height / 2);
        card.style.transform = "translateY(-6px) scale(1.03) perspective(900px) rotateX(" + (-dy * maxDeg).toFixed(2) + "deg) rotateY(" + (dx * maxDeg).toFixed(2) + "deg)";
      });
      card.addEventListener("pointerleave", function () {
        card.style.transform = "";
      });
    });
  }
  bindTilt(".project-card", 7);
  bindTilt(".note-card", 8);

  if (!canvas || !canvas.getContext) return;

  var STRINGS = 6;
  var N = 72;
  var COLORS = ["#6e322c", "#8a4634", "#9a7040", "#1c2733", "#2d5c52", "#5a6878"];
  var WEIGHT = [2.4, 2.0, 1.6, 1.3, 1.05, 0.85];
  var y = [];
  var v = [];
  var s, i;
  for (s = 0; s < STRINGS; s++) {
    y.push(new Float32Array(N));
    v.push(new Float32Array(N));
  }

  var ctx = canvas.getContext("2d", { alpha: true });
  var dpr = 1;
  var width = 0;
  var height = 112;
  var running = false;
  var raf = 0;
  var lastX = -1;
  var lastY = -1;

  function resize() {
    var rect = canvas.getBoundingClientRect();
    width = Math.max(1, rect.width);
    height = Math.max(1, rect.height);
    dpr = Math.min(window.devicePixelRatio || 1, 1.5);
    canvas.width = Math.round(width * dpr);
    canvas.height = Math.round(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw(true);
  }

  function energy() {
    var m = 0;
    for (s = 0; s < STRINGS; s++) {
      var yy = y[s];
      var vv = v[s];
      for (i = 1; i < N - 1; i++) {
        var a = yy[i] < 0 ? -yy[i] : yy[i];
        var b = vv[i] < 0 ? -vv[i] : vv[i];
        if (a > m) m = a;
        if (b > m) m = b;
      }
    }
    return m;
  }

  function step() {
    var tension = 0.22;
    var damp = 0.972;
    for (s = 0; s < STRINGS; s++) {
      var yy = y[s];
      var vv = v[s];
      for (i = 1; i < N - 1; i++) {
        var acc = yy[i - 1] + yy[i + 1] - 2 * yy[i];
        vv[i] = (vv[i] + tension * acc) * damp;
      }
      for (i = 1; i < N - 1; i++) {
        yy[i] += vv[i];
        if (yy[i] > 26) yy[i] = 26;
        else if (yy[i] < -26) yy[i] = -26;
      }
      yy[0] = 0;
      yy[N - 1] = 0;
      vv[0] = 0;
      vv[N - 1] = 0;
    }
  }

  function stringY(index) {
    var pad = 16;
    return pad + ((height - pad * 2) * (index + 0.5)) / STRINGS;
  }

  function draw() {
    ctx.clearRect(0, 0, width, height);
    var nutX = 28;
    var bridgeX = width - 28;
    if (bridgeX < nutX + 40) {
      nutX = 8;
      bridgeX = width - 8;
    }
    ctx.strokeStyle = "rgba(45, 92, 82, 0.28)";
    ctx.lineWidth = 1;
    var frets = 7;
    var f;
    for (f = 1; f < frets; f++) {
      var x = nutX + (bridgeX - nutX) * (1 - Math.pow(0.5, f / 3.2));
      if (x > bridgeX - 10) break;
      ctx.beginPath();
      ctx.moveTo(x, 8);
      ctx.lineTo(x, height - 8);
      ctx.stroke();
    }
    ctx.fillStyle = "#6e322c";
    ctx.fillRect(nutX - 3, 8, 4, height - 16);
    ctx.fillStyle = "#9a7040";
    ctx.fillRect(bridgeX - 1, 8, 3, height - 16);

    var span = bridgeX - nutX;
    for (s = 0; s < STRINGS; s++) {
      var base = stringY(s);
      var yy = y[s];
      ctx.beginPath();
      ctx.lineWidth = WEIGHT[s];
      ctx.strokeStyle = COLORS[s];
      ctx.lineJoin = "round";
      ctx.lineCap = "round";
      for (i = 0; i < N; i++) {
        var px = nutX + span * (i / (N - 1));
        var py = base + yy[i];
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();
    }
  }

  function kick(stringIndex, t, amp) {
    if (stringIndex < 0 || stringIndex >= STRINGS) return;
    var center = Math.round(t * (N - 1));
    var vv = v[stringIndex];
    var k;
    for (k = -4; k <= 4; k++) {
      var j = center + k;
      if (j > 0 && j < N - 1) {
        vv[j] += amp * Math.exp(-(k * k) / 3.2);
      }
    }
    start();
  }

  function frame() {
    step();
    draw();
    if (energy() < 0.08) {
      running = false;
      raf = 0;
      canvas.dataset.live = "0";
      for (s = 0; s < STRINGS; s++) {
        y[s].fill(0);
        v[s].fill(0);
      }
      draw();
      return;
    }
    raf = requestAnimationFrame(frame);
  }

  function start() {
    if (reduce) return;
    if (running) return;
    running = true;
    canvas.dataset.live = "1";
    raf = requestAnimationFrame(frame);
  }

  function pointer(ev) {
    var rect = canvas.getBoundingClientRect();
    var x = ev.clientX - rect.left;
    var py = ev.clientY - rect.top;
    if (lastX < 0) {
      lastX = x;
      lastY = py;
      return;
    }
    var dy = py - lastY;
    var sIndex = -1;
    var best = 18;
    for (s = 0; s < STRINGS; s++) {
      var dist = Math.abs(py - stringY(s));
      if (dist < best) {
        best = dist;
        sIndex = s;
      }
    }
    if (sIndex >= 0 && (dy > 0.4 || dy < -0.4)) {
      var nutX = width > 80 ? 28 : 8;
      var bridgeX = width > 80 ? width - 28 : width - 8;
      var span = Math.max(1, bridgeX - nutX);
      var t = (x - nutX) / span;
      if (t < 0.04) t = 0.04;
      if (t > 0.96) t = 0.96;
      var amp = dy * 0.55;
      if (amp > 14) amp = 14;
      if (amp < -14) amp = -14;
      kick(sIndex, t, amp);
    }
    lastX = x;
    lastY = py;
  }

  function leave() {
    lastX = -1;
    lastY = -1;
  }

  resize();
  window.addEventListener("resize", resize, { passive: true });

  if (!reduce) {
    canvas.addEventListener("pointermove", pointer, { passive: true });
    canvas.addEventListener("pointerdown", pointer, { passive: true });
    canvas.addEventListener("pointerleave", leave);
    document.addEventListener("visibilitychange", function () {
      if (!document.hidden) return;
      if (raf) cancelAnimationFrame(raf);
      raf = 0;
      running = false;
      canvas.dataset.live = "0";
      for (s = 0; s < STRINGS; s++) {
        y[s].fill(0);
        v[s].fill(0);
      }
      draw();
    });
    var open = [0.78, 0.66, 0.55, 0.44, 0.34, 0.24];
    for (s = 0; s < STRINGS; s++) {
      (function (index) {
        setTimeout(function () {
          kick(STRINGS - 1 - index, open[index], 7.5 - index * 0.4);
        }, 280 + index * 110);
      })(s);
    }
  } else {
    canvas.dataset.live = "0";
  }
})();
