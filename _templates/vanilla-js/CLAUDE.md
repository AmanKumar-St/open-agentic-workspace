# [PROJECT NAME] — Vanilla JavaScript

<!--
  TEMPLATE: Copy this file to your project root as CLAUDE.md
  Replace bracketed placeholders with your actual project details
-->

## Stack
- **Language:** Vanilla JavaScript (ES2022+)
- **Styling:** CSS / GSAP (if animations needed)
- **Bundler:** None (or Vite if bundling needed)
- **Runtime:** Browser

## Dev Commands
```bash
# No bundler - open index.html directly, or:
npx serve .           # Simple static server on port 3000
# If using Vite:
npm run dev
```

## Project Structure
```
project/
├── index.html         # Entry point
├── src/
│   ├── main.js        # App entry, event listeners
│   ├── modules/       # ES module files (one concern per file)
│   └── utils/         # Shared utility functions
├── styles/
│   ├── main.css       # Global styles
│   └── components/    # Component-scoped CSS
└── assets/            # Images, fonts
```

## JavaScript Rules
- Use **ES modules** (`import`/`export`) — no global variables, no var
- **No jQuery** — use native `document.querySelector`, `fetch`, `addEventListener`
- All async operations use `async/await` with try/catch
- **Event delegation** over adding listeners to many individual elements
- Use `const` by default; `let` only when reassignment is needed; never `var`
- DOM queries cached in variables — never query the DOM in a loop

## GSAP Rules (if used)
- Register plugins once at top of `main.js`
- Always clean up animations on page transitions or component removal
- Use `gsap.context()` for scoped animation cleanup

## Code Standards
- No `console.log` in committed code
- JSDoc comments on exported functions
- Files under 200 lines — split into modules if larger
- Group imports: browser APIs → third-party → local modules

## Skills to Use
- `coding-standards` — clean code, naming conventions
- `security-review` — XSS prevention (never `innerHTML` with user data)
- `frontend-patterns` — DOM patterns, event handling
- `tdd-workflow` — test with Vitest or Jest

## Agent Delegation
- `typescript-reviewer` — JS/JSX code quality
- `code-reviewer` — general review
- `security-reviewer` — XSS/injection audit before deploy
