# ROADMAP — From portfolio to industry-standard OSS tools

Owner-approved competitive strategy (Sep 30, 2026). Positioning per repo, the wedge
that beats incumbents, and the build waves. Golden rules: 3-minute time-to-value,
zero-invasive integration (OpenAI base_url swap + OpenTelemetry), own the unclaimed
pain points (MCP/tool security, cross-agent data loss, incident post-mortems).

## Wave 1 — The wedges (IN PROGRESS)

### AegisGate — wedge: "Agent Tool & MCP Firewall"
- [ ] `mcp_firewall.py`: deterministic tool-call inspector — arg schema validation,
      dangerous-command patterns (rm -rf / DROP TABLE / sudo / curl|bash), SSRF
      (private IPs, 169.254.169.254, file://), path traversal, privilege-escalation
      verbs, per-tool allowlists. Decision: allow/deny/sanitize + reasons.
- [ ] Gateway endpoints: POST /v1/tools/inspect + /v1/mcp/inspect; settings.intercept_tools.
- [ ] `pii.py`: PII round-trip — detect (email/phone/name/card heuristics), pseudonymize
      in (John Doe → User_123, consistent mapping), restore on response. Optional stage.
- [ ] "Drop-in" docs: one-line base_url swap example; verify OpenAI response shape.
- [ ] Tests offline (SSRF/SQLi/rm-rf/priv-esc/schema/PII round-trip).

### VerdictAI — wedge: "Seam Auditor for multi-agent handoffs"
- [ ] `pytest_plugin.py` (entry point pytest11): `verdict` fixture, pass/fail exit codes.
- [ ] `deterministic.py`: deterministic-first suite (schema conformity, bounds, JSON
      validity, cosine-threshold via hash embedding) — LLM judge only on escalation.
- [ ] `seams.py`: HandoffAuditor — field-level diff between consecutive agent steps
      (dropped/mutated/typed-changed), fidelity score per handoff, `fidelity_halflife`,
      `blame()` → worst node.
- [ ] `report.py`: self-contained HtmlDiffReport (inline CSS, steps×fields matrix,
      dropped/mutated color coding) — Playwright-report feel.
- [ ] CLI: `verdict audit --steps trace.json --html report.html`.

## Wave 2 — Declarative + OTel

### RedForge — wedge: "Automated pentester for agents with tools"
- [ ] `redforge.yaml` declarative config (target, attack set, defenses, gate thresholds).
- [ ] Tool-abuse attack suite: forced unauthorized tool calls, SSRF via web tools,
      SQLi through agent DB tools, MCP tool confusion.
- [ ] Compliance mapping in reports: OWASP LLM Top 10 (exists) + NIST AI RMF + EU AI Act.
- [ ] Adaptive multi-turn: attacker consumes target responses and escalates (stateful).

### ForensiQ — wedge: "SIEM for AI — the black box flight recorder"
- [ ] OTel ingestion: accept OTLP JSON exports (OTEL_EXPORTER_OTLP_ENDPOINT compatible).
- [ ] DuckDB store adapter for high-throughput trace writes (embedded, offline-friendly).
- [ ] Incident Post-Mortem: single-page causal chain (trigger prompt → poisoned context →
      validator failures) — extend RCA generator.
- [ ] Session replay: step-through state inspection CLI (state at Tn).

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
