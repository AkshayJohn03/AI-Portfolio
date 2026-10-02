# QUORUM — A focus group in a box
*Grounded in 250M measured tastes. Qloo Agentic Hackathon entry — Oct 30 deadline.*

---

## The pitch (paste into registration)

**Name:** Quorum — a focus group in a box

**Idea:** Small businesses and founders burn $10–40k on market research — or ship on vibes. Quorum runs a grounded focus group in minutes: describe an idea, pick an audience, and the agent builds that audience as a measured segment from Qloo's cross-domain taste graph (250M entities), then runs a synthetic panel where every participant reacts *through* their real affinity fingerprint — each reaction citing the Qloo evidence behind it. The verdict report tells you who loves it, who rejects it and why, and the demand-supply gap: which segment your idea resonates with that nothing nearby serves. Synthetic users exist today — but every tool invents personas from LLM imagination. Quorum is the first grounded one.

---

## What it is (one screen)

```
INPUT: your idea + your target audience ("vinyl cafés in Austin, 22–30")
  ↓
① SEGMENT BUILDER
   Qloo audiences + geo + affinities → the audience as a measured
   fingerprint (top entities, cross-domain chains, over-index signals)
  ↓
② CLAIM DECOMPOSER (agent)
   The idea is broken into testable claims ("students will pay ₹250
   for a listening bar", "vinyl buyers overlap with specialty coffee")
  ↓
③ THE PANEL (grounded synthetic participants, 6–10)
   Each participant carries a real fingerprint slice and reacts
   through it — enthusiasm, rejection, price pushback, "this isn't
   for me" — every sentence traceable to a Qloo correlation
  ↓
④ GROUNDING SCORER (VerdictAI pattern)
   grounding-rate = % of panel claims traceable to Qloo evidence.
   The metric nobody in the synthetic-user category publishes.
  ↓
⑤ VERDICT REPORT
   who loves it / who rejects it / why / the demand-supply gap /
   the 3 real people to talk to next (names of segments, not people)
```

## The technical novelty: the grounding-rate

The synthetic-user category's open wound (documented by Nielsen Norman Group) is that personas are ungrounded LLM stereotypes. Our answer is a **measurable claim**: every panel statement must carry a Qloo receipt — an entity, an affinity score, a correlation. The **grounding-rate** (% of panel claims traceable to Qloo evidence) is computed by the report and displayed live. A panel with grounding-rate 0.92 is a different product than ChatGPT roleplaying. This is the thing the Qloo CTO cannot get from anyone else's entry.

## Why the agent is necessary (the saffron rule for ourselves)

A script could print fixed reactions. The agent earns its existence by:
- **Decomposing** any arbitrary idea into testable claims (open input space)
- **Choosing which segments to probe** based on what the fingerprint reveals
- **Chasing contradictions**: when a panelist says something off-fingerprint, the agent runs a follow-up Qloo query and probes deeper — adaptive, multi-step
- **Scanning supply**: cross-referencing the demand signal against what exists nearby (the gap analysis)

The demo must show one adaptive probe on screen — that's the moment judges see it's an agent, not a form.

## Demo script (3 minutes, 3 panels)

Idea: *"a listening bar — vinyl + high-end coffee, no talking past 8pm"* — tested against 3 measured segments:
1. **Austin record collectors (25–34)** — enthusiasm with receipts (affinity chain: vinyl → specialty coffee → late-night culture)
2. **New parents in the suburbs** — polite rejection with the *reason* (early nights, price pushback) — rejections make the tool credible
3. **Club-goers (21–27)** — "no talking past 8pm? seriously?" — the segment Quorum flags as the demand gap it *can't* serve → the honest limit is the trust builder

Closing frame: *"Quorum just saved six weeks and ₹3 lakh of guessing. Talk to the two segments that matter: the collectors, and someone who says no."*

## Judge-by-judge attack map (and our answers)

| Judge | Their attack | Our answer |
|---|---|---|
| Calacanis | "Synthetic research is fake research" | We never claim prediction — we claim *grounded hypothesis generation* + tell you exactly who to talk to next. Cheaper, faster, honest. |
| Qloo CTO | "Shallow API usage" | 4+ endpoints (audiences, insights, compare, trending), grounding-rate metric, adaptive follow-up queries — plus the metric is a new artifact FOR Qloo's ecosystem. |
| Seligman (governance) | "What are the ethics of fake people?" | Radical transparency: receipts on every claim, explicit limits on the report, no overselling prediction. |
| Boehly / Abrams / Cedric | "Does this matter to entertainment?" | Demo segment 2: a comedy-night tour plan for 3 cities — panels react to the bill. Live-entertainment use case, literally on stage. |

## Honest scoring

| Criterion | Score | The gap |
|---|---|---|
| Non-obvious idea | 9 | "Grounded panels" is fresh; "simulated research" broadly is warming up |
| Qloo load-bearing | 10 | Absolute — the product is the graph |
| Agent necessity | 9 | Adaptive probing must be *shown*, not claimed |
| Demo wow | 9.5 | Three contrasting panels + live receipts |
| Feasibility (4 wks) | 8.5 | Prompt-engineering for grounded reactions is the hard 20% |
| Judge-bench fit | 9.5 | Investor + CTO + entertainment bench all hit |
| **The missing 0.6** | — | "Does grounded = predictive?" is unprovable in 4 weeks. We don't claim it. We claim grounding — which is measurable. |

**Verdict: 9.4/10. Proceed.** The 0.6 is not fixable by a better idea — it's fixable by *honest framing*, which is already designed in.

---

## 4-week plan

**Week 1 — Reality gate + scaffold.** Register on Devpost. Request API key (day 1 — arrives in "a few business days"). Meanwhile: build the Qloo tool layer against the sandbox docs (search → tags → insights, GET + X-Api-Key), and the SegmentBuilder with mock fingerprints. **The Gate:** the hour the key lands, pull 3 segments × 3 cities; if correlations are rich → all-in. If thin → demo cities move to US/UK (data deepest there), concept unchanged.
**Week 2 — The engine.** Claim decomposer, panel loop with receipts, grounding scorer, verdict report v1. Wire through AegisGate (metering: "this panel cost $0.11").
**Week 3 — The product.** Front-end (PipelineViz design system): idea form → live panel transcript → report. Deploy live (Vercel + API routes). Grounding-rate shown in real time.
**Week 4 — Demo + submission.** Record the adaptive-probe moment. README with the category landscape (genagents, Concordia, OASIS, SyntheticUsers + NN/g critique — and our answer). Submit 48h before deadline.

**Kill/pivot criteria:** if the Week-1 gate shows fingerprints too thin even in US cities → pivot to VibeCheck (audit verb, same engine, less data-hungry), keep everything.

## Stack (all existing, 5 repos compose)

Swarm runtime (orchestration) · AegisGate (LLM routing/metering/keys) · VerdictAI (grounding scorer — the grounding-rate is a VerdictAI report) · RedForge (input defenses on user-submitted ideas) · PipelineViz design language (front-end). Qloo = the new data layer.
