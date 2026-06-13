---
published: false  # internal design doc — keep out of the Jekyll/GitHub Pages build
---

# Beyond Research — Personal Gallery Page

**Date:** 2026-06-13
**Status:** Built
**Owner:** Hanchao Zhang

## Purpose

Add a personal page to the academic homepage that shows life beyond research —
Chinese calligraphy works and competitive swimming — to humanize the site. It is a
small, curated gallery (5 photos today), built to grow as more photos are added.

## Scope

- A new standalone page at `/life.html` reusing the existing sidebar layout.
  (Served at root level, not `/life/`, because the theme layout links its CSS/JS/avatar
  with relative `./assets/...` paths that 404 from a nested URL — `/life.html` keeps the
  page "directory" at root so those inherited paths resolve. No layout edit needed.)
- A "Beyond Research" gallery with two sections: Calligraphy and Swimming.
- Discovery: a handwritten "趣 Beyond Research →" link in the sidebar (home → `/life.html`),
  hidden on the page itself; a "← Back to home" link on `/life.html`.
- **Out of scope:** a CMS, tagging/filtering, comments, or per-photo pages. YAGNI.

## Chosen Design — "Mounted Scrolls" (Demo B)

Each calligraphy piece is framed like a hung exhibition scroll (立轴): a silk-tone mat,
dark roller bars top and bottom, and a soft drop shadow, so the works read as *mounted*
rather than floating. Swimming photos sit below as clean framed images with a caption
overlay. The page is a visual sibling of the home page, reusing its identity.

### Design tokens

- **Color** (inherited from the site, plus one new accent):
  - Ground `#ffffff` (lets the Vanta birds show through)
  - NYU Purple `#57068c`, Purple-dark `#3a006b`, Orchid `#9c27b0`, Soft `#ab82c5`
  - Ink `#1a1320`
  - **Cinnabar `#c1352b`** — the one new accent, used only as a small seal/chop and the
    hero accent bar. Authentic to calligraphy; spent in one place.
- **Type:**
  - Display/eyebrow: **Caveat** (already loaded by the theme) — handwriting fronting a
    page about handwriting.
  - Body: the theme's existing sans.
  - Chinese labels: system serif stack `"Songti SC","STSong","Noto Serif SC",serif`
    (no web font download).
- **Signature element:** the cinnabar **roller-bar scroll frame** + the hero accent bar.

### Layout

```
/life/  (homepage layout: existing sidebar on the left, content on the right)

  [accent bar] | beyond the research…        ← Caveat eyebrow
               | Beyond Research              ← gradient-shimmer h1 (reused from home)

  ← Back to home

  Chinese Calligraphy · 书法                  ← Caveat sub-label
  ┌─────────┐  ┌─────────┐  ┌─────────┐       ← 3 mounted scrolls
  │ ▔▔▔▔▔▔ │  │ ▔▔▔▔▔▔ │  │ ▔▔▔▔▔▔ │       (roller bar)
  │  silk   │  │  silk   │  │  silk   │
  │ [photo] │  │ [photo] │  │ [photo] │
  │ ▁▁▁▁▁▁ │  │ ▁▁▁▁▁▁ │  │ ▁▁▁▁▁▁ │       (roller bar)
  │ title 隶│  │ title 楷│  │ title 行│
  └─────────┘  └─────────┘  └─────────┘

  Swimming · 游泳
  ┌──────────────┐  ┌──────────────┐
  │  [photo]      │  │  [photo]      │
  │  caption ▔   │  │  caption ▔   │
  └──────────────┘  └──────────────┘
```

Calligraphy order is chronological by script style — Clerical (Han) → Regular (Wei-Jin)
→ Running (E. Jin) — so the order itself shows the script's evolution.

**Responsive:** calligraphy grid 3 → 2 → 1 columns; swimming 2 → 1. Single column on phones.

### Interaction

- **Lightbox:** clicking any photo opens it full-size, uncropped, on a dim overlay with its
  caption; close on click, the × button, or `Esc`. Lightweight vanilla JS, no library.
- **Hover:** scroll lifts slightly with a deeper shadow (reuses the home page's card-hover feel).
- **Scroll-reveal:** sections fade in on scroll, matching the home page (reuse the same pattern).
- **Reduced motion:** `prefers-reduced-motion` disables transforms/animations.

## Content (first-draft captions — editable)

**Calligraphy** (`assets/img/calligraphy/`)
| File | Title | Script |
|---|---|---|
| IMG_6331.jpeg | Spring Verses | Clerical · 隶书 |
| IMG_3157.jpeg | 賢 — "the worthy" | Regular · 楷书 |
| save-new.jpeg | Orchid Pavilion Preface | Running · 行书 |

**Swimming** (`assets/img/swimming/`)
| File | Title | Meta |
|---|---|---|
| IMG_6769.jpeg | The Team | Capital Univ. of Economics & Business · 2016 |
| IMG_6727.jpeg | On the Podium | 2016 Beijing Collegiate Swimming Championship |

> The clerical-script title "Spring Verses" is a placeholder — replace with the actual poem.

## Architecture / Files

This is a Jekyll site using the `yaoyao-liu/minimal-light` remote theme. The home page is
`index.md` → `homepage` layout (`_layouts/homepage.html`), composing `_includes/*.md`
section files. The new page follows the same pattern.

- **`life.md`** (new) — front matter `layout: homepage`, `permalink: /life/`, `title`.
  Contains a back-to-home link and `{% include_relative _includes/beyond_research.md %}`.
- **`_includes/beyond_research.md`** (new) — the gallery markup, an inline `<style>` block
  (scoped under a `.beyond` root class), and the inline lightbox + scroll-reveal `<script>`.
  Inline styles/scripts match the site's existing convention (e.g. `style.md`).
- **`index.md`** (edit) — add a compact "Beyond Research" teaser/link section so visitors
  discover `/life/`.

No changes to `_layouts/homepage.html`, so the sidebar, Vanta background, favicon switching,
and scroll-progress bar are inherited automatically on `/life/`.

### Image paths

Reference photos with root-relative, theme-safe URLs so they resolve correctly from `/life/`:
`{{ "/assets/img/calligraphy/IMG_6331.jpeg" | relative_url }}`. Verify each renders.

### CSS isolation

All new rules are scoped under a single `.beyond` wrapper class to avoid colliding with the
theme's global selectors (the theme uses bare `.section`, `h1`, etc.). Watch selector
specificity around section padding/margins.

## Error / edge handling

- Missing image → `alt` text describes the work (e.g. "Clerical script, 隶书").
- Photos vary in aspect ratio → scrolls keep natural proportions; swimming frames use a
  fixed aspect with `object-fit: cover`, full image preserved in the lightbox.
- Adding more photos later → drop files in the folder and add one `<figure>` block; the grid
  reflows. Documented as a comment in the include.

## Testing / verification

- Run Jekyll locally; load `/life/` and confirm all five images render and the sidebar matches home.
- Click each photo → lightbox opens the full image; `Esc`/×/backdrop close it.
- Resize to tablet and phone widths → columns collapse 3→2→1, no overflow.
- Home page shows the discovery link; `/life/` shows the back link; both navigate correctly.
- `prefers-reduced-motion` disables motion (toggle OS setting or emulate in devtools).
- Keyboard: photos are focusable and openable; lightbox close is keyboard-reachable.
