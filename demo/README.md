# MSR-V White Engine — Public Demo

> **87% cost reduction. 0.29ms overhead. 100% safety gating.**  
> This is what deterministic reasoning governance looks like.

---

This repository contains an **IP-safe public demo** of MSR-V governance outputs.

MSR-V is not a language model. It's a **white-box governance engine** that decides *when*, *how deeply*, and *whether* reasoning should execute — before costly inference occurs.

---

## Key Results (Demo Scope)

| Metric | Value |
|--------|-------|
| Cost Reduction | **87.4%** |
| Governance Latency | **0.29 ms** |
| Routing | Deterministic |
| Transparency | Full trace (State-4, Zs, θ, Shape) |

> Metrics reflect governance behavior — not model accuracy or factual correctness.

---

## What This Demo Shows

### ✅ Demonstrates

- Deterministic **Route** selection (`BYPASS` / `LITE` / `FULL`)
- Interpretable **State-4** classification  
  (Harmony / Alignment / Divergence / Fracture)
- Transparent **trace-style JSON outputs**
- Benchmark summary reports (Markdown)

### 🚫 Does NOT Include

- Proprietary MSR-V 2.5.x core logic
- Private datasets or raw production logs
- Factual correctness or truth validation

---

## 🚀 Quick Start

### Requirements

```bash
Python >= 3.8
pip install -r requirements.txt
```

### CLI Demo

```bash
python demo_cli.py --lang EN --text "Quantum robots cure cancer 100%."
python demo_cli.py --lang KO --text "추천 시스템이 효과가 없다"
python demo_cli.py --interactive --lang EN
```

**Output includes:**
- Structural state (State-4)
- Routing decision (`BYPASS` / `LITE` / `FULL`)
- Zs / θ indicators
- Governance rationale

### Streamlit Web UI

```bash
pip install -r requirements.txt
streamlit run web_ui.py
```

**Visualizes:**
- Input text → Structural state → Routing path → Execution depth

---

## How Routing Works

| Input Type | Route | What Happens |
|------------|-------|--------------|
| High-confidence, low-risk | `BYPASS` | Inference skipped |
| Medium-risk | `LITE` | Shallow reasoning |
| Structurally unstable | `FULL` | Full inference |

**Result**: Most inputs never reach expensive deep reasoning.

---

## Methodology Notes

- Demo returns exact/fuzzy matches from bundled trace samples when available
- If no match: conservative fallback heuristic applies
- Fallback biases toward `FULL` routing for structurally risky claims
- This demonstrates **governance safety**, not factual accuracy

**For real evaluation:**
- Run proprietary MSR-V engine privately
- Publish only outputs and traces, never core logic

---

## Use Cases

- **Cost Optimization** — Reduce GPU/NPU spend by skipping unnecessary inference
- **Regulated Environments** — EU AI Act compliant audit trails
- **Edge Deployment** — Sub-millisecond governance for on-device AI
- **Safety Layers** — Catch unstable inputs before they propagate

---

## 🔒 License & Scope

- **License**: Apache-2.0 (demo wrapper only)
- **Proprietary MSR-V core logic**: Explicitly excluded
- **Purpose**: Research and architectural inspection

---

<p align="center">
  <strong>MSR-V</strong> — Control reasoning depth, not tokens.<br>
  <a href="https://github.com/ChanKi-arch/msrv-public-demo/releases">Releases</a> •
  <a href="../../issues">Issues</a>
</p>
