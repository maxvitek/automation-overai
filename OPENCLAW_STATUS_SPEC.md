# Spec: openclaw-status — Agent Health & Status Endpoint

## Overview

A lightweight per-agent HTTP service that reads openclaw's on-disk state and exposes
a JSON status endpoint. No UI. Designed to be polled programmatically by automation
systems (e.g. the app-forge fleet dashboard).

One instance runs per agent, as a LaunchDaemon (macOS) or systemd service (Linux).
Deployed and managed by the existing `openclaw` Ansible role.

---

## Data Sources

All data is read from disk — no gateway API calls required.

| File | Data |
|------|------|
| `~/.openclaw/openclaw.json` | agent name, model, gateway port |
| `~/.openclaw/agents/main/sessions/*.jsonl` | session history, token usage, last activity |
| `~/.openclaw/cron/jobs.json` | scheduled jobs and their last-run state |
| `~/.openclaw/agents/main/agent/auth-profiles.json` | which auth profiles are configured |
| Gateway port (from config) | liveness check via TCP probe |
| `ps` output | gateway process uptime |

---

## Endpoint

### `GET /status`

Returns a single JSON object. Always responds 200 OK (even if agent is down — the
payload itself reflects health state).

**Response schema:**

```json
{
  "agent": {
    "name": "Rook",
    "user": "forestai",
    "model": "openai-codex/gpt-5.3-codex",
    "fallbacks": ["anthropic/claude-sonnet-4-6"]
  },
  "gateway": {
    "up": true,
    "port": 18800,
    "uptime_s": 3661
  },
  "activity": {
    "last_active_at": "2026-03-18T02:14:00Z",
    "last_session_id": "abc123",
    "idle_s": 480
  },
  "usage": {
    "current_session": {
      "tokens_in": 12400,
      "tokens_out": 3200
    },
    "today": {
      "sessions": 4,
      "tokens_in": 48000,
      "tokens_out": 12800
    },
    "window_1h": {
      "sessions": 1,
      "tokens_in": 12400,
      "tokens_out": 3200
    }
  },
  "crons": {
    "total": 2,
    "enabled": 1,
    "jobs": [
      {
        "id": "b02de813",
        "name": "heartbeat",
        "enabled": true,
        "last_run_at": "2026-03-18T01:00:00Z",
        "last_status": "success"
      }
    ]
  },
  "auth": {
    "profiles": ["anthropic:default", "openai-codex:default"]
  },
  "status_at": "2026-03-18T02:22:00Z"
}
```

### `GET /health`

Minimal liveness check — just returns 200 with `{"ok": true}`. For use by load
balancers or simple uptime monitors.

---

## Implementation Notes

### Language & Runtime
Node.js (consistent with the rest of the openclaw toolchain). No external npm
dependencies — Node built-ins only (`http`, `fs`, `child_process`).

### Session Parsing
Session files are JSONL — one JSON object per line. Each line has a `role` field
(`user` or `assistant`) and `usage` fields for token counts. To compute today's
usage: filter session files by mtime >= midnight local time, sum `usage.input_tokens`
and `usage.output_tokens` across all lines where those fields are present.

Last activity time = mtime of the most recently modified session file.

### Gateway Liveness
Read `gateway.port` from `openclaw.json`. Attempt a TCP connection to
`127.0.0.1:<port>` with a 1s timeout. If it connects, `up: true`. Do not make an
HTTP request — just a socket probe is sufficient.

Gateway uptime: find the `openclaw-gateway` process via `ps` filtered by the agent
user, extract start time, compute elapsed seconds.

### Caching
Cache the parsed state for 10 seconds. The `/status` endpoint should respond in
< 50ms. Do not re-read all session files on every request.

### Configuration
Accept configuration via environment variables:

| Variable | Default | Purpose |
|----------|---------|---------|
| `STATUS_PORT` | `19000` | Port to listen on |
| `OPENCLAW_DIR` | `~/.openclaw` | Root openclaw directory |
| `OPENCLAW_AGENT` | `main` | Agent ID |
| `CACHE_TTL_S` | `10` | Cache TTL in seconds |

The port should be allocated per agent and stored in inventory. Suggested port range:
`19000`–`19099` (one per agent, analogous to gateway ports `18789`–`18799`).

---

## Deployment

### Ansible Role: `openclaw-status`

New role at `playbooks/roles/openclaw-status/`. Wired into `playbooks/main.yaml`
after the `openclaw` role.

Tasks:
1. Template `server.js` to `~/.openclaw/status/server.js` for each agent
2. On macOS: template `~/Library/LaunchAgents/ai.openclaw.status.plist` and load it
3. On Linux: template `/etc/systemd/system/openclaw-status-<user>.service` and enable it
4. Open the status port in the host firewall (restrict to LAN — not public)

### Inventory

Add `status_port` to each agent entry:

```yaml
openclaw_agents:
  - user: forestai
    name: Rook
    gateway_port: 18800
    status_port: 19000
    ...
  - user: overai
    name: Aegis
    gateway_port: 18790
    status_port: 19001
    ...
```

---

## Aggregation (app-forge)

The app-forge backend polls each agent's status endpoint and merges into a fleet view.
Agent URLs are derived from inventory (baked into a config file at deploy time).

Example fleet config:
```json
[
  { "name": "Rook",  "url": "http://aeneas:19000" },
  { "name": "Aegis", "url": "http://aeneas:19001" },
  { "name": "Alder", "url": "http://nestor:19002" },
  { "name": "Axiom", "url": "http://cassandra:19003" }
]
```

Suggested polling interval: 30 seconds. Cache responses in the app-forge backend —
don't fan out to all agents on every frontend request.

---

## Out of Scope

- Authentication on the status endpoint (LAN-only, no sensitive data exposed)
- Writing to openclaw state (read-only)
- Real-time streaming (polling is sufficient)
- Historical storage (app-forge backend can accumulate its own history if needed)
