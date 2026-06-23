# New Project Guide — Adding a Project to the ECC Workspace

Every new project in `./` follows the same 4-step checklist.
This guide walks through each step in full detail with working examples for every stack.

---

## The 4-Step Checklist (Quick Reference)

```
Step 1 → Create the project folder under ./
Step 2 → Copy the right CLAUDE.md template into it (then customize)
Step 3 → Register the project in ./AGENTS.md
Step 4 → Open claude CLI from the project folder
```

That's it. Steps 1–3 take about 5 minutes. Details below.

---

## Step 1 — Create the Project Folder

All projects live directly under `./`.
One project = one folder. Never nest projects inside each other.

```powershell
# General pattern:
New-Item -ItemType Directory "./<your-project-name>"

# Examples:
New-Item -ItemType Directory "./portfolio-site"
New-Item -ItemType Directory "./weather-app"
New-Item -ItemType Directory "./discord-bot"
```

> Rule: The folder name becomes how you refer to the project everywhere.
> Use lowercase with hyphens, no spaces.

---

## Step 2 — Copy and Customize the Right CLAUDE.md

This is the most important step. The `CLAUDE.md` file is what Claude reads
at the start of every session to understand your project — its stack, how to run it,
what rules to follow, and which ECC agents/skills to use.

**Pick your stack:**

| Your Stack | Template to copy from |
|-----------|----------------------|
| React + Vite + Tailwind CSS + GSAP | `./_templates/react-vite-tailwind-gsap/CLAUDE.md` |
| Vanilla JavaScript | `./_templates/vanilla-js/CLAUDE.md` |
| Python (any framework) | `./pyGame/CLAUDE.md` as a starting point |

---

### Stack A — React + Vite + Tailwind CSS + GSAP

**Example project: `portfolio-site`** — a personal portfolio with scroll animations

#### 2A-1. Scaffold the project first, then copy CLAUDE.md

```powershell
# From ./portfolio-site:
cd ./portfolio-site

# Create Vite + React app in current folder
npm create vite@latest . -- --template react

# Install all stack dependencies
npm install
npm install gsap @gsap/react
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

#### 2A-2. Copy the CLAUDE.md template

```powershell
Copy-Item "./_templates/react-vite-tailwind-gsap/CLAUDE.md" "./portfolio-site/CLAUDE.md"
```

#### 2A-3. Customize the CLAUDE.md — what to change

Open `./portfolio-site/CLAUDE.md` and edit these sections:

**Change the title line:**
```markdown
# Before (template placeholder):
# [PROJECT NAME] — React + Vite + Tailwind CSS + GSAP

# After (your project):
# portfolio-site — Personal Portfolio with GSAP Scroll Animations
```

**Delete the template comment block at the top:**
```markdown
<!-- 
  TEMPLATE: Copy this file to your project root as CLAUDE.md
  Replace bracketed placeholders with your actual project details
-->
```
Remove this entirely — it's just for you, not Claude.

**Update Project Structure to match your actual folders:**
```markdown
## Project Structure
src/
├── components/
│   ├── Hero.jsx          # Landing section with GSAP entrance animation
│   ├── Projects.jsx      # Project cards with ScrollTrigger reveal
│   └── Contact.jsx       # Contact form
├── animations/
│   └── gsap.config.js    # ScrollTrigger registered here
├── styles/
│   └── index.css         # Tailwind directives
└── App.jsx
```

**Add project-specific Known Issues section (very important for future sessions):**
```markdown
## Known Issues / Gotchas
- ScrollTrigger requires `gsap.registerPlugin(ScrollTrigger)` in gsap.config.js
  before any component imports it — do not move this
- Tailwind purge must include `./src/**/*.{js,jsx}` in tailwind.config.js content array
- Vite hot reload can lose GSAP context — full refresh fixes it
```

**Add dev commands specific to this project:**
```markdown
## Dev Commands
npm run dev          # http://localhost:5173
npm run build        # Output to dist/
npm run preview      # Preview dist/ at http://localhost:4173
```

**Final portfolio-site CLAUDE.md should look like:**
```markdown
# portfolio-site — Personal Portfolio with GSAP Scroll Animations

## Stack
- Framework: React 18 + Vite
- Styling: Tailwind CSS v3
- Animations: GSAP + ScrollTrigger
- Language: JavaScript / JSX
- Package manager: npm

