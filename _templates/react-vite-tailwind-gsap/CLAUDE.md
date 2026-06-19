# [PROJECT NAME] — React + Vite + Tailwind CSS + GSAP

<!-- 
  TEMPLATE: Copy this file to your project root as CLAUDE.md
  Replace bracketed placeholders with your actual project details
-->

## Stack
- **Framework:** React 18+ with Vite
- **Styling:** Tailwind CSS v3
- **Animations:** GSAP (GreenSock Animation Platform)
- **Language:** JavaScript / JSX  (or TypeScript / TSX if applicable)
- **Package manager:** npm

## Dev Commands
```bash
npm run dev          # Start dev server (Vite, default port 5173)
npm run build        # Production build
npm run preview      # Preview production build locally
npm run lint         # ESLint
```

## Project Structure
```
src/
├── components/        # Reusable React components
├── pages/             # Page-level components (if using react-router)
├── hooks/             # Custom React hooks
├── animations/        # GSAP animation definitions (centralized)
│   └── gsap.config.js # GSAP global config, ScrollTrigger registration
├── styles/            # Global CSS, Tailwind base layer overrides
├── assets/            # Images, fonts, SVGs
└── App.jsx            # Root component
```

## GSAP Rules
- **Always register plugins at app entry point** (`main.jsx` or `gsap.config.js`):
  ```js
  import { gsap } from "gsap";
  import { ScrollTrigger } from "gsap/ScrollTrigger";
  gsap.registerPlugin(ScrollTrigger);
  ```
- **Always use `useGSAP()` hook** (from `@gsap/react`) inside components — never raw `useEffect` for GSAP
- **Always return a cleanup function** or use the `gsap.context()` scope pattern to kill animations on unmount
- **Never mutate DOM directly** — use refs (`useRef`) for GSAP targets
- **Prefer `gsap.timeline()` over chained `.to()` calls** for sequenced animations

## Tailwind CSS Rules
- Use **Tailwind utility classes** in JSX — no inline `style` props unless GSAP sets them dynamically
- Use `@apply` in CSS only for truly reusable component patterns, not one-offs
- Use **Tailwind config** (`tailwind.config.js`) for custom colors, fonts, spacing — never hardcode hex values in JSX
- Responsive: mobile-first (`sm:`, `md:`, `lg:`, `xl:`)

## React / Vite Rules
- **Functional components only** — no class components
- **Custom hooks** for all stateful logic (keep components dumb)
- Keep component files under 200 lines — split if larger
- **Co-locate** component, its CSS module (if any), and its test in the same folder
- Use `React.memo` and `useCallback` only when profiling proves it's needed
- Vite env vars must be prefixed `VITE_` to be exposed to client

## Code Standards
- No `console.log` in committed code (use a logger utility)
- TypeScript strict mode if using TS
- Import order: React → third-party → local components → styles
- All async functions must handle errors (try/catch or `.catch()`)

## Skills to Use
- `frontend-patterns` — React hooks, component patterns, data fetching
- `tdd-workflow` — test with Vitest + React Testing Library
- `coding-standards` — universal clean-code rules
- `security-review` — XSS, dependency audit, CSP headers

## Agent Delegation
- `typescript-reviewer` — for code quality and React patterns
- `code-reviewer` — for general review
- `build-error-resolver` — for Vite build failures
- `security-reviewer` — before any production release

## Dependencies (Install These)
```bash
npm create vite@latest . -- --template react
npm install gsap @gsap/react
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

## Environment Variables
```
VITE_API_URL=          # Backend API base URL
VITE_PUBLIC_KEY=       # Any public keys (NEVER private keys here)
```
