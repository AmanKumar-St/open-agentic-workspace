# Crafting Custom `CLAUDE.md` Stack Templates

While the `_templates` directory provides a few ready-made configurations, the true power of the CLAUD workspace lies in its flexibility. You can create a highly tailored `CLAUDE.md` file for **any technology stack** (Python, Node.js, Go, Rust, Ruby, etc.). 

This guide will teach you the anatomy of a perfect `CLAUDE.md` file so you can define custom environments that perfectly suit your projects.

---

## 🧠 Why `CLAUDE.md` Matters

Anthropic's Claude Code CLI looks for a `CLAUDE.md` file in the root of your project directory whenever it starts. It treats this file as a **system prompt / supreme rulebook**. 

If you configure this file correctly, the AI will:
- Instantly know what language, framework, and exact version to use.
- Never hallucinate outdated dependencies or use libraries you hate.
- Format code exactly to your preference (tabs vs spaces, types vs interfaces).
- Know exactly how to run tests and build the code to verify its own work.

---

## 🦴 Core Anatomy of a Great Template

Every robust stack template should include the following 5 sections:

### 1. The Role / Identity
Tell the AI exactly what kind of expert it needs to be. Setting the persona drastically improves the quality of the generated code.
> *"You are an Expert Node.js Backend Developer specializing in scalable microservices."*

### 2. Tech Stack & Versions
List the exact frameworks and their versions. This prevents the AI from using deprecated APIs (like React Class Components or Express v3).
> *- Language: TypeScript v5.x*
> *- Framework: Express v4.x*
> *- Database: PostgreSQL with Prisma ORM*

### 3. Project Structure Tree
Provide a visual map of where files should go. If you don't provide this, the AI might dump all code into a single `main.js` file. Tell it exactly where controllers, routes, and models live.

### 4. Build, Run, and Test Commands
Provide the exact terminal commands required to run the project. Since the agent can run bash commands, it will use these scripts to test its code before showing it to you.
> *- Build: `npm run build`*
> *- Test: `npm run test`*

### 5. Strict Rules & Anti-Patterns
This is the most important section. List things the AI must **always** do and **never** do. 
> *- Never use `var`.*
> *- Always use `camelCase` for variables.*
> *- Do not write inline CSS.*

---

## 🛠️ Step-by-Step Guide: Adding a New Template

To create a reusable template for your workspace:

1. Navigate to the `_templates` folder: `e:\CLAUD\_templates\`
2. Create a new subfolder for your stack (e.g., `nodejs-express-typescript`).
3. Inside that folder, create a file named `CLAUDE.md`.
4. Copy the structure below and adapt it to your stack!

---

## 💡 Example: Node.js + Express + TypeScript

Here is an example of what a high-quality custom template looks like for a popular backend framework:

```markdown
# Node.js + Express Backend Workspace

You are an Expert Node.js Backend Developer specializing in highly scalable, secure, and well-tested microservices using TypeScript and Express.

## Core Tech Stack
- **Runtime:** Node.js v20+
- **Language:** TypeScript
- **Framework:** Express.js v4
- **Database ORM:** Prisma
- **Testing:** Jest + Supertest

## Directory Structure Enforcement
All code must be organized into this standard MVC structure:
```text
src/
├── controllers/    # Request handlers (logic)
├── routes/         # Express route definitions
├── services/       # Business logic / DB calls
├── middlewares/    # Custom Express middlewares
├── models/         # Prisma schemas / Type definitions
└── index.ts        # App entry point
```

## Available Commands
Whenever you add new features or modify existing code, you MUST run tests to verify your changes using these commands:
- Start dev server: `npm run dev`
- Run typecheck: `npm run typecheck`
- Run tests: `npm run test`

## Strict Coding Rules
1. **Types over Interfaces:** Prefer TypeScript `type` aliases over `interface`.
2. **Error Handling:** Every route MUST use the centralized `asyncHandler` middleware to catch errors. Never use standard `try/catch` blocks inside controllers.
3. **No 'any' Types:** Never use `any`. Always define strict types or use `unknown` if truly dynamic.
4. **Environment Variables:** Never hardcode secrets. Always use `process.env.VARIABLE_NAME`.
```

---

With this guide, you can now seamlessly expand your `CLAUD` workspace to support any framework or technology you desire!