## Dev Commands
npm run dev      # http://localhost:5173
npm run build
npm run preview

## Project Structure
src/
├── components/
│   ├── Hero.jsx
│   ├── Projects.jsx
│   └── Contact.jsx
├── animations/
│   └── gsap.config.js    ← ScrollTrigger registered here
├── styles/
│   └── index.css
└── App.jsx

## GSAP Rules
(keep all rules from template — they all apply)

## Tailwind CSS Rules
(keep all rules from template)

## React / Vite Rules
(keep all rules from template)

## Known Issues / Gotchas
- Always register ScrollTrigger in gsap.config.js before component imports
- Tailwind content array must include src/**/*.{js,jsx}

## Skills to Use
- frontend-patterns
- tdd-workflow
- coding-standards
- security-review

## Agent Delegation
- typescript-reviewer — React code quality
- build-error-resolver — Vite failures
- security-reviewer — before deploying
```

---

### Stack B — Vanilla JavaScript

**Example project: `weather-app`** — a browser weather dashboard using a public API

#### 2B-1. Create the project structure manually

```powershell
cd ./weather-app

# Create folder structure
New-Item -ItemType Directory src, src\modules, src\utils, styles, assets

# Create entry files
New-Item index.html
New-Item src\main.js
New-Item styles\main.css
```

#### 2B-2. Copy the CLAUDE.md template

```powershell
Copy-Item "./_templates/vanilla-js/CLAUDE.md" "./weather-app/CLAUDE.md"
```

#### 2B-3. Customize the CLAUDE.md

**Change the title:**
```markdown
# weather-app — Browser Weather Dashboard
```

**Update Stack section with the actual tech:**
```markdown
## Stack
- Language: Vanilla JavaScript (ES2022+)
- Styling: CSS (no framework)
- APIs: OpenWeatherMap REST API
- Bundler: None — open index.html with Live Server
- Runtime: Browser
```

**Update Dev Commands:**
```markdown
## Dev Commands
# No bundler — open index.html with:
npx serve .           # http://localhost:3000
# or use VS Code Live Server extension
```

**Update Project Structure:**
```markdown
## Project Structure
weather-app/
├── index.html
├── src/
│   ├── main.js            # App entry, event listeners, DOM setup
│   ├── modules/
│   │   ├── weather.js     # API calls to OpenWeatherMap
│   │   └── ui.js          # DOM update functions
│   └── utils/
│       └── format.js      # Temperature/date formatters
├── styles/
│   └── main.css
└── assets/
    └── icons/             # Weather condition SVGs
```

**Add project-specific Known Issues:**
```markdown
## Known Issues / Gotchas
- API key goes in a .env file — NEVER commit it
- OpenWeatherMap free tier: 60 calls/min, 1000 calls/day limit
- Fetch API errors silently on CORS issues — always check Network tab
- Browser caches aggressively — use Cache-Control headers on API responses
```

**Add Environment Variables section:**
```markdown
## Environment Variables
Create a .env file (git-ignored):
  WEATHER_API_KEY=your_openweathermap_key_here

Load it with: const key = import.meta.env.WEATHER_API_KEY (if using Vite)
Or: manually set window.ENV = { WEATHER_API_KEY: '...' } in a config.js (no bundler)
```

**Update Agent Delegation:**
```markdown
## Agent Delegation
- typescript-reviewer — JS quality, XSS prevention
- security-reviewer — API key handling, CSP headers
- build-error-resolver — if CORS or fetch errors
```

---

### Stack C — Python (Any Framework)

**Example project: `discord-bot`** — a Python Discord bot using discord.py

#### 2C-1. Create the project structure

```powershell
cd ./discord-bot
New-Item -ItemType Directory src, tests
New-Item src\bot.py, src\commands.py, src\config.py, tests\test_commands.py
```

#### 2C-2. Use pyGame's CLAUDE.md as a starting point

```powershell
Copy-Item "./pyGame/CLAUDE.md" "./discord-bot/CLAUDE.md"
```

#### 2C-3. Rewrite it completely for the new project

The pyGame CLAUDE.md is a starting point for structure only — every section needs updating.

**Title:**
```markdown
# discord-bot — Moderation + Utility Discord Bot
```

**Stack:**
```markdown
## Stack
- Language: Python 3.11+
- Framework: discord.py 2.x
- Python path: python
- Package manager: pip
```

**Dev Commands:**
```markdown
## Dev Commands
# Run the bot (from ./discord-bot)
python src\bot.py

