# MSR-V White Engine — Public Demo

> **87% cost reduction. 0.29ms overhead. 100% traceable routing.**  
> Deterministic structural governance for LLM systems.

---

## ⚠️ Important Notice

**This demo does NOT run the real MSR-V engine.**

It replays precomputed governance traces from `public_samples.json` or applies conservative heuristics for unknown inputs. The proprietary MSR-V 2.5.x core is intentionally excluded to protect IP.

---

## What MSR-V Does

MSR-V is a **white-box governance layer** that decides:
- **When** to execute reasoning
- **How deeply** to process (BYPASS / LITE / FULL)
- **Whether** input is structurally safe

It is **NOT** a fact-checker. It does **NOT** detect hallucinations.  
It governs **structural integrity**, not factual truth.

---

## Key Metrics (Production Engine)

| Metric | Value |
|--------|-------|
| Cost Reduction | **87.4%** |
| Governance Latency | **0.29 ms** |
| Routing | Deterministic |
| Traceability | Full (State-4, Zs, θ, Shape) |

> Measured on MSR-V v2.5.3 with 4,200 test samples.

---

## What This Demo Shows

### ✅ Demonstrates
- Deterministic **Route** selection (`BYPASS` / `LITE` / `FULL`)
- Interpretable **State-4** classification (Harmony / Alignment / Divergence / Fracture)
- Transparent **JSON trace outputs**
- Benchmark summary reports

### ❌ Does NOT Include
- Proprietary MSR-V 2.5.x core logic
- Factual correctness validation
- Hallucination detection

---

## Quick Start

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

### Streamlit Web UI

```bash
streamlit run web_ui.py
```

---

## How Routing Works

| Input Type | Route | What Happens |
|------------|-------|--------------|
| High-confidence, low-risk | `BYPASS` | Inference skipped |
| Medium-risk | `LITE` | Shallow reasoning |
| Structurally unstable | `FULL` | Full inference |

**Result**: 87% of inputs never reach expensive deep reasoning.

---

## What MSR-V Detects (and Does NOT Detect)

### ✅ DETECTS
- Structural incompleteness (missing slots)
- Formal logical impossibilities
- Parser failures / malformed inputs
- Excessive structural complexity

### ❌ DOES NOT DETECT
- Factual errors ("Earth is flat")
- Semantic contradictions
- Exaggerated claims ("100% guaranteed")

**MSR-V is a structural governance layer, not a fact-checker.**

---

## Benchmark Summary (4,200 Samples)

| Domain | Samples | BYPASS | LITE | FULL | Latency | Cost Reduction |
|--------|--------:|-------:|-----:|-----:|--------:|---------------:|
| KO-Normal | 1,000 | 62.5% | 37.5% | 0.0% | 0.22ms | 93.1% |
| KO-Negation | 1,000 | 68.5% | 31.5% | 0.0% | 0.19ms | 93.4% |
| EN-Normal | 1,000 | 0.0% | 92.3% | 7.7% | 0.38ms | 83.1% |
| EN-Negation | 1,000 | 0.0% | 88.7% | 11.3% | 0.33ms | 79.8% |
| KO-Hard | 100 | 58.0% | 41.0% | 1.0% | 0.54ms | 92.0% |
| EN-Hard | 100 | 0.0% | 92.0% | 8.0% | 0.67ms | 82.8% |
| **Total** | **4,200** | **32.6%** | **62.7%** | **4.7%** | **0.29ms** | **87.4%** |

---

## Use Cases

- **Cost Optimization** — Reduce LLM API spend by 87%
- **Regulated Environments** — EU AI Act compliant audit trails
- **Edge Deployment** — Sub-millisecond governance for on-device AI
- **Safety Layers** — Catch unstable inputs before propagation

---

## License

- **License**: Apache-2.0 (demo wrapper only)
- **Proprietary MSR-V core**: Explicitly excluded
- **Purpose**: Research and architectural inspection

---

<p align="center">
  <strong>MSR-V</strong> — Control reasoning depth, not tokens.
</p>
