/* membrezweiler.com shared behavior. Progressive enhancement only. */
(function () {
  "use strict";

  /* ---- colour theme ------------------------------------------------------ */
  var root = document.documentElement;
  var KEY = "mw-theme";

  try {
    var saved = localStorage.getItem(KEY);
    if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);
  } catch (e) { /* storage may be unavailable */ }

  function currentTheme() {
    var explicit = root.getAttribute("data-theme");
    if (explicit) return explicit;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  document.addEventListener("click", function (ev) {
    var btn = ev.target.closest && ev.target.closest(".theme-toggle");
    if (!btn) return;
    var next = currentTheme() === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    btn.setAttribute("aria-label", next === "dark" ? "Switch to light theme" : "Switch to dark theme");
    try { localStorage.setItem(KEY, next); } catch (e) { /* ignore */ }
  });

  /* ---- lab repository filtering ------------------------------------------ */
  var grid = document.getElementById("lab-grid");
  if (!grid) return;

  var search = document.getElementById("lab-search");
  var buttons = Array.prototype.slice.call(document.querySelectorAll(".filter-btn"));
  var counter = document.getElementById("lab-count");
  var empty = document.getElementById("lab-empty");
  var labs = Array.prototype.slice.call(grid.querySelectorAll(".lab"));
  var activeCourse = "all";

  function apply() {
    var q = (search && search.value ? search.value : "").trim().toLowerCase();
    var shown = 0;

    labs.forEach(function (lab) {
      var matchCourse = activeCourse === "all" || lab.dataset.course === activeCourse;
      var haystack = lab.dataset.search || lab.textContent.toLowerCase();
      var matchText = !q || haystack.indexOf(q) !== -1;
      var visible = matchCourse && matchText;
      lab.hidden = !visible;
      if (visible) shown++;
    });

    if (counter) {
      counter.textContent = shown === labs.length
        ? "Showing all " + labs.length + " labs."
        : "Showing " + shown + " of " + labs.length + " labs.";
    }
    if (empty) empty.hidden = shown !== 0;
  }

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      activeCourse = btn.dataset.filter;
      buttons.forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
      apply();
    });
  });

  if (search) {
    search.addEventListener("input", apply);
    search.addEventListener("search", apply);
  }

  labs.forEach(function (lab) {
    lab.dataset.search = lab.textContent.toLowerCase();
  });

  apply();
})();