# Run tests
python -m pytest tests/ -v

# Install dependencies
python -m pip install -r requirements.txt
```

**Project Structure:**
```markdown
## Project Structure
discord-bot/
├── src/
│   ├── bot.py           # Bot entry point, intents setup, on_ready
│   ├── commands.py      # Slash commands (use Cog pattern)
│   └── config.py        # Loads env vars (DISCORD_TOKEN, GUILD_ID)
├── tests/
│   └── test_commands.py # Unit tests for command logic
├── requirements.txt
├── .env                 # DISCORD_TOKEN=... (git-ignored)
└── CLAUDE.md
```

**Known Issues:**
```markdown
## Known Issues / Gotchas
- Discord token goes in .env — NEVER hardcode or commit it
- discord.py requires Python 3.8+ — we use 3.11
- Always declare all intents you need in bot.py or events won't fire
- Use Cog pattern for commands — never add all commands to bot.py directly
- Rate limits: 5 req/sec per guild; use exponential backoff on 429 errors
```

**Skills:**
```markdown
## Skills to Use
- python-patterns     — type hints, dataclasses, async/await
- python-testing      — pytest fixtures for mocking discord.py
- tdd-workflow        — test command logic before wiring to Discord
- security-review     — token handling, input sanitization
```

**Agent Delegation:**
```markdown
## Agent Delegation
- python-reviewer      — code quality, async patterns
- build-error-resolver — discord.py import/version errors
- tdd-guide            — writing tests for async Discord commands
- security-reviewer    — before publishing or open-sourcing
```

---

## Step 3 — Register in ./AGENTS.md

Open [AGENTS.md](./AGENTS.md) and add your project to the Projects table.

**Current table:**
```markdown
| Project | Stack | Directory | Status |
|---------|-------|-----------|--------|
| pyGame / Snake | Python + pygame | `./pyGame/` | Active |
```

**After adding portfolio-site:**
```markdown
| Project | Stack | Directory | Status |
|---------|-------|-----------|--------|
| pyGame / Snake | Python + pygame | `./pyGame/` | Active |
| portfolio-site | React + Vite + Tailwind + GSAP | `./portfolio-site/` | Active |
```

**After adding weather-app:**
```markdown
| Project | Stack | Directory | Status |
|---------|-------|-----------|--------|
| pyGame / Snake | Python + pygame | `./pyGame/` | Active |
| portfolio-site | React + Vite + Tailwind + GSAP | `./portfolio-site/` | Active |
| weather-app | Vanilla JS | `./weather-app/` | Active |
```

> Why this matters: When Claude Code CLI starts from the workspace root (`./`), it reads `AGENTS.md`
> and knows what sub-projects exist. Cross-harness tools (Cursor, Codex) also auto-detect this file.

---

## Step 4 — Open Claude CLI from the Project Folder

Always launch `claude` from inside the project folder — not from the workspace root.

```powershell
# For portfolio-site:
cd ./portfolio-site
claude

# For weather-app:
cd ./weather-app
claude

