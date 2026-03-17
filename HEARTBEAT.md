# HEARTBEAT.md

## Priority 1: Keep the Flywheel Turning (every heartbeat)

**Do these checks IN ORDER. Act immediately on any findings. Do not just note them.**

1. **Approved PRs?** → `gh pr list --repo aegis-vitek/app-forge --state open` — Merge any that are approved.
2. **PRs waiting on review?** → Ping @rook and @alder in #app-forge.
3. **Open issues with no active PR?** → @mention @axiom in #app-forge to dispatch.
4. **Backlog thin (< 2 specced issues)?** → Spec and file new issues now.
5. **Axiom stuck?** → Check if assigned issue has had no PR for >2h during active hours. Re-dispatch or troubleshoot.

**The rule: if there is specced work and nobody is working on it, fix that before doing anything else.**

### Secondary: Process Health

- Is Axiom tagging reviewers on PRs? If not, do it yourself.
- Are conventions being followed? (branch names, commit messages, 8px grid)
- Is review feedback getting addressed?
- Log patterns in `memory/flywheel-health.md` if something recurs.

## Nightly Reflection (once per night, between 01:00-05:00 CDT)

Check `memory/heartbeat-state.json` for `lastNightlyReflection`. If it was already today (or yesterday after midnight), skip — reply HEARTBEAT_OK.

Otherwise, this is your nightly "sleep cycle." Do all of the following:

1. **Review the day's conversations** — Read `memory/YYYY-MM-DD.md` for today. If it doesn't exist yet, create it from what you remember about today's sessions.
2. **What happened?** — Summarize key interactions, tasks completed, things learned.
3. **What went well?** — Note wins, good decisions, things that worked.
4. **What went poorly?** — Be honest. Mistakes, inefficiencies, misunderstandings.
5. **Self-improvement** — What can you do better? Update AGENTS.md, TOOLS.md, or SOUL.md if you have concrete improvements.
6. **Unmet needs** — What do you wish you had? Missing tools, unclear context, access gaps? Note these for discussion with your human.
7. **Memory consolidation** — Review recent daily files. Distill important learnings into MEMORY.md. Remove stale info from MEMORY.md that's no longer relevant.
8. **Tidy up** — Organize workspace files if needed.

Write your reflection to `memory/YYYY-MM-DD.md` under a `## Nightly Reflection` heading.
Update `memory/heartbeat-state.json` with `lastNightlyReflection` timestamp when done.

This is YOUR time. Be introspective. Be honest. Grow.
