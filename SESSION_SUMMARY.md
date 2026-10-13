# SESSION_SUMMARY — the entire context, compacted

*Everything built in this workspace, what it is, where it lives, and how it fits together.
Workspace root: `D:\aria\Projects` · GitHub: `github.com/AkshayJohn03` · Owner: Akshay John Xavier.*

---

## 1. The mission arc (how this all happened)

1. **Fix BrandMorph** (`ChangeMy_powerpoint`) — it decompiled decks and rebuilt them from blank layouts with 5 hardcoded colors, destroying charts/tables/layouts. Diagnosed, redesigned, rebuilt as an in-place OOXML transformation engine.
2. **15 ideas → 7 new systems** — the ideas you listed were grouped into coherent products (gateway, evals, security, forensics, orchestration, distillation, vertical RAG), each with a competitive wedge against named incumbents.
3. **Enterprise hardening** — an interviewer-style assessment found the gaps (decorative auth, no durable state, unpinned deps, asserted-not-proven integration); all were closed with code, CI, and threat models.
4. **Competitive wedge round** — your own industry analysis became ROADMAP.md; three build waves shipped the unclaimed territory (MCP firewall, seam auditing, tool-abuse pentesting, AI SIEM).
5. **The tutor layer** — 10 whiteboard video lectures + 10 GLOSSARY.md study docs + PipelineViz, so you can learn your own platform.

**Totals: 12 GitHub repos · ~1,240 offline-passing tests · 10 videos (~62 min) · scorecard average 9.3/10.**

---

## 2. The systems (what each one is)

| Repo | What it is | Wedge vs incumbents | Tests | Key measured evidence |
|---|---|---|---|---|
| **AegisGate** | Self-healing LLM gateway: identity (JWT + hashed keys), rate limiting, semantic cache, routing w/ circuit breakers + hedging, cost autopilot, feature flags, usage ledger, **Agent Tool & MCP Firewall**, PII round-trip | LiteLLM/Bifrost/Portkey stop at chat — AegisGate inspects **LLM→tool payloads** (SQLi, SSRF, traversal, priv-esc) and pseudonymizes PII both directions | 175 | 484 rps, p95 60ms (measured); live curl: `rm -rf /` → deny |
| **VerdictAI** | LLM-as-judge with human calibration, eval dataset generator, regression gates, eval-service API, **Seam Auditor** | DeepEval/Ragas are single-hop — VerdictAI measures **agent handoff degradation**: fidelity half-life, blame attribution | 228 | kappa 0.5 fixture; planted −19% caught, exit 1; PAV 2.5→3.75 |
| **ForensiQ** | Failure forensics — traces in (Langfuse/OTLP/JSONL), failure taxonomy, blame ranking, drift alarms, causal-chain post-mortems, session replay | Langfuse/Phoenix are dashboards; ForensiQ is **SIEM for AI** — incident response with a causal chain | 210 | precision/recall 1.0 on planted failures; blame top-1 100% |
| **RedForge** | Red-team harness + layered injection defense; declarative `redforge.yaml`; **tool-abuse attacks that actually execute** (SQLite SQLi, SSRF metadata, traversal); OWASP + NIST AI RMF + EU AI Act mapping; adaptive crescendo | Promptfoo/Garak attack text; RedForge attacks **tool boundaries** | 56 | Vulnerable ASR 94.3% → hardened 0.0% |
| **SwarmResearch** | Multiagent deep-research on a hand-rolled runtime (DAG, checkpoint/resume, human-in-loop, citations) | No LangGraph — zero framework lock-in, proven crash-safety | 85 | hallucination rate 0.0; planted contradiction surfaced |
| **Model-Distillery** | Distillation pipeline: teacher data → MinHash dedup → rejection sampling → decontamination → QLoRA plan/KD → exam vs teacher → breakeven | 122 → 59 kept → 68.6% retention, byte-identical runs | 114 | hand-computed KD-loss fixture |
| **HVAC-Copilot** | Multimodal RAG for technicians: section-aware chunking, hybrid BM25+dense+RRF, fault-code fast path, safety escalation | Industrial incumbents bind to their own ecosystems; this targets unstructured OEM manuals | 38 | recall@5 = 1.0, zero safety violations |
| **BrandMorph** (`ChangeMy_powerpoint`) | In-place deck re-branding: theme surgery, Lab-space role-preserving color mapping, fit guard, PII-safe hostile-deck defenses, batch CLI/API | Rebuild-approach clones destroy content — this preserves it | 43 | 65 audited changes, idempotent, demo committed |
| **PlatformDemo** | The vertical integration proof: HVAC → gateway → spans → ForensiQ → VerdictAI gate | Composition claim = runnable artifact | 11 | 6,578 tokens metered; 44 spans; gate exit 0→1 |
| **PipelineViz** | Interactive 3D scrollytelling of the whole journey (GSAP ScrollTrigger + Three.js), workflow diagrams, 69 tooltip definitions | bbycroft.net/llm-style, browser-verified | — | live at 127.0.0.1:5173 during dev |