# For discord-bot:
cd ./discord-bot
claude
```

Why: Claude Code CLI reads `CLAUDE.md` from the current working directory.
If you run `claude` from the workspace root (`./`), it reads `AGENTS.md` but
not any project's `CLAUDE.md` — meaning it won't know your stack rules.

---

## What ECC Provides Automatically (No Extra Setup)

Once you've done the 4 steps, these work immediately in any project:

| Feature | How it activates | Example usage |
|---------|-----------------|---------------|
| Code review | Claude reads agents from `~/.claude/agents/` | Just ask "review this file" |
| Python rules | Rules in `~/.claude/rules/ecc/python/` | Always active in Python sessions |
| TS/JS rules | Rules in `~/.claude/rules/ecc/typescript/` | Always active in JS/React sessions |
| Universal rules | Rules in `~/.claude/rules/ecc/common/` | Always active in every session |
| TDD workflow | Skill in `~/.claude/skills/tdd-workflow/` | Ask "help me do TDD for this feature" |
| Frontend patterns | Skill in `~/.claude/skills/frontend-patterns/` | Ask "what's the pattern for data fetching in React?" |
| Python patterns | Skill in `~/.claude/skills/python-patterns/` | Ask "best way to structure this in Python?" |

---

## Quick-Reference: Which Agents to Use Per Stack

### Python projects (pyGame, discord-bot, scripts, APIs)
```
Planning a feature   →  planner
Writing code TDD     →  tdd-guide
Reviewing code       →  python-reviewer
Fixing import errors →  build-error-resolver
Security audit       →  security-reviewer
Architecture         →  architect
```

### React / Vite / JS / Tailwind / GSAP projects
```
Planning a feature   →  planner
Writing code TDD     →  tdd-guide
Reviewing code       →  typescript-reviewer
Fixing Vite errors   →  build-error-resolver  (also: react-build-resolver)
Security audit       →  security-reviewer
Architecture         →  architect
```

### Vanilla JS projects
```
Planning a feature   →  planner
Reviewing code       →  typescript-reviewer   (handles JS too)
Security audit       →  security-reviewer
Fixing errors        →  build-error-resolver
```

---

## The Anatomy of a Good CLAUDE.md

Every `CLAUDE.md` must have these 7 sections. Missing any of them means
Claude will make wrong assumptions in that area.

```markdown
# [Project Name] — [One-line description]

## Stack
  What language, framework, libraries, package manager

## Dev Commands
  Exact commands to run/test/build — copy-paste ready

## Project Structure
  Actual folder tree with comments on what lives where

## Known Issues / Gotchas
  Things that will trip Claude up if it doesn't know them upfront
  (wrong imports, env var quirks, run order, etc.)

## Skills to Use
  List from: python-patterns, python-testing, frontend-patterns,
  tdd-workflow, coding-standards, security-review, api-design, etc.

## Code Standards
  Project-specific standards beyond the global ECC rules

## Agent Delegation
  Which specialist agent to use for which class of task
```

---

## Checklist (Print This Out)

```
[ ] 1. Created folder: `./<project-name>/`
[ ] 2. Copied CLAUDE.md template for my stack
[ ] 3. Changed the title line in CLAUDE.md
[ ] 4. Deleted the <!-- TEMPLATE: ... --> comment block
[ ] 5. Updated Stack section with real tech
[ ] 6. Updated Dev Commands with real commands
[ ] 7. Updated Project Structure with real folders
[ ] 8. Added Known Issues / Gotchas
[ ] 9. Added Agent Delegation section
[ ] 10. Updated `./AGENTS.md` projects table
[ ] 11. Opened claude CLI from the project folder (cd + claude)
```

---

## What NOT to Do

| ❌ Don't | ✅ Do Instead |
|---------|-------------|
| Leave `[PROJECT NAME]` placeholder in CLAUDE.md | Replace with your actual project name |
| Run `claude` from the workspace root (`./`) | Run it from inside `./<project>/` |
| Put secrets / API keys in CLAUDE.md | Use `.env` and note the var name in CLAUDE.md |
| Copy ALL template rules if they don't apply | Remove sections that don't apply to your stack |
| Forget to update `AGENTS.md` workspace registry | Always update the Projects table |
| Run the full ECC installer again for new projects | Global rules/agents are already installed — just add CLAUDE.md |

---

## Example: Full Timeline for Adding `portfolio-site`

```
2 min  →  mkdir ./portfolio-site
           cd ./portfolio-site
           npm create vite@latest . -- --template react
           npm install gsap @gsap/react
           npm install -D tailwindcss postcss autoprefixer
           npx tailwindcss init -p

1 min  →  Copy-Item "./_templates/react-vite-tailwind-gsap/CLAUDE.md" .\CLAUDE.md

3 min  →  Edit CLAUDE.md:
           - Change title
           - Delete template comment
           - Update Project Structure to match your src/ layout
           - Add Known Issues for GSAP plugin registration

1 min  →  Edit ./AGENTS.md:
           - Add portfolio-site row to Projects table

0 min  →  cd ./portfolio-site && claude
           ← ECC is live. Claude knows your stack, rules, agents.
```

Total setup time: ~7 minutes.
