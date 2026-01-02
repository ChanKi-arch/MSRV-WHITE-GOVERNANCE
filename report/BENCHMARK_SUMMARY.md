# MSR-V Benchmark Summary

**Engine**: MSR-V White Engine v2.5.3  
**Samples**: 4,200 test cases  
**Scope**: Routing behavior, latency, structural governance

> **Important**: This report measures structural governance, NOT factual correctness.

---

## Executive Summary

MSR-V is a **structural governance layer**, not a fact-checker.

| Capability | Status |
|------------|--------|
| Measures structural completeness | ✅ |
| Routes execution depth deterministically | ✅ |
| Provides white-box trace signals | ✅ |
| Judges factual truth | ❌ |
| Detects hallucinations | ❌ |

---

## Benchmark Results (4,200 Samples)

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

## Key Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| **Cost Reduction** | 87.4% | Weighted average across all domains |
| **Governance Latency** | 0.29ms | Average per-input processing time |
| **BYPASS Rate** | 32.6% | Inputs skipping LLM entirely |
| **FULL Rate** | 4.7% | Inputs requiring deep inspection |

---

## Interpretation Notes

### Language Differences

- **Korean** shows higher BYPASS due to agglutinative structure and lower ambiguity
- **English** shows higher LITE/FULL due to inflectional ambiguity

### Cost Reduction Calculation

```
Cost Reduction = (BYPASS% × 1.0) + (LITE% × 0.7) + (FULL% × 0.0)
```

- BYPASS: 100% cost saved (no LLM call)
- LITE: 70% cost saved (shallow processing)
- FULL: 0% cost saved (full inference)

---

## What "Fracture" Means

**Fracture = structural defect**, such as:
- Parsing failure
- Missing essential slots
- Unstable structural signals

Fracture does **NOT** mean "factually false".

---

## Recommended Pipeline

```
Input -> MSR-V (structural governance) -> LLM / KG (optional semantic verification) -> Output
```

MSR-V acts as a **cost gate** before expensive inference.  
Factual verification is a separate downstream concern.
