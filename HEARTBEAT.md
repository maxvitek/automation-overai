# HEARTBEAT.md

## ⚠️ DEVELOPMENT PAUSED

Max has asked to pause development as of 2026-03-19 ~10:48 CDT.

**Do NOT:**
- File new issues
- Dispatch Codex or any agent
- Open PRs
- Merge anything

Wait for explicit go-ahead from Max before resuming the flywheel.

---

## Workflow

1. **Max files issues** (or I spec them when backlog is thin)
2. **I dispatch Codex** — `codex exec --full-auto` in a git worktree
3. **Codex writes the code** — I watch for completion
4. **I review and merge** — check the diff, run CI, merge when green, delete branch
5. **I deploy** — `ssh appforge@hector "cd /opt/app-forge && bash deploy/deploy.sh"`

No Alder reviews. No Axiom. No #app-forge messages. This is a two-player game: Codex codes, I ship.

---

## Priority Checks (every heartbeat, in order)

1. **Open PRs green?** → Review the diff, merge immediately, delete branch, deploy.
2. **Codex session finished?** → Check `process list`, push branch, open PR, review + merge.
3. **Open issues with no active Codex session?** → Dispatch Codex now.
4. **Backlog thin (< 2 open issues)?** → Spec and file new issues.

**Never leave a heartbeat without doing at least one of the above.**

---

## Deploy Command

```
ssh appforge@hector "cd /opt/app-forge && bash deploy/deploy.sh"
```

---

## Nightly Reflection (01:00–05:00 CDT)

Check `memory/heartbeat-state.json` → `lastNightlyReflection`. Skip if already done today.

1. Review `memory/YYYY-MM-DD.md`
2. What happened / went well / went poorly
3. Self-improvement → update workspace files if warranted
4. Consolidate learnings into MEMORY.md
5. Write under `## Nightly Reflection` heading
6. Update `lastNightlyReflection` timestamp
