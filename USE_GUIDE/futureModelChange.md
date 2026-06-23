# Future Model Change Guide

How to switch the AI model used by Claude Code CLI across this entire workspace.
Covers every file that stores the model string so nothing is missed.

---

## Overview — What Stores the Model

There are exactly **3 places** the model string lives:

| # | File | What It Controls |
|---|------|-----------------|
| 1 | `%USERPROFILE%\.claude\settings.json` | The model Claude Code CLI uses for every session |
| 2 | `%USERPROFILE%\.claude\agents\*.md` (67 files) | The model each ECC specialist agent uses when invoked |
| 3 | `./AGENTS.md` (Workspace root) | Human-readable workspace registry (documentation only) |

---

## Step-by-Step: Switching to Any New Model

### Step 1 — Find the Exact OpenRouter Model String

Go to [openrouter.ai/models](https://openrouter.ai/models) and search for your model.
Copy the **API name** exactly — it's case-sensitive.

Common examples:
| Model | OpenRouter API string |
|-------|----------------------|
| GPT OSS 120B (current) | `openai/gpt-oss-120b:free` |
| Qwen 3 (235B MoE) | `qwen/qwen3-235b-a22b:free` |
| Qwen 2.5 72B | `qwen/qwen-2.5-72b-instruct` |
| Qwen QwQ 32B | `qwen/qwq-32b:free` |
| Llama 3.3 70B | `meta-llama/llama-3.3-70b-instruct:free` |
| DeepSeek R1 | `deepseek/deepseek-r1:free` |

> **Finding Qwen 3.6 specifically:** Search "qwen 3.6" on openrouter.ai — look for
> a string like `qwen/qwen3-6b` or similar. Confirm the exact string before running
> the commands below, as the wrong string will silently fail.

---

### Step 2 — Run This PowerShell Script

Open PowerShell and run (replace the model string with your new one):

```powershell
# ============================================================
# MODEL SWITCH SCRIPT
# Replace NEW_MODEL with your actual OpenRouter model string
# ============================================================

$NEW_MODEL = "qwen/qwen3-235b-a22b:free"   # <-- CHANGE THIS LINE ONLY

# ---- 1. Update settings.json ----
$settingsPath = "$HOME\.claude\settings.json"
$settings = Get-Content $settingsPath | ConvertFrom-Json
$settings.env.ANTHROPIC_MODEL = $NEW_MODEL
$settings | ConvertTo-Json -Depth 5 | Set-Content $settingsPath
Write-Host "[1/3] settings.json updated -> ANTHROPIC_MODEL = $NEW_MODEL"

# ---- 2. Patch all 67 agent frontmatter files ----
$agentPath = "$HOME\.claude\agents"
$patched = 0
Get-ChildItem "$agentPath\*.md" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    $updated = $content -replace '(?m)^model:\s*.+$', "model: $NEW_MODEL"
    if ($updated -ne $content) {
        Set-Content -Path $_.FullName -Value $updated -NoNewline
        $patched++
    }
}
Write-Host "[2/3] Agent files patched: $patched files"

# ---- 3. Update workspace AGENTS.md (documentation) ----
$agentsMd = "./AGENTS.md"
$agentsMdContent = Get-Content $agentsMd -Raw
$agentsMdUpdated = $agentsMdContent -replace '(?m)^- Model: .+$', "- Model: $NEW_MODEL (via OpenRouter)"
Set-Content -Path $agentsMd -Value $agentsMdUpdated -NoNewline
Write-Host "[3/3] AGENTS.md registry updated"

# ---- Verify ----
Write-Host ""
Write-Host "=== VERIFICATION ==="
$verify = (Get-Content $settingsPath | ConvertFrom-Json).env.ANTHROPIC_MODEL
Write-Host "settings.json ANTHROPIC_MODEL : $verify"
$remaining = (Select-String -Path "$agentPath\*.md" -Pattern "^model:" | Where-Object { $_.Line -notmatch [regex]::Escape($NEW_MODEL) }).Count
Write-Host "Agents still on old model     : $remaining (should be 0)"

Write-Host ""
Write-Host "Done. Restart your 'claude' CLI session to apply."
```

---

### Step 3 — Restart Claude Code CLI

```bash
# In your terminal, exit the current claude session and reopen:
exit   # or Ctrl+C
claude # reopen
```

The new model takes effect immediately on the next session start.

---

## Quick Copy-Paste for Specific Models

### Switch to Qwen 3 (find exact string on openrouter.ai first)
```powershell
$NEW_MODEL = "qwen/qwen3-235b-a22b:free"   # verify this string at openrouter.ai/models
```

### Switch back to GPT OSS 120B (current)
```powershell
$NEW_MODEL = "openai/gpt-oss-120b:free"
```

### Switch to DeepSeek R1 (free)
```powershell
$NEW_MODEL = "deepseek/deepseek-r1:free"
```

---

## What Does NOT Need Changing

These are model-agnostic — leave them alone:

- `./_templates/**/CLAUDE.md` — project instructions, not model-specific
- `./pyGame/CLAUDE.md` — same
- `%USERPROFILE%\.claude\rules\ecc\**` — plain markdown coding standards
- `%USERPROFILE%\.claude\skills\**` — workflow definitions
- `ANTHROPIC_BASE_URL` in settings.json — stays `https://openrouter.ai/api/v1`
- `ANTHROPIC_API_KEY` / `ANTHROPIC_AUTH_TOKEN` — your OpenRouter API key stays the same

---

## If a Model Doesn't Work

Some models on OpenRouter have quirks with Claude Code CLI:

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `model not found` error | Wrong model string | Check exact ID on openrouter.ai |
| Agents not responding to instructions | Model ignores YAML frontmatter | Normal — frontmatter is a hint, not enforced |
| Session starts then immediately errors | Model doesn't support system prompts | Try a different model variant |
| Slow / no streaming | `:free` tier rate-limited | Switch to paid tier or different free model |
| `MAX_THINKING_TOKENS` errors | Claude-only feature in env | Already removed from your settings.json |

---

## History Log

| Date | From | To | Changed By |
|------|------|----|-----------|
| 2026-06-18 | `sonnet[1m]` (Claude) | `openai/gpt-oss-120b:free` | Initial OpenRouter setup |
| _(next change)_ | `openai/gpt-oss-120b:free` | _(new model)_ | _(your name)_ |
