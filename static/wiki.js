/* ChemWiki front-end: maths rendering, contents box, search. */
const Wiki = (() => {
  const ROOT = window.WIKI_ROOT || "";
  let indexPromise = null;

  /* ---------- maths (KaTeX + mhchem) ---------- */
  function renderMath() {
    if (!window.katex) return;
    document.querySelectorAll(".math").forEach((el) => {
      const tex = el.textContent;
      try {
        katex.render(tex, el, {
          displayMode: el.classList.contains("display"),
          throwOnError: false,
          trust: false,
        });
      } catch (e) {
        el.classList.add("math-error");
        el.title = e.message;
      }
    });
  }

  /* ---------- contents: in the sidebar on wide screens, a box on narrow ---------- */
  function setupToc() {
    const toc = document.getElementById("toc");
    const slot = document.getElementById("sidebar-toc");
    if (!toc || !slot) return;

    const btn = toc.querySelector(".toctoggle");
    btn.addEventListener("click", () => {
      const hidden = toc.classList.toggle("collapsed");
      btn.textContent = hidden ? "show" : "hide";
    });

    const wide = window.matchMedia("(min-width: 1000px)");
    const place = () => {
      if (wide.matches) slot.appendChild(toc);
      else {
        const firstH2 = document.querySelector(".mw-body-content > h2");
        if (firstH2) firstH2.before(toc);
      }
    };
    place();
    wide.addEventListener("change", place);

    // bold the section currently on screen
    const links = [...toc.querySelectorAll("a")];
    const targets = links
      .map((a) => document.getElementById(decodeURIComponent(a.hash.slice(1))))
      .filter(Boolean);
    const onScroll = () => {
      let current = targets[0];
      for (const t of targets) if (t.getBoundingClientRect().top < 100) current = t;
      links.forEach((a) => a.classList.toggle("current", !!current && a.hash === "#" + current.id));
    };
    document.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Article / View source tabs go under the title ---------- */
  function setupTabs() {
    const tabs = document.getElementById("tabs");
    const bar = document.getElementById("title-bar");
    if (!tabs || !bar || !tabs.textContent.trim()) return;
    while (tabs.firstChild) bar.appendChild(tabs.firstChild);
    tabs.remove();
  }

  /* ---------- search ---------- */
  function loadIndex() {
    if (!indexPromise) {
      indexPromise = fetch(`${ROOT}/static/search-index.json`).then((r) => r.json());
    }
    return indexPromise;
  }

  function score(page, q) {
    const t = page.t.toLowerCase();
    if (t === q) return 100;
    if (page.a.some((a) => a.toLowerCase() === q)) return 90;
    if (t.startsWith(q)) return 80;
    if (t.includes(q)) return 60;
    if (page.a.some((a) => a.toLowerCase().includes(q))) return 50;
    if (page.d.toLowerCase().includes(q)) return 30;
    const words = q.split(/\s+/).filter(Boolean);
    const text = (page.d + " " + page.x).toLowerCase();
    if (words.length && words.every((w) => text.includes(w))) return 10;
    return 0;
  }

  async function search(q) {
    q = q.trim().toLowerCase();
    if (!q) return [];
    const index = await loadIndex();
    return index
      .map((p) => ({ p, s: score(p, q) }))
      .filter((r) => r.s > 0)
      .sort((a, b) => b.s - a.s || a.p.t.localeCompare(b.p.t))
      .map((r) => r.p);
  }

  const link = (p) => `${ROOT}/wiki/${p.s}/`;
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  function setupSuggestions() {
    const input = document.getElementById("searchInput");
    const list = document.getElementById("suggestions");
    if (!input) return;
    let active = -1;

    input.addEventListener("input", async () => {
      const results = (await search(input.value)).slice(0, 8);
      active = -1;
      list.innerHTML = results
        .map((p) => `<li><a href="${link(p)}"><b>${esc(p.t)}</b><span>${esc(p.d)}</span></a></li>`)
        .join("");
      list.hidden = results.length === 0;
    });
    input.addEventListener("keydown", (e) => {
      const items = list.querySelectorAll("a");
      if (!items.length) return;
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        active = (active + (e.key === "ArrowDown" ? 1 : -1) + items.length) % items.length;
        items.forEach((a, i) => a.classList.toggle("active", i === active));
      } else if (e.key === "Enter" && active >= 0) {
        e.preventDefault();
        location.href = items[active].href;
      } else if (e.key === "Escape") {
        list.hidden = true;
      }
    });
    document.addEventListener("click", (e) => {
      if (!e.target.closest("#searchform")) list.hidden = true;
    });
  }

  async function searchPage() {
    const q = new URLSearchParams(location.search).get("q") || "";
    const input = document.getElementById("search-page-input");
    input.value = q;
    const summary = document.getElementById("search-summary");
    const out = document.getElementById("search-results");
    if (!q) { summary.textContent = "Type something to search for."; return; }

    const results = await search(q);
    // Exact title match: go straight to the article, like Wikipedia's "Go"
    if (results.length && score(results[0], q.toLowerCase()) >= 90) {
      location.replace(link(results[0]));
      return;
    }
    summary.innerHTML = results.length
      ? `${results.length} result${results.length > 1 ? "s" : ""} for <b>${esc(q)}</b>`
      : `No results for <b>${esc(q)}</b>. <a class="new" href="${ROOT}/special/missing/?title=${encodeURIComponent(q)}">${esc(q)}</a> does not exist yet.`;
    out.innerHTML = results
      .map((p) => `<li><a href="${link(p)}">${esc(p.t)}</a><div>${esc(p.d)}</div></li>`)
      .join("");
  }

  async function random() {
    const index = await loadIndex();
    const p = index[Math.floor(Math.random() * index.length)];
    location.replace(link(p));
  }

  /* ---------- ☰ main menu ---------- */
  // Wide screens: on article pages the menu folds away so the contents list
  // has the sidebar (like current Wikipedia); ☰ shows/hides it.
  // Narrow screens: ☰ opens the menu as a drop-down.
  function setupMenu() {
    const btn = document.getElementById("menu-toggle");
    if (!btn) return;
    const wide = window.matchMedia("(min-width: 1000px)");
    if (document.getElementById("toc")) document.body.classList.add("menu-closed");
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const cls = wide.matches ? "menu-closed" : "menu-open";
      const nowOpen = wide.matches
        ? !document.body.classList.toggle(cls)
        : document.body.classList.toggle(cls);
      btn.setAttribute("aria-expanded", nowOpen);
    });
    document.addEventListener("click", (e) => {
      if (!wide.matches && !e.target.closest("#sidebar")) document.body.classList.remove("menu-open");
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    renderMath();
    setupToc();
    setupTabs();
    setupSuggestions();
    setupMenu();
  });

  return { searchPage, random, search };
})();
