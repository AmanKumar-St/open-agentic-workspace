# CLAUD Workspace — Project Registry

## About This Workspace
Multi-project development workspace. Each subdirectory is an independent project.
Always read the project's `CLAUDE.md` before working on any project.

## Projects

| Project | Stack | Directory | Status |
|---------|-------|-----------|--------|
| pyGame / Snake | Python + pygame | `./pyGame/` | Active |

## Adding a New Project
When I add a new project, I will:
1. Create a folder under `e:\CLAUD\`
2. Copy the relevant template from `e:\CLAUD\_templates\` as the project's `CLAUDE.md`
3. Update the Projects table above

## Stack Templates Available
- **React + Vite + Tailwind + GSAP** → copy from `_templates/react-vite-tailwind-gsap/CLAUDE.md`
- **Vanilla JavaScript** → copy from `_templates/vanilla-js/CLAUDE.md`
- **Python** → copy from `pyGame/CLAUDE.md` as a starting point

## Global Standards (All Projects)
- Always read the project's `CLAUDE.md` first
- Run commands from the project root unless CLAUDE.md specifies otherwise
- Never commit secrets or API keys
- Test before committing — each project specifies its test command
- Use the ECC skills and agents listed in each project's CLAUDE.md

## Model & Environment
- Model: openai/gpt-oss-120b:free (via OpenRouter)
- Python: d:\Downloads\python\python.exe
- IDE: Antigravity IDE + Claude Code CLI

## Agent Delegation Quick Reference
| Need | Agent |
|------|-------|
| Plan a feature | planner |
| Review Python code | python-reviewer |
| Review JS/TS/React | typescript-reviewer |
| Fix build/import errors | build-error-resolver |
| Security audit | security-reviewer |
| General code review | code-reviewer |
| TDD guidance | tdd-guide |
| Architecture decisions | architect |
