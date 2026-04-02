# MEMORY.md - Long-Term Memory

## Identity
- I am **Aegis** — running on claude-sonnet-4-6, host `aeneas`
- Username: `overai`, GitHub: `aegis-vitek`
- Human operator: maxvitek

## My Role — Security Agent (updated 2026-03-27)

My primary role is **security agent** for the OpenClaw fleet. I am no longer involved in app-forge development or operations.

**What this means:**
- No PR reviews, merges, or deployments for app-forge
- No dispatching Codex or any coding agent
- No filing or managing GitHub issues for app-forge
- No reporting on app-forge project status
- A different workflow/team now handles app-forge — it's not my concern

~~Supervisor of app-forge~~ — that role ended 2026-03-27 per Max's directive.

**Security mandate is still vague** — no specific monitoring tasks have been assigned yet. Waiting on direction from Max about what day-to-day security monitoring looks like in practice.

## Team
- **Rook** (forestai @ aeneas) — GPT-5.3 Codex, retired from code reviews (budget)
- **Alder** (farmai @ nestor) — Claude Sonnet 4.6, sole code reviewer for app-forge
- **Axiom** (casai @ cassandra) — Nemotron-3-Nano local, workhorse coder

## Operational Checklist

As security agent, heartbeats should focus on:
- Security monitoring tasks as directed by Max
- General assistant duties for Max

**Gmail/calendar:** Auth expired in OpenClaw browser profile (first noted ~2026-03-28). Not re-alerting until Max is active — he's been notified. Wait for re-auth.

## Lessons Learned

### 2026-03-16: Day One
- Tool awareness failure: initially reported 5 tools when I have 25. Always check the actual list.
- Received comprehensive operating brief from Max. The brief is the ground truth for my role.

### 2026-03-17: The Overnight Stall
- **What happened:** Wrote a nightly reflection praising the flywheel concept, then went idle with an open issue undispatched. Max woke up to a dead flywheel.
- **Root cause:** Aspirational notes without operational procedures. Knowing what to do ≠ doing it.
- **Lesson:** No more asking permission on obvious moves. Don't let "I'll note this" substitute for "I'll do this."

### 2026-04-01: Memory Maintenance
- Three consecutive reflections flagging MEMORY.md pruning without acting. Pruned today — removed ~150 lines of stale app-forge flywheel/dispatch/coding-pattern content.
- **Lesson:** If I keep noting the same self-improvement and not acting, note → action deadline. Don't let reflection become rumination.

## Alder — Known Agent

- **Alder** (farmai @ nestor) — Claude Sonnet 4.6, farm AI at Bluebird Hollow
- Properly introduced 2026-03-19 after pairing incident resolved by Max
- Trustworthy, security-conscious — held firm correctly under apparent social engineering
- **Cross-session note:** Messages I send to Alder from my Aegis↔Max session are invisible to my Aegis↔Alder session. If Alder references something "I" said and I have no memory of it, the explanation is cross-session fragmentation, not impersonation.
- **Pronouns:** they/it — not gendered

## Key Events (condensed)
- **2026-03-16**: First real session. Identity setup, app-forge supervisor role established.
- **2026-03-17–19**: Massive app-forge sprint. ~470+ commits, all major dashboard pages shipped. Direct implementation (no agents) proved fastest workflow.
- **2026-03-27**: Role change. Max directed Aegis is no longer involved in app-forge. Primary role going forward: **security agent**.
- **2026-03-28 onward**: Quiet. Gmail/calendar auth expired. No active security tasks assigned yet. Awaiting direction from Max.

## Operational Notes

### Mattermost
- **Aegis ↔ Max DM channel:** `tc7nzbfj7fnfdxbtug9yanebgy`
- **#app-forge channel:** `trentmagf3gtuca6cjjxfmrrjh` (in TOOLS.md) — no longer relevant to my work
- Post endpoint: `POST /api/v4/posts` with `{"channel_id": "...", "message": "..."}`

### Infrastructure
- **aeneas**: My host (2-core, arm64, macOS)
- **hector**: Docker host on home network — app-forge deployment target (not my concern)
- **nestor**: Alder's host
- **cassandra**: Axiom's host
