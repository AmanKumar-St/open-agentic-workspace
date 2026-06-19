# Free OpenRouter Models for Agentic Coding

This is a live-fetched list of currently free models on OpenRouter, ranked roughly by their capability for **agentic coding** and complex reasoning tasks. 

> [!TIP]
> To use any of these models, copy the exact **Model String** into your `update_model.ps1` script or `settings.json` file.

## 🏆 Tier 1: Top Performers (Best for Coding & Agents)
These are massive models or models specifically fine-tuned for heavy coding and reasoning tasks.

| Rank | Model Name | Model String (ID) | Notes |
|---|---|---|---|
| 1 | Qwen3 Coder 480B A35B | `qwen/qwen3-coder:free` | Purpose-built for coding tasks, massive scale |
| 2 | Nous Hermes 3 405B Instruct | `nousresearch/hermes-3-llama-3.1-405b:free` | 405B parameter heavyweight; excellent general reasoning |
| 3 | OpenAI gpt-oss-120b | `openai/gpt-oss-120b:free` | Very strong 120B model |
| 4 | NVIDIA Nemotron 3 Ultra | `nvidia/nemotron-3-ultra-550b-a55b:free` | 550B parameters; massive knowledge base |
| 5 | Meta Llama 3.3 70B Instruct | `meta-llama/llama-3.3-70b-instruct:free` | Reliable, well-steered, and extremely popular for agents |

## 🥈 Tier 2: Strong Contenders & Specialized Coders
Very capable models that are slightly smaller, but highly optimized or specifically trained for code.

| Rank | Model Name | Model String (ID) | Notes |
|---|---|---|---|
| 6 | Poolside Laguna M.1 | `poolside/laguna-m.1:free` | Poolside models are specifically trained for software engineering |
| 7 | Cohere North Mini Code | `cohere/north-mini-code:free` | Specialized coding model by Cohere |
| 8 | Qwen3 Next 80B A3B Instruct | `qwen/qwen3-next-80b-a3b-instruct:free` | Excellent reasoning capabilities |
| 9 | NVIDIA Nemotron 3 Super | `nvidia/nemotron-3-super-120b-a12b:free` | Strong 120B model |
| 10 | Google Lyria 3 Pro Preview | `google/lyria-3-pro-preview` | Solid Google foundational model |
| 11 | Poolside Laguna XS.2 | `poolside/laguna-xs.2:free` | Smaller variant of Poolside's coding model |

## 🥉 Tier 3: Good for Fast/Simple Tasks
Smaller or experimental models. Great for quick queries, formatting, or simple scripts, but might struggle with complex agentic loops.

| Rank | Model Name | Model String (ID) | Notes |
|---|---|---|---|
| 12 | Google Gemma 4 31B | `google/gemma-4-31b-it:free` | Solid mid-size model |
| 13 | Google Gemma 4 26B A4B | `google/gemma-4-26b-a4b-it:free` | Efficient MoE architecture |
| 14 | OpenAI gpt-oss-20b | `openai/gpt-oss-20b:free` | Fast and capable 20B |
| 15 | Venice: Uncensored 24B | `cognitivecomputations/dolphin-mistral-24b-venice-edition:free` | Uncensored Mistral fine-tune |
| 16 | NVIDIA Nemotron 3 Nano Omni | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | Good reasoning for its size |

## 🪶 Tier 4: Lightweight & Niche Models
Use these if you need extreme speed or specific modalities (like thinking/vision).

| Model Name | Model String (ID) | Notes |
|---|---|---|
| Liquid LFM2.5 1.2B Thinking | `liquid/lfm-2.5-1.2b-thinking:free` | Small but features a thinking/reasoning phase |
| Liquid LFM2.5 1.2B Instruct | `liquid/lfm-2.5-1.2b-instruct:free` | Fast small Liquid foundation model |
| Meta Llama 3.2 3B Instruct | `meta-llama/llama-3.2-3b-instruct:free` | Meta's smallest capable model |
| NVIDIA Nemotron 3 Nano 30B | `nvidia/nemotron-3-nano-30b-a3b:free` | Lightweight NVIDIA model |
| NVIDIA Nemotron Nano 12B VL | `nvidia/nemotron-nano-12b-v2-vl:free` | Vision-Language model |
| NVIDIA Nemotron Nano 9B V2 | `nvidia/nemotron-nano-9b-v2:free` | Very small NVIDIA model |
| Nex AGI Nex-N2-Pro | `nex-agi/nex-n2-pro:free` | Niche |
| Google Lyria 3 Clip Preview | `google/lyria-3-clip-preview` | Niche/Specialized |
| NVIDIA Nemotron 3.5 Content Safety| `nvidia/nemotron-3.5-content-safety:free` | Guardrail/safety model |

## 🔀 Auto-Routers
These endpoints don't point to a single model. Instead, OpenRouter dynamically routes your prompt to a free model based on availability.

| Model Name | Model String (ID) |
|---|---|
| Free Models Router | `openrouter/free` |
| Owl Alpha | `openrouter/owl-alpha` |
