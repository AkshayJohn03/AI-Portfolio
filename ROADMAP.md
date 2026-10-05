# ROADMAP — From portfolio to industry-standard OSS tools

Owner-approved competitive strategy (Sep 30, 2026). Positioning per repo, the wedge
that beats incumbents, and the build waves. Golden rules: 3-minute time-to-value,
zero-invasive integration (OpenAI base_url swap + OpenTelemetry), own the unclaimed
pain points (MCP/tool security, cross-agent data loss, incident post-mortems).

## Wave 1 — The wedges (COMPLETE — verified: 175+228 tests, live curl ergonomics proof)

### AegisGate — wedge: "Agent Tool & MCP Firewall"
- [x] `mcp_firewall.py`: deterministic tool-call inspector — arg schema validation,
      dangerous-command patterns (rm -rf / DROP TABLE / sudo / curl|bash), SSRF
      (private IPs, 169.254.169.254, file://), path traversal, privilege-escalation
      verbs, per-tool allowlists. Decision: allow/deny/sanitize + reasons.
- [x] Gateway endpoints: POST /v1/tools/inspect + /v1/mcp/inspect; settings.intercept_tools.
- [x] `pii.py`: PII round-trip — detect (email/phone/name/card heuristics), pseudonymize
      in (John Doe → User_123, consistent mapping), restore on response. Optional stage.
- [x] "Drop-in" docs: one-line base_url swap example; verify OpenAI response shape.
- [x] Tests offline (SSRF/SQLi/rm-rf/priv-esc/schema/PII round-trip).

### VerdictAI — wedge: "Seam Auditor for multi-agent handoffs"
- [x] `pytest_plugin.py` (entry point pytest11): `verdict` fixture, pass/fail exit codes.
- [x] `deterministic.py`: deterministic-first suite (schema conformity, bounds, JSON
      validity, cosine-threshold via hash embedding) — LLM judge only on escalation.
- [x] `seams.py`: HandoffAuditor — field-level diff between consecutive agent steps
      (dropped/mutated/typed-changed), fidelity score per handoff, `fidelity_halflife`,
      `blame()` → worst node.
- [x] `report.py`: self-contained HtmlDiffReport (inline CSS, steps×fields matrix,
      dropped/mutated color coding) — Playwright-report feel.
- [x] CLI: `verdict audit --steps trace.json --html report.html`.

## Wave 2 — Declarative + OTel (COMPLETE — RedForge 56 tests, ForensiQ 210 tests, both pushed)

### RedForge — wedge: "Automated pentester for agents with tools"
- [x] `redforge.yaml` declarative config (target, attack set, defenses, gate thresholds).
- [x] Tool-abuse attack suite: forced unauthorized tool calls, SSRF via web tools,
      SQLi through agent DB tools, MCP tool confusion.
- [x] Compliance mapping in reports: OWASP LLM Top 10 (exists) + NIST AI RMF + EU AI Act.
- [x] Adaptive multi-turn: attacker consumes target responses and escalates (stateful).

### ForensiQ — wedge: "SIEM for AI — the black box flight recorder"
- [x] OTel ingestion: accept OTLP JSON exports (OTEL_EXPORTER_OTLP_ENDPOINT compatible).
- [x] DuckDB store adapter for high-throughput trace writes (embedded, offline-friendly).
- [x] Incident Post-Mortem: single-page causal chain (trigger prompt → poisoned context →
      validator failures) — extend RCA generator.
- [x] Session replay: step-through state inspection CLI (state at Tn).

## Wave 3 — Repositioning + proof
- [ ] All 5 READMEs: new identities, 3-minute quickstarts, integration diagram
      (RedForge+VerdictAI in CI → AegisGate+ForensiQ in prod).
- [ ] HVAC-Copilot: multimodal wiring-diagram cross-reference spike; enterprise-hardening
      proof wired through PlatformDemo.
- [ ] Scorecard re-score after waves.

## Explicit non-goals this cycle
- Go/Rust single-binary port (roadmap note in AegisGate README; latency story documented
  with measured profiles instead).
- Braintrust/DeepEval feature parity chase — we win on the seam, not the checklist.
