# MSR-V Public Demo — Benchmark Summary (Structural Governance)

**Engine**: MSR-V White Engine v2.5.3 (Demo Scope)  
**Report Scope**: Routing behavior, latency, structural completeness, and relative cost  
**Important**: This report does **NOT** claim factual correctness.

---

## Executive Summary (4,200 Samples)

MSR-V is a **structural governance layer**, not a fact-checker.

- ✅ Measures **structural completeness** of inputs (parsing / slot extraction / stability signals)
- ✅ Routes execution depth deterministically (**BYPASS / LITE / FULL**)
- ✅ Provides white-box trace signals (**Zs, θ, Shape, State-4**)
- ❌ Does not judge factual truth
- ❌ Does not guarantee semantic correctness

---

## Domain Coverage Summary

| Domain | Samples | BYPASS | LITE | FULL | Avg Latency | Safety* | Cost Reduction |
|-------|--------:|-------:|-----:|-----:|------------:|--------:|---------------:|
| Korean — Normal (KO-NORM) | 1,000 | 62.5% | 37.5% | 0.0% | 0.22 ms | 100.0% | 93.12% |
| Korean — Negation (KO-NEG) | 1,000 | 68.5% | 31.5% | 0.0% | 0.19 ms | 100.0% | 93.42% |
| English — Normal (EN-NORM) | 1,000 | 0.0% | 92.3% | 7.7% | 0.38 ms | 100.0% | 83.07% |
| English — Negation (EN-NEG) | 1,000 | 0.0% | 88.7% | 11.3% | 0.33 ms | 100.0% | 79.83% |
| Korean — Hard Examples (KO-HARD) | 100 | 58.0% | 41.0% | 1.0% | 0.54 ms | 100.0% | 92.00% |
| English — Hard Examples (EN-HARD) | 100 | 0.0% | 92.0% | 8.0% | 0.67 ms | 100.0% | 82.80% |
| **Weighted Average (Total)** | **4,200** | **32.6%** | **62.7%** | **4.7%** | **0.29 ms** | **100.0%** | **87.40%** |

\* **Safety (Demo Definition)**: No structurally risk-tagged cases were routed to BYPASS under the evaluated demo settings.  
This is a governance safety property, not factual correctness.

---

## Interpretation Notes

- Korean shows higher **BYPASS** due to agglutinative structure and lower ambiguity in shallow cases.
- English shows higher **LITE/FULL** due to inflectional ambiguity and deeper structural checks.
- Cost reduction reflects **avoided deep reasoning execution**, not model quality improvement.

---

## What "Fracture" Means Here

**Fracture = structural defect** (e.g., parsing failure, missing essential slots, or unstable structural signals).  
Fracture does **NOT** mean "factually false".

Recommended pipeline:
`Input → MSR-V (structural governance) → LLM / KG (optional semantic verification) → Output`
