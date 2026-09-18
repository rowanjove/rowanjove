<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="jove-R Banner" src="assets/banner-dark.svg" width="100%">
</picture>

<div align="center">

# jove-R

**Local-first software for personal computing.**  
为个人计算环境构建本地优先的软件。

Windows · Rust · Tauri · Personal Data · AI-assisted Workflows

[rowanjove.top](https://rowanjove.top) &nbsp;·&nbsp; [X (Twitter)](https://x.com/rowanjove)

</div>

---

## Selected Work

### [INKREST](https://github.com/rowanjove/INKREST)

A local-first long-form writing workspace designed for authors. Integrates outline planning, draft production, character and setting memory retrieval, and pre-commit checks for banned terms and timeline continuity.

[![INKREST Workspace](https://raw.githubusercontent.com/rowanjove/INKREST/main/docs/images/readme-overview.png)](https://github.com/rowanjove/INKREST)

`Python` · `FastAPI` · `Vue 3` · `Electron` · `SQLite` &nbsp;|&nbsp; [Source](https://github.com/rowanjove/INKREST) · [Releases](https://github.com/rowanjove/INKREST/releases)

---

### [Browsory](https://github.com/rowanjove/Browsory)

Local-first desktop application that incrementally imports browsing history from Chromium-based profiles (Chrome, Edge, Brave). Indexes visit logs locally with SQLite FTS5 for sub-millisecond search and timeline analytics without sending data upstream.

[![Browsory Interface](https://raw.githubusercontent.com/rowanjove/Browsory/main/docs/screenshots/history-zh.png)](https://github.com/rowanjove/Browsory)

`Rust` · `Tauri` · `SQLite` · `FTS5` · `Windows` &nbsp;|&nbsp; [Source](https://github.com/rowanjove/Browsory) · [Releases](https://github.com/rowanjove/Browsory/releases)

---

### [ProxyDuck](https://github.com/rowanjove/ProxyDuck)

A Windows utility for per-application network routing. Intercepts and directs TCP, UDP, and DNS traffic of selected processes into a local SOCKS5 proxy, complete with a desktop GUI, live connection diagnostic logs, and a CLI daemon.

[![ProxyDuck Desktop](https://raw.githubusercontent.com/rowanjove/ProxyDuck/main/docs/images/proxyduck-overview.png)](https://github.com/rowanjove/ProxyDuck)

`Rust` · `Windows` · `Desktop` · `CLI` &nbsp;|&nbsp; [Source](https://github.com/rowanjove/ProxyDuck) · [Releases](https://github.com/rowanjove/ProxyDuck/releases)

---

### [Loomark](https://github.com/rowanjove/Loomark)

Desktop research crawler and web archival platform. Leverages `curl_cffi` for fast static extraction and Playwright for dynamic JavaScript pages, featuring automated site monitoring, snapshot history, and local structured search.

[![Loomark Dashboard](https://raw.githubusercontent.com/rowanjove/Loomark/main/docs/images/01_dashboard.png)](https://github.com/rowanjove/Loomark)

`Python` · `Playwright` · `curl_cffi` · `Tauri` &nbsp;|&nbsp; [Source](https://github.com/rowanjove/Loomark) · [Releases](https://github.com/rowanjove/Loomark/releases)

---

## Small Tools

Focused utilities designed for specific friction points in daily personal computing.

| Tool | Purpose | Platform / Stack | Links |
|---|---|---|---|
| **[RunTelos](https://github.com/rowanjove/RunTelos)** | Lightweight Windows task launcher for scripts, batch files and local utilities | Windows · Rust · Desktop | [Source](https://github.com/rowanjove/RunTelos) · [Releases](https://github.com/rowanjove/RunTelos/releases) |
| **[Metaxy](https://github.com/rowanjove/Metaxy)** | Personal cross-device relay for temporary clipboard text and file transfer | Web · Cloudflare · TS | [Source](https://github.com/rowanjove/Metaxy) |
| **[StackHome](https://github.com/rowanjove/StackHome)** | Local file workspace for rule-based organization, deduplication and backup | Windows · Rust · Desktop | [Source](https://github.com/rowanjove/StackHome) · [Releases](https://github.com/rowanjove/StackHome/releases) |
| **[Orthos](https://github.com/rowanjove/Orthos)** | Offline configuration validator and fixer for JSON, YAML, TOML, XML, INI, ENV | CLI · Rust | [Source](https://github.com/rowanjove/Orthos) · [Releases](https://github.com/rowanjove/Orthos/releases) |
| **[LANDrop](https://github.com/rowanjove/LANDrop)** | Zero-configuration local network file and text transfer utility | Local Network · Go | [Source](https://github.com/rowanjove/LANDrop) |
| **[MarkClip](https://github.com/rowanjove/MarkClip)** | Browser extension converting web pages, selected areas, or articles into clean Markdown | Chrome Extension · JS | [Source](https://github.com/rowanjove/MarkClip) |
| **[Postcase-X](https://github.com/rowanjove/Postcase-X)** | Saves X (Twitter) posts, threads, and articles as structured Markdown with ZIP media archive | Chrome Extension · JS | [Source](https://github.com/rowanjove/Postcase-X) · [Web Store](https://chromewebstore.google.com/detail/x-markdown-exporter/alicknocngkldhijfocddaepnfpgjlee) |
| **[CF-Nexarch](https://github.com/rowanjove/CF-Nexarch)** | Local Windows console for Cloudflare Workers, DNS, and edge service management | Windows · Desktop | [Source](https://github.com/rowanjove/CF-Nexarch) |
| **[WebVault](https://github.com/rowanjove/WebVault)** | Local web archive and digital asset preservation tool | Local-first · Storage | [Source](https://github.com/rowanjove/WebVault) |

---

## Currently Building

Active focus areas under continuous iterative development:

- **[INKREST](https://github.com/rowanjove/INKREST)** — Long-form memory consistency, plugin ecosystem architecture, and automated editorial workflows.
- **[Browsory](https://github.com/rowanjove/Browsory)** — Unified Chromium-family schema migration, FTS5 query optimization, and offline personal analytics.
- **[Loomark](https://github.com/rowanjove/Loomark)** — Incremental crawl policies, structured schema extractors, and automated task recovery.

---

## Principles

- **Local-first**: Personal data remains strictly on local storage in transparent, non-proprietary formats (SQLite, Markdown, JSON).
- **Useful before intelligent**: Reliable software engineering takes precedence over hype; AI serves as an augmentation layer rather than a gimmick.
- **Small tools, clear purpose**: Clean boundaries, single responsibilities, and straightforward solving of concrete personal computing problems.
- **Maintenance depth > Repository count**: Prioritize long-term polish, stability, test coverage, and documentation over publishing high volumes of transient repositories.

---

<details>
<summary><b>Labs & Experiments (探索性原型)</b></summary>
<br>

Exploratory prototypes and early concept verifications:

- **[WOL](https://github.com/rowanjove/WOL)** — Web-based random life simulation and destiny wheel experiment.
- **[Worldara](https://github.com/rowanjove/Worldara)** — Worldbuilding and lore management tool for long-form narrative design.
- **[PanNexus](https://github.com/rowanjove/PanNexus)** — Multi-source federation and resource aggregation search prototype.
- **[MediaFlow](https://github.com/rowanjove/MediaFlow)** — Lightweight multi-platform media stream parser and downloader.
- **[Pixkin](https://github.com/rowanjove/Pixkin)** — AI desktop companion prototype with character incubation and state management.
- **[Personal-Site-Matrix](https://github.com/rowanjove/Personal-Site-Matrix)** — 21 static website templates for personal profiles, blogs, and link trees.

</details>

---

## Elsewhere

- **Website**: [rowanjove.top](https://rowanjove.top)
- **X (Twitter)**: [@rowanjove](https://x.com/rowanjove)
