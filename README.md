# 🚀 CLAUD Workspace 

<div align="center">
  <a href="https://github.com/affaan-m/ECC.git">
    <img src="https://img.shields.io/badge/ECC-Repository-blue?style=for-the-badge&logo=github" alt="ECC Repository" />
  </a>
  <a href="https://openrouter.ai/">
    <img src="https://img.shields.io/badge/OpenRouter-Free_Models-orange?style=for-the-badge&logo=openai" alt="OpenRouter" />
  </a>
</div>

Welcome to the **CLAUD Workspace**! This repository is designed to be your ultimate, zero-cost agentic coding environment. We warmly welcome all users to openly use, modify, and build upon this workspace for their own projects!

## 📋 Prerequisites
Before diving in, ensure you have the core tools installed:
1. **Claude Code CLI**: This workspace relies on the official Anthropic CLI. Install it globally:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
2. **ECC (Everything Claude Code)**: This workspace is heavily powered by the ECC framework. You **must** install the ECC plugin to make this environment work as intended. Please refer to the [official ECC Repository](https://github.com/affaan-m/ECC.git) for detailed installation instructions before proceeding. Without ECC, the templates and agent prompts will not function.

## 📖 Table of Contents: The Perfect Flow
To get the most out of this workspace, we recommend following these guides in a specific order:

1. **Setup Free AI Models**
   - [Step 1: Choose a Free OpenRouter Model](./USE_GUIDE/Free_Open_router_model.md)
   - [Step 2: Change the Workspace Model](./USE_GUIDE/futureModelChange.md)
2. **Using the Workspace**
   - [Step 3: Create a New Project](./USE_GUIDE/NewProjectGuide.md)
   - [Step 4: Tech Stack & Architecture Rules](./USE_GUIDE/Claude_Tech_stack_Guide.md)
   - [Step 5: Using ECC Without the Plugin](./USE_GUIDE/UseWithoutPlugin.md)
3. **Deep Dive**
   - [Comprehensive ECC Documentation](./USE_GUIDE/ECC%20README.md)

## ✨ What Makes This Workspace Great?
The `CLAUD` folder is more than just a directory—it's a fully configured, multi-project workspace supercharged by the **Enhanced Claude Code (ECC)** architecture. It provides:
- **Pre-configured Agent Workflows:** Immediate access to specialized subagents (like planners, code reviewers, security auditors, and architecture designers).
- **Template-Driven Development:** Ready-to-use stack templates for rapid project scaffolding.
- **Budget-Friendly AI:** You don't need a premium Anthropic subscription to experience these advanced agentic tools!

## 🧠 Harnessing ECC Power... For Free!
By default, Anthropic's Claude Code CLI requires a paid subscription to access their proprietary models. However, this workspace is designed to skillfully bypass that requirement. 

By editing `.claude/settings.json` and rerouting the API requests through **OpenRouter**, we unlock the ability to power the ECC architecture using incredibly capable, **100% free open-source models** (such as DeepSeek, Qwen Coder, and Llama 3). 

For a complete walkthrough on how to do this—including how to use our automated `update_model.ps1` script to apply your model of choice across all agents—please follow the **Setup Free AI Models** steps in the Table of Contents above. This ensures you get the premium, multi-agent coding experience entirely for free!

---
*Happy Coding! Let's build something amazing.*
