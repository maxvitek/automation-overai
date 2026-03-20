# GUIDANCE.md — Max's Direction

This file captures explicit guidance from Max. These are **non-negotiable and permanent** until explicitly changed.
When in doubt, re-read this file before making any product decision.

---

## Fleet / Vehicles

- **No Mach-E Mustang.** It doesn't exist in the fleet. Remove it.
- **Mustang sprite: Option A** — clean side profile, gunmetal grey Dark Horse. LOCKED IN. Already deployed.
- **Vehicle sizing**: tractor and gator look too small — confirm real-world lengths and re-check proportional scaling.
- Sprite sizes are **proportional to real-world vehicle length** with baseline `Airstream 28ft = 256px`.

## House vs Farm

- **Two distinct locations**: Forest House and Vitek Farm — these are separate properties.
- **Both should be respected equally** in the dashboard design. Neither should feel like a secondary screen.
- Review the full app design and ensure the farm gets equal visual weight, depth, and data coverage as the house.

## Design / Content

- Do not invent or make up data. If HA doesn't expose something, show graceful fallback.
- Keep the terminal/pixel-art aesthetic consistent across all pages (Gruvbox Dark, Press Start 2P).

## Process

- **Don't make Max say things twice.** Capture guidance here immediately.
- It's fine to try ideas and experiment — but once Max gives direction, lock it in.
- Guidance in this file overrides any prior implementation decisions.

---

*Last updated: 2026-03-18*

## UI / Carousel

- **Carousel nav buttons must be fixed in position** — PREV/NEXT should never shift when slide content changes height. Keep them in a dedicated row outside the slide area with a fixed height container.

## Themes

- **Gruvbox Light skin** — add a light theme alongside dark. Should respect system `prefers-color-scheme` automatically.
- User should not need to manually toggle — it follows OS dark/light setting.
- File as an issue and implement when current PRs are clear.

## Farm Planting Schedule

- The /garden and /farm pages should have a **detailed planting schedule** based on what Alder is tracking.
- Source of truth: ask Alder for their data model — what crops, dates, stages, beds, etc.
- This is real operational data, not made-up placeholder content.
- Once Alder shares the schema/data, build a proper PLANTING SCHEDULE section into /garden (and possibly /farm).
