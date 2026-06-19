$NEW_MODEL = "openai/gpt-oss-120b:free"

# ---- 1. Update settings.json ----
$settingsPath = "$HOME\.claude\settings.json"
$settings = Get-Content $settingsPath | ConvertFrom-Json
$settings.env.ANTHROPIC_MODEL = $NEW_MODEL
$settings | ConvertTo-Json -Depth 5 | Set-Content $settingsPath
Write-Host "[1/3] settings.json updated -> ANTHROPIC_MODEL = $NEW_MODEL"

# ---- 2. Patch all agent frontmatter files ----
$agentPath = "$HOME\.claude\agents"
$patched = 0
if (Test-Path $agentPath) {
    Get-ChildItem "$agentPath\*.md" | ForEach-Object {
        $content = Get-Content $_.FullName -Raw
        $updated = $content -replace '(?m)^model:\s*.+$', "model: $NEW_MODEL"
        if ($updated -ne $content) {
            Set-Content -Path $_.FullName -Value $updated -NoNewline
            $patched++
        }
    }
}
Write-Host "[2/3] Agent files patched: $patched files"

# ---- 3. Update workspace AGENTS.md (documentation) ----
$agentsMd = "e:\CLAUD\AGENTS.md"
if (Test-Path $agentsMd) {
    $agentsMdContent = Get-Content $agentsMd -Raw
    $agentsMdUpdated = $agentsMdContent -replace '(?m)^- Model: .+$', "- Model: $NEW_MODEL (via OpenRouter)"
    Set-Content -Path $agentsMd -Value $agentsMdUpdated -NoNewline
    Write-Host "[3/3] AGENTS.md registry updated"
}

# ---- Verify ----
Write-Host ""
Write-Host "=== VERIFICATION ==="
$verify = (Get-Content $settingsPath | ConvertFrom-Json).env.ANTHROPIC_MODEL
Write-Host "settings.json ANTHROPIC_MODEL : $verify"
if (Test-Path $agentPath) {
    $remaining = (Select-String -Path "$agentPath\*.md" -Pattern "^model:" | Where-Object { $_.Line -notmatch [regex]::Escape($NEW_MODEL) }).Count
    Write-Host "Agents still on old model     : $remaining (should be 0)"
}
