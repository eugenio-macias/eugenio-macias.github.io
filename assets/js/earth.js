(function () {
  "use strict";

  var canvas = document.getElementById("earth");
  if (!canvas || !canvas.getContext) return;
  var maskB64 = window.EARTH_MASK;
  var cities = window.EARTH_CITIES;
  if (!maskB64 || !cities) return;

  /* Planned trips. Blue pins, separate from cities already visited. */
  var trips = [
    ["Hà Giang loop", "Vietnam", 23.14, 105.02],
    ["Camino de Santiago", "Spain", 42.88, -8.545],
    ["San Sebastián", "Spain", 43.318, -1.981],
    ["Oaxaca", "Mexico", 17.065, -96.725],
    ["Pátzcuaro", "Mexico", 19.516, -101.609],
    ["Chengdu", "China", 30.66, 104.065],
    ["Xi'an", "China", 34.265, 108.954],
    ["Edinburgh", "Scotland", 55.953, -3.188],
    ["Shangri-La", "China", 27.827, 99.707],
    ["Silk Road", "China", 40.142, 94.662],
    ["Yi Peng", "Thailand", 18.788, 98.986],
    ["Chiang Mai mountains", "Thailand", 18.587, 98.487],
    ["Patagonia", "Argentina", -49.331, -72.886],
    ["Ålesund", "Norway", 62.472, 6.19],
    ["Svalbard", "Norway", 78.223, 15.646],
    ["Kumano Kodo", "Japan", 33.839, 135.774],
    ["Annapurna", "Nepal", 28.53, 83.878],
    ["Kakheti", "Georgia", 41.85, 45.72],
    ["Galápagos", "Ecuador", -0.744, -90.316],
    ["St. Petersburg", "Russia", 59.934, 30.335],
    ["Petra", "Jordan", 30.328, 35.444],
    ["Wadi Rum", "Jordan", 29.577, 35.421],
    ["Raja Ampat", "Indonesia", -0.23, 130.51]
  ];

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var caption = document.getElementById("earthCaption");
  var defaultCaption = caption ? caption.textContent : "";
  var ctx = canvas.getContext("2d", { alpha: true });
  var mask = new Uint8Array(360 * 180);
  var bin = atob(maskB64);
  var bit = 0;
  for (var i = 0; i < bin.length && bit < mask.length; i++) {
    var byte = bin.charCodeAt(i);
    for (var k = 7; k >= 0 && bit < mask.length; k--) {
      mask[bit++] = (byte >> k) & 1;
    }
  }

  var rot = -28;
  var raf = 0;
  var last = 0;
  var acc = 0;
  var running = false;
  var frame = null;
  var hits = [];
  var dpr = 1;

  function landAt(lonDeg, latDeg) {
    var x = ((lonDeg + 180) / 360) * 360;
    var y = ((90 - latDeg) / 180) * 180;
    if (x < 0) x = 0;
    if (x > 359.999) x = 359.999;
    if (y < 0) y = 0;
    if (y > 179.999) y = 179.999;
    var x0 = Math.floor(x);
    var y0 = Math.floor(y);
    var x1 = x0 + 1;
    if (x1 > 359) x1 = 359;
    var y1 = y0 + 1;
    if (y1 > 179) y1 = 179;
    var tx = x - x0;
    var ty = y - y0;
    var a = mask[y0 * 360 + x0];
    var b = mask[y0 * 360 + x1];
    var c = mask[y1 * 360 + x0];
    var d = mask[y1 * 360 + x1];
    return a * (1 - tx) * (1 - ty) + b * tx * (1 - ty) + c * (1 - tx) * ty + d * tx * ty;
  }

  function resize() {
    var css = canvas.clientWidth || 196;
    dpr = Math.min(2, Math.max(1.5, window.devicePixelRatio || 1));
    var px = Math.max(64, Math.round(css * dpr));
    if (!frame || canvas.width !== px || canvas.height !== px) {
      canvas.width = px;
      canvas.height = px;
      frame = ctx.createImageData(canvas.width, canvas.height);
    }
  }

  function draw() {
    resize();
    var w = canvas.width;
    var h = canvas.height;
    var data = frame.data;
    var cx = w * 0.5;
    var cy = h * 0.5;
    var r = Math.min(w, h) * 0.47;
    var lam0 = rot * Math.PI / 180;
    var pix = 0;
    for (var py = 0; py < h; py++) {
      var gy = (cy - (py + 0.5)) / r;
      for (var px = 0; px < w; px++) {
        var gx = ((px + 0.5) - cx) / r;
        var rr = gx * gx + gy * gy;
        if (rr > 1) {
          data[pix] = 0;
          data[pix + 1] = 0;
          data[pix + 2] = 0;
          data[pix + 3] = 0;
          pix += 4;
          continue;
        }
        var gz = Math.sqrt(1 - rr);
        var lat = Math.asin(gy) * 180 / Math.PI;
        var lon = Math.atan2(gx, gz) + lam0;
        if (lon > Math.PI) lon -= Math.PI * 2;
        if (lon < -Math.PI) lon += Math.PI * 2;
        var land = landAt(lon * 180 / Math.PI, lat);
        var coast = land > 0.08 && land < 0.92;
        var shade = gx * -0.32 + gy * 0.46 + gz * 0.83;
        if (shade < 0) shade = 0;
        shade = 0.34 + 0.66 * shade;
        var br = 36 + land * 72;
        var bg = 40 + land * 74;
        var bb = 46 + land * 76;
        if (coast) {
          br += 10;
          bg += 10;
          bb += 10;
        }
        data[pix] = br * shade;
        data[pix + 1] = bg * shade;
        data[pix + 2] = bb * shade;
        data[pix + 3] = 255;
        pix += 4;
      }
    }
    ctx.putImageData(frame, 0, 0);
    ctx.beginPath();
    ctx.arc(cx, cy, r - 0.5, 0, Math.PI * 2);
    ctx.strokeStyle = "rgba(12, 16, 20, 0.55)";
    ctx.lineWidth = Math.max(1, dpr);
    ctx.stroke();

    hits = [];
    var scale = w / (canvas.clientWidth || w);
    for (var c = 0; c < cities.length; c++) {
      var city = cities[c];
      var phi = city[2] * Math.PI / 180;
      var lam = city[3] * Math.PI / 180 - lam0;
      var x = Math.cos(phi) * Math.sin(lam);
      var y = Math.sin(phi);
      var z = Math.cos(phi) * Math.cos(lam);
      if (z < 0.05) continue;
      var sx = cx + x * r;
      var sy = cy - y * r;
      var rad = Math.max(1.15, (1.35 + z * 0.7) * dpr);
      ctx.beginPath();
      ctx.arc(sx, sy, rad + dpr * 0.45, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(8, 10, 14, 0.55)";
      ctx.fill();
      ctx.beginPath();
      ctx.arc(sx, sy, rad, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(236, 240, 244, 0.95)";
      ctx.fill();
      hits.push({
        x: sx / scale,
        y: sy / scale,
        rad: (rad + 3) / scale,
        name: city[0],
        country: city[1]
      });
    }

    for (var t = 0; t < trips.length; t++) {
      var trip = trips[t];
      var tphi = trip[2] * Math.PI / 180;
      var tlam = trip[3] * Math.PI / 180 - lam0;
      var tx = Math.cos(tphi) * Math.sin(tlam);
      var ty = Math.sin(tphi);
      var tz = Math.cos(tphi) * Math.cos(tlam);
      if (tz < 0.08) continue;
      var tsx = cx + tx * r;
      var tsy = cy - ty * r;
      var ps = (3.1 + tz * 1.35) * dpr;
      ctx.save();
      ctx.translate(tsx, tsy);
      ctx.fillStyle = "#2563eb";
      ctx.strokeStyle = "rgba(236, 244, 255, 0.95)";
      ctx.lineWidth = Math.max(1, dpr * 0.65);
      ctx.beginPath();
      ctx.moveTo(-ps * 0.46, -ps * 0.02);
      ctx.lineTo(0, ps * 1.45);
      ctx.lineTo(ps * 0.46, -ps * 0.02);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(0, -ps * 0.62, ps * 0.78, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(0, -ps * 0.62, ps * 0.28, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(236, 244, 255, 0.96)";
      ctx.fill();
      ctx.restore();
      var headY = (tsy - ps * 0.2) / scale;
      hits.push({
        x: tsx / scale,
        y: headY,
        rad: (ps * 1.35) / scale,
        name: "Next: " + trip[0],
        country: trip[1]
      });
    }
  }

  function show(text) {
    if (caption) caption.textContent = text;
  }

  canvas.addEventListener("mousemove", function (ev) {
    var rect = canvas.getBoundingClientRect();
    var x = ev.clientX - rect.left;
    var y = ev.clientY - rect.top;
    var best = null;
    var bestD = 1e9;
    for (var i = 0; i < hits.length; i++) {
      var h = hits[i];
      var dx = x - h.x;
      var dy = y - h.y;
      var d = dx * dx + dy * dy;
      if (d < h.rad * h.rad && d < bestD) {
        best = h;
        bestD = d;
      }
    }
    show(best ? best.name + ", " + best.country : defaultCaption);
  });
  canvas.addEventListener("mouseleave", function () {
    show(defaultCaption);
  });

  function tick(t) {
    if (!running) return;
    if (!last) last = t;
    var dt = Math.min(0.05, (t - last) / 1000);
    last = t;
    rot += dt * 11;
    if (rot > 180) rot -= 360;
    if (rot < -180) rot += 360;
    acc += dt;
    if (acc >= 1 / 30) {
      acc = 0;
      draw();
    }
    raf = requestAnimationFrame(tick);
  }

  function start() {
    if (reduce || running) return;
    running = true;
    last = 0;
    raf = requestAnimationFrame(tick);
  }

  function stop() {
    running = false;
    if (raf) cancelAnimationFrame(raf);
    raf = 0;
  }

  document.addEventListener("visibilitychange", function () {
    if (document.hidden) stop();
    else start();
  });
  window.addEventListener("resize", function () {
    frame = null;
    draw();
  }, { passive: true });

  draw();
  if (!reduce) start();
})();
