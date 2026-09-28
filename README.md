# AI Infrastructure Portfolio — Akshay John Xavier

Eight production-grade systems covering the full lifecycle of LLM applications: **build → serve → observe → evaluate → secure → compress**. Each repository is independently deployable, and each exposes clean interfaces so the others can plug into it — the portfolio composes into a single platform.

```
                        ┌─────────────────────────────────────────────┐
                        │              AI-Portfolio map               │
                        └─────────────────────────────────────────────┘

  BUILD                SERVE                 OBSERVE              ASSURE
  ┌──────────────┐    ┌──────────────┐     ┌──────────────┐    ┌──────────────┐
  │ SwarmResearch│    │  AegisGate   │◄────│   ForensiQ   │    │  VerdictAI   │
  │ multiagent   │    │ self-healing │     │  failure     │    │ judge+human  │
  │ research     │    │ gateway:     │     │  forensics   │    │ calibration  │
  │ orchestrator │    │ routing, RL, │     │ (Langfuse,   │    │ regression   │
  │              │    │ fallback,    │     │  RAG_showcase│    │ detection    │
  │              │    │ semantic     │     │  compatible) │    └──────┬───────┘
  │              │    │ cache, cost  │     └──────┬───────┘           │
  │              │    │ autopilot,   │            │                   ▼
  │              │    │ feature flags│     ┌──────┴───────┐    ┌──────────────┐
  │              │    └──────┬───────┘     │  RedForge    │    │  Model-      │
  │              │           │             │ red team +   │    │  Distillery  │
  │              │           │             │ injection    │    │ SFT data →   │
  │              │           ▼             │ defense      │    │ QLoRA →      │
  │      ┌───────┴────────┴────────┐     └──────┬───────┘    │ quantize →   │
  │      │ DOMAIN APPLICATIONS     │            │            │ eval → serve │
  │      │ HVAC-Copilot (multimodal│◄───────────┘            └──────┬───────┘
  │      │ RAG) · BrandMorph (deck │  attacks both as targets       │
  │      │ re-branding engine)     │                                │
  │      └─────────────────────────┘     every system ◄──────────────┘
  └──────────────────────────────────────── evaluated by VerdictAI,
                                          traced via ForensiQ, routed by AegisGate
```

## The systems

| # | Repository | One-liner | Ideas covered |
|---|-----------|-----------|---------------|
| 1 | **[AegisGate](AegisGate/)** | Self-healing LLM gateway & control plane: adaptive routing with circuit breakers, tenant rate limiting, fallback chains, semantic caching, cost autopilot, model feature flags + a self-healing documentation bot as its flagship consumer | Self-healing LLM gateway · self-healing doc bot · rate limiting + fallback routing · semantic cache · LLM cost autopilot · AI feature flags |
| 2 | **[VerdictAI](VerdictAI/)** | LLM-as-judge with statistical human calibration (bias-aware: position, verbosity, self-preference; isotonic recalibration), automated eval dataset generation, and model regression detection with CI gates | LLM-as-judge w/ human calibration · automated eval dataset generator · model regression detection |
| 3 | **[Model-Distillery](Model-Distillery/)** | End-to-end distillation pipeline: diversity-driven synthetic SFT data, quality filtering, QLoRA training + logit-KD reference, quantization (GGUF/AWQ), teacher-vs-student eval, serving configs | Model distillation pipeline |
| 4 | **[RedForge](RedForge/)** | Automated red-team harness (evolutionary attack generation, OWASP LLM Top-10 taxonomy, ASR metrics, CI gates) + layered prompt-injection defenses, demonstrated on a recruiting assistant that ingests untrusted resumes | Automated red team harness · prompt-injection defense for recruiting assistants |
| 5 | **[ForensiQ](ForensiQ/)** | Failure forensics for AI pipelines: Langfuse trace ingestion, stage-level failure taxonomy, root-cause attribution with counterfactual replay, pattern mining + drift alerts, RCA report generation. Reads RAG_showcase-style pipelines natively | Failure forensics tool for AI pipelines |
| 6 | **[SwarmResearch](SwarmResearch/)** | Multiagent deep-research assistant on a hand-rolled async orchestration runtime (DAG planner/executor/critic, checkpoint+resume, human-in-loop, streaming) with citation-grounded report synthesis | Multiagent research assistant · agent orchestration system |
| 7 | **[HVAC-Copilot](HVAC-Copilot/)** | Multimodal document processor → RAG assistant for HVAC technicians: layout-aware ingestion (tables, diagrams, fault-code tables), hybrid BM25+dense+rerank retrieval, diagram-aware QA, safety-critical escalation guardrails | Multimodal document processor · multimodal RAG for HVAC technicians |
| 8 | **[BrandMorph](BrandMorph/)** | PowerPoint re-branding engine, rebuilt: in-place OOXML theme surgery + role-aware color/font mapping (no more rebuild-and-destroy), brand-guideline ingestion (BrandDNA), length-budgeted copy rewriting, fit guards, full change reports | Fixes `ChangeMy_powerpoint` |

Also in this workspace: `_reference/RAG_showcase` — the existing flagship RAG pipeline that ForensiQ instruments and RedForge attacks.

## How they interconnect (the "why" behind the interfaces)

- **Every system speaks the same `LLMClient` / `EmbeddingClient` protocols** (OpenAI-compatible + offline mock implementations), so any two systems compose without glue code.
- **AegisGate serves everyone**: point any system's `LLMClient` at the gateway URL and it inherits rate limiting, fallback, caching, cost policies, and feature-flagged model rollouts with zero code changes.
- **ForensiQ observes everyone**: systems emit ForensiQ-compatible spans (same span schema as RAG_showcase's Langfuse traces). Failures flow into the taxonomy automatically.
- **VerdictAI evaluates everyone**: eval datasets, judge scores, and regression gates are cross-project; Model-Distillery reuses VerdictAI judges for data filtering and student eval.
- **RedForge attacks the domain apps**: the recruiting assistant is a built-in target; the HVAC-Copilot's untrusted-manual ingestion is the indirect-injection target.
- **Model-Distillery closes the cost loop**: AegisGate's cost autopilot flags "this task doesn't need the big model" → Distillery produces the small model → VerdictAI certifies it → AegisGate routes to it.

## Reproduction & quality bar

Every repo: `python -m pytest -q` passes **offline** (deterministic mock LLM/embedding clients — no API keys required to run the test suites), ruff-clean, MIT licensed, with architecture decisions and their trade-offs documented in the README. Real provider calls are opt-in via `.env` (see each repo's `.env.example`).
