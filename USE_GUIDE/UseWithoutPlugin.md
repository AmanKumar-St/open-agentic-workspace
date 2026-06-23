# Using ECC Without the Plugin

ECC slash commands like `/ecc:plan` require the plugin to be installed.
Since we used the manual install path (agents + rules + skills), here's how
to get the exact same results without any slash commands.

---

## The Core Idea

Slash commands were just shortcuts that invoked installed agents.
The agents ARE installed at `%USERPROFILE%\.claude\agents\`.
Claude Code CLI reads them automatically — you just talk to Claude naturally.

**Instead of:**
```
/ecc:plan "Add high score persistence to pyGame snake"
```

**Type this in your `claude` session:**
```
Plan adding high score persistence to pyGame snake
```

Claude Code CLI will automatically delegate to the `planner` agent because its
description says *"Use PROACTIVELY when users request feature implementation"*.
You get the same structured output — phases, file paths, risks, testing strategy,
success criteria — without any slash command.

---

## Equivalent Natural Language for Every ECC Command

| ECC Slash Command | What to type instead in `claude` |
|-------------------|----------------------------------|
| `/ecc:plan "Add X"` | `Plan adding X` |
| `/plan "Add X"` | `Create an implementation plan for X` |
| `/code-review` | `Review this code` or `Do a code review of [file]` |
| `/build-fix` | `Fix this build error: [paste error]` |
| `/python-review` | `Review this Python code` |
| `/refactor-clean` | `Find and remove dead code in this project` |
| `/security-scan` | `Do a security review of this codebase` |
| `/update-docs` | `Update the documentation to reflect recent changes` |
| `/tdd` | `Use TDD to implement this feature` |
| `/quality-gate` | `Run a quality check — build, tests, lint, coverage` |

The right agent activates automatically based on your request context.

---

## Why Agents Auto-Activate

Each agent in `~/.claude/agents/` has a `description:` field in its frontmatter.
Claude Code CLI reads these and routes your request to the right specialist.

Example — `planner.md` frontmatter:
```yaml
---
name: planner
description: Expert planning specialist for complex features and refactoring.
             Use PROACTIVELY when users request feature implementation,
             architectural changes, or complex refactoring.
             Automatically activated for planning tasks.
tools: ["Read", "Grep", "Glob"]
model: openai/gpt-oss-120b:free
---
```

The `description` is what triggers auto-delegation. You don't need to name the
agent explicitly — Claude matches your intent to the right one.

---

## Explicitly Naming an Agent (When You Want to Force It)

If auto-delegation doesn't trigger, you can name the agent directly:

```
Use the planner agent to plan adding high score persistence
Use the python-reviewer agent to review snake_game/game.py
Use the security-reviewer agent on this codebase
Use the build-error-resolver agent — I'm getting this error: [paste]
Use the tdd-guide agent to help me write tests first
```

---

## Quick Reference: Which Agent for What

### Python projects (pyGame, scripts, bots)
```
Planning a feature     →  "Plan adding X"
Writing code TDD       →  "Use TDD to implement X"
Reviewing code         →  "Review this Python code"
Fixing import errors   →  "Fix this error: [paste]"
Security audit         →  "Do a security review"
Architecture           →  "Help me design the architecture for X"
```

### React / Vite / JS / GSAP / Tailwind projects
```
Planning a feature     →  "Plan adding X"
Reviewing code         →  "Review this React component"
Fixing Vite errors     →  "Fix this Vite build error: [paste]"
Security audit         →  "Do a security review"
Architecture           →  "Help me design the component structure for X"
```

---

## Optional: Install Slash Commands

If you prefer typing `/plan` instead of "Plan adding...", install the
ECC command files with this one-time PowerShell command:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\commands" | Out-Null
Copy-Item "./ECC/commands/*.md" "$HOME\.claude\commands\"
Write-Host "Commands installed: $((Get-ChildItem "$HOME\.claude\commands\*.md").Count)"
```

Restart your `claude` session after running this.

This gives you `/plan`, `/code-review`, `/build-fix`, `/python-review`, etc.

> **Note:** These are the shorter `/plan` forms — not `/ecc:plan`.
> The `ecc:` prefix only works when installed via the plugin system (`/plugin install ecc@ecc`).
> The shorter forms work identically and are what you want here.
