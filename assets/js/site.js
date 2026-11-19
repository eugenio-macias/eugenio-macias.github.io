(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var bar = document.getElementById("scrollBar");
  var pending = false;

  function setProgress() {
    if (!bar) return;
    var el = document.documentElement;
    var max = el.scrollHeight - el.clientHeight;
    var t = max > 0 ? el.scrollTop / max : 0;
    bar.style.transform = "scaleX(" + t.toFixed(4) + ")";
  }

  if (!reduce && bar) {
    window.addEventListener("scroll", function () {
      if (pending) return;
      pending = true;
      requestAnimationFrame(function () {
        pending = false;
        setProgress();
      });
    }, { passive: true });
    setProgress();
  } else if (bar) {
    bar.style.display = "none";
  }

  var here = location.pathname.replace(/\/$/, "") || "/";
  document.querySelectorAll(".primary-nav a").forEach(function (a) {
    var path = (a.pathname || "").replace(/\/$/, "") || "/";
    if (path === here) a.setAttribute("aria-current", "page");
  });
})();
