# Hyperframes Composition Brief: AI-Portfolio — "The Map" (whiteboard lecture)

## Objective

Create a long-form whiteboard explainer lecture (series opener) touring the
AI-Portfolio's 8 systems with the restaurant-kitchen analogy, on-screen
keyword definitions, measured numbers, and the recommended study order.
This is a TUTOR_BRIEF override of /brag's 15–25s format: **~380–400 seconds,
narration ON** (`--voice`), calm tutor pacing.

## Output

- Composition directory: `D:/aria/Projects/brag-output/composition/`
- Rendered video: `D:/aria/Projects/brag-output/brag.mp4`
- Format: landscape — 1920x1080, `data-fps="24"`
- Duration: sum of scene durations (voice-driven), target 380–400s

## Source Material

- Project root: `D:/aria/Projects` (README.md, TUTOR_BRIEF.md, GLOSSARY.md)
- Product name: AI-Portfolio (Akshay John Xavier)
- Tagline / strongest claim: "every number is measured, not claimed"
- Key visual moments: the restaurant map (8 stations), per-station sketches,
  measured-number readout strips, refusal card, RELEASE BLOCKED stamp
- Copy that must appear verbatim:
  - "2,926 requests · 0 errors · 484 rps · p95 60ms" (AegisGate)
  - "precision 1.0 · recall 1.0 · blame top-1 100%" (ForensiQ)
  - "hallucination rate 0.0" (SwarmResearch)
  - "122 → 59 kept" (Model-Distillery)
  - "ASR 92% → 0%" (RedForge), "RELEASE BLOCKED · exit 1" (VerdictAI)
  - "recall@5 1.0 · safety violations 0" (HVAC-Copilot)
  - "65 audited changes" (BrandMorph), "44 spans · 6,578 tokens · exit 0 → exit 1" (PlatformDemo)
  - Study order: 1 Map · 2 AegisGate · 3 HVAC-Copilot · 4 VerdictAI · 5 ForensiQ · 6 RedForge · 7 SwarmResearch · 8 Model-Distillery · 9 BrandMorph · 10 PlatformDemo

## Creative Direction

- Tone preset: `polished`, overridden by the freeform tutor direction in
  `brag-plan.md` (whiteboard lecture, no hype, long holds, readable text)
- Angle: see brag-plan.md "The angle" (restaurant map + "you are here" motif)
- Hook: "A weekend:" struck through → "a different job."
- Outro: "That's the map." → next-episode card (AegisGate, bring coffee)
- Avoid: hype adjectives, launch energy, generic SaaS language, abstract
  filler, waveforms/equalizers, busy motion under narration

## Visual Identity

- Background: paper `#F6F2E8`; faint warm grid lines `#E7DFCB`; subtle grain
- Ink: `#26241D`; secondary ink `#6B6353`
- Blue marker accent: `#1D4ED8`; red marker: `#B42318`; green: `#166534`;
  amber highlight: `#B45309`; definition-chip paper: `#FFF8E6` (border `#E3D5A8`)
- Display font: Kalam 700 (local `assets/fonts/kalam-700.woff2`; Kalam 400 also shipped)
- Body font: Public Sans (local variable `assets/fonts/publicsans-var.woff2`,
  declared `font-weight: 100 900`)
- Hand-drawn feel: slight rotations (-1.5°..1.5°) on chips/cards, dashed or
  2–3px irregular-feeling borders, marker underlines that draw via scaleX
- Persistent motif: a small "you are here" kitchen mini-map in station scenes
  (8 dots; current station filled red) — bottom-left or top-right corner

## Storyboard

Contract: `brag-plan.md` (14 scenes, S1–S14). Scene timings are NOT fixed in
the plan: per-scene narration WAVs are generated first, measured with ffprobe,
and each scene's `data-duration` = wav + 0.7s tail (last scene +2.5s). Scene
`data-start` values are the running sum. The JS timeline uses the same table
(a `SCENES` array of {start, dur}) — keep HTML and JS consistent.

Per-scene content, keyword chips, readouts and SFX moments are specified in
`brag-plan.md` § Storyboard — follow it as the creative contract. Keyword
definition chips (one plain sentence each, from GLOSSARY.md) must appear at
the moment the narration first speaks the term: stagger them evenly across
the VO duration of the scene in narration order (e.g. chip i at
sceneStart + 0.15*dur + i*0.6*dur/(n-1) — adjust per scene so chip i lands
while its term is spoken; hold all chips until scene end).

## Audio

- Audio role: warm quiet bed + voice protagonist
- Audio arc: music fades in 0→3s, sits at whisper level throughout, fades out
  over the last 4s