**Shared contract:** every system speaks the same `LLMClient`/`EmbeddingClient` protocols with deterministic offline mocks, emits ForensiQ-compatible spans, and passes its suite with zero network/keys.

---

## 3. The enterprise round (what the assessment found and what closed)

| Gap found | Closed by |
|---|---|
| Decorative auth | JWT (HS256, exp/aud/iss) + static keys SHA-256-hashed + rotation window; API-key auth on HVAC/Swarm/VerdictAI services |
| No durable state | SQLite/WAL append-only usage ledger (restart-safe autopilot), budgets, audit log, GDPR tenant deletion |
| Unpinned deps / supply chain | constraints.txt, blocking pip-audit, SBOM, Dependabot (12 repos), coverage gates |
| API hygiene | Idempotency keys, request caps, /v1 versioning with Sunset headers, correlation IDs, HMAC-signed webhooks |
| Not operational | Prometheus alerts, RUNBOOK.md, measured load profile (484 rps / p95 60ms), eval-service API |
| Asserted integration | **PlatformDemo** — one offline run proving the whole lifecycle |

---

## 4. The tutor layer (learn your own platform)

- **[TUTOR_BRIEF.md](TUTOR_BRIEF.md)** — master instruction for the video series + per-repo lecture outlines + study order.
- **10 videos** (~6 min each, narrated, keywords defined on screen) at `<repo>/brag-output/brag.mp4` — index in the portfolio README.
- **10 GLOSSARY.md files** — ~640 keyword definitions ("why it matters here").
- **[PipelineViz](PipelineViz/)** — the interactive version: vertical 3D journey, workflow diagrams, keyword chips, replay button.
- **Recommended study order:** map → AegisGate → HVAC → VerdictAI → ForensiQ → RedForge → Swarm → Distillery → BrandMorph → PlatformDemo.

---

## 5. Strategy documents

| File | What it holds |
|---|---|
| [ROADMAP.md](ROADMAP.md) | The OSS wedge plan vs LiteLLM/DeepEval/Promptfoo/Langfuse — waves 1-3 all complete |
| [LINKEDIN_PLAYBOOK.md](LINKEDIN_PLAYBOOK.md) | Positioning, 7-post series, website tie-in, free signal loops |
| [TUTOR_BRIEF.md](TUTOR_BRIEF.md) | The video-series master brief |
| [README.md](README.md) | Portfolio index: systems table, integration map, scorecard (9.3/10), episode index |

**The DevSecOps lifecycle (the one-line strategy):** RedForge + VerdictAI gate development → AegisGate + ForensiQ guard production → incidents feed playbooks → back to development.

---

## 6. Where everything lives

| Path | Repo |
|---|---|
| `D:\aria\Projects\AegisGate` | github.com/AkshayJohn03/AegisGate |
| `D:\aria\Projects\VerdictAI` | github.com/AkshayJohn03/VerdictAI |
| `D:\aria\Projects\ForensiQ` | github.com/AkshayJohn03/ForensiQ |
| `D:\aria\Projects\RedForge` | github.com/AkshayJohn03/RedForge |
| `D:\aria\Projects\SwarmResearch` | github.com/AkshayJohn03/SwarmResearch |
| `D:\aria\Projects\Model-Distillery` | github.com/AkshayJohn03/Model-Distillery |
| `D:\aria\Projects\HVAC-Copilot` | github.com/AkshayJohn03/HVAC-Copilot |
| `D:\aria\Projects\BrandMorph` | github.com/AkshayJohn03/ChangeMy_powerpoint |
| `D:\aria\Projects\PlatformDemo` | github.com/AkshayJohn03/PlatformDemo |
| `D:\aria\Projects\PipelineViz` | github.com/AkshayJohn03/PipelineViz |
| `D:\aria\Projects` (this root) | github.com/AkshayJohn03/AI-Portfolio |
| `D:\aria\Projects\_banners\` | Social preview images (upload per repo: Settings → Social preview) |
| `D:\aria\Projects\_reference\` | Cloned references (RAG_showcase) |

---

## 7. How to run anything

```bash
# any Python repo
cd <repo> && pip install -e . && python -m pytest tests -q     # offline, no keys

# the interactive site
cd PipelineViz && npm install && npm run dev                     # 127.0.0.1:5173

# the integration proof
cd PlatformDemo && python demo/pipeline_demo.py

# a red-team campaign
cd RedForge && python -m redforge.cli run --config redforge.yaml
```

## 8. Open threads (deliberate, not forgotten)

- Qloo Agentic Hackathon (Oct 30, $25k) — plan ready; awaiting your go to register + scaffold MUSE.
- PipelineViz → Vercel deploy (public link for resume/interviews).
- LinkedIn 7-post series — playbook ready; drafts on request.
- Per-repo remaining-to-10 items listed in the portfolio scorecard.