- Music: `assets/music/happy-beats-business-moves-vol-12-by-ende-dot-app.mp3`
  (1:58). Loop it: place 3–4 segments on separate track indices (10,11,12,13)
  back to back (slight 0.5s overlap ok across different tracks), each with a
  `data-automation` volume lane (points in absolute values ~0.10–0.12; first
  segment ramps 0→0.12 over 3s; last segment ramps 0.12→0 over 4s at its end)
- Voiceover: 14 WAVs at `assets/voiceover/s01.wav` … `s14.wav` (Kokoro
  af_heart, already generated). One `<audio id="vo-s01">` per scene,
  `data-start` = scene start, `data-track-index` 20+i, `data-volume="1"`.
  Narration file paths also under `assets/voiceover/script/*.txt`.
- Music cue guidance: bundled preset exists for vol-12, but beat sync is
  deliberately not used in a narration-led lecture (readability primary;
  natural timing chosen throughout — documented in brag-plan.md)
- Audio-reactive treatment: none (deliberate, documented in brag-plan.md)
- Audio-coupled moments:
  - S1 — strike-through draws; 4 risk chips pin (soft drop on each)
  - S2 — pipeline boxes draw in sequence
  - S3 — 8 stations sketch in; single bell (impactBell_heavy_000 @ 0.4) when map completes
  - S4 — readout strip prints in (soft chip hit); 6 chips pin (drop on first only)
  - S5 — kappa gauge settles; stamp "RELEASE BLOCKED" (impactSoft_medium @ 0.5)
  - S6 — span tree draws; red circle around guilty span; readout prints
  - S7 — DAG draws; readout prints
  - S8 — funnel stages light; readout prints
  - S9 — ASR counter 92→0 (soft ticks); chips pin
  - S10 — refusal card slides up (soft drop); readout prints
  - S11 — before/after flip; readout prints
  - S12 — metric cards flip in pair by pair
  - S13 — flow diagram draws; study list items write in (quiet tick each)
  - S14 — title card; soft bell (impactBell_heavy_004 @ 0.35); music fades
- SFX selection guidance: sparse and quiet (0.3–0.5 volume); interface/drop_001
  for chip pin, casino/chip-lay for readout prints, impact/impactSoft_medium_001
  for the stamp, impact bells only at map reveal and outro
- SFX analysis guidance: `<skill-dir>/assets/sfx/sfx-analysis.md`; prefer low
  HF-risk files for repeated moments
- Exact SFX choice: Hyperframes chooses filenames/timestamps/density to match
  the implemented animation; copy chosen SFX into `composition/assets/sfx/`
- Audio files: music already copied to `composition/assets/music/`; voice WAVs
  are generated into `composition/assets/voiceover/`

## Hyperframes Instructions

Load and follow the Hyperframes domain skills (`hyperframes-core`,
`hyperframes-animation`, `hyperframes-creative`, `hyperframes-keyframes`,
`hyperframes-cli`). /brag is its own workflow — do not enter the hyperframes
entry-point interview or its generic promo workflow.

Requirements:
- Standalone composition: one `index.html`, root `data-composition-id="main"`,
  `data-width="1920"`, `data-height="1080"`, `data-fps="24"`, explicit
  `data-duration` = total (voice-driven), one paused GSAP timeline registered
  as `window.__timelines["main"]`, built synchronously from the SCENES table
- 14 scene clips: `<section class="clip" data-start data-duration>` direct
  children of root (automatic layout applies); never tween the clip itself —
  animate children; no scene-exit visibility sets (the runtime owns clip
  windows)
- All fonts via local `@font-face` (shipped woff2 files) — no Google Fonts
  links, no network at render time
- Every keyword defined on screen at first use (chips with one-sentence
  definitions from GLOSSARY.md); hold chips to scene end
- Reading-time floors: definition chips ~1.2s+ settled; readout numbers held
  2s+; body text 0.3s/word
- WCAG contrast: ink on paper is safe; colored text uses the dark variants
  above; run and fix `hyperframes check` (single gate)
- Music loop segments + 14 voice clips + sparse SFX on separate track indices
  with `id`s on every `<audio>`; use `data-automation` volume lanes for music
  fades (never combine a lane with a volume tween)
- Poster: after render, pick the settled restaurant-map frame (scene 3, ~
  scene3Start + 80% of its VO) as `brag.jpg` and bake it as frame 0
- Render: `npx hyperframes render --quality looks --output ../brag.mp4`
  (24 fps keeps the ~400s render tractable; whiteboard motion is fine at 24)
