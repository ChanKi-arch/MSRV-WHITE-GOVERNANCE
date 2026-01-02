# MSR-V Architecture Overview

MSR-V (Merge-Split-Re-merge Visibility) is a **white-box structural governance layer** for LLM systems.

It evaluates the **structural integrity** of reasoning inputs/outputs and deterministically controls execution depth.

> MSR-V is NOT a fact-checker and does NOT judge factual truth.

---

## 1. Structural Governance Objective

LLM failures are often invisible to confidence scores because fluent text can still contain:
- Unstable definitions
- Invalid relations
- Impossible operations
- System/domain mismatches

MSR-V makes these structural risks observable and governable via explicit signals and routing.

---

## 2. Core Loop Concept (Merge-Split-Re-merge)

The internal engine design follows a deterministic governance loop:

- **Merge**: Compress structural primitives (D/R/O/S)
- **Split**: Explore alternative structural tensions
- **Re-merge**: Select stable configuration and determine execution necessity

This public repo demonstrates the **interfaces and behaviors**, not proprietary internals.

---

## 3. 3-Tier Deterministic Routing

MSR-V routes execution into:

| Route | Description |
|-------|-------------|
| **BYPASS** | Trivial structure, no deep reasoning required |
| **LITE** | Shallow verification and risk gating |
| **FULL** | Deep inspection for high-risk or structurally fractured cases |

Routing is based on **structural necessity**, not probability.

---

## 4. White-Box Traceability

MSR-V exposes governance decisions using interpretable signals:

- Structural axes (D/R/O/S)
- State-4 classification
- Stability indices (Zs, θ)
- Routing decision factors

This enables audits, safe deployment, and system-level optimization.

---

## 5. Parser-Agnostic Design

MSR-V's core is the **Structural Physics Engine**, not the parser.

```
[Any Parser] -> JSON12 Slots -> DROS/FMEP -> V-Axis Energy
                                                |
                                    Physics Layer (theta, m, v)
                                                |
                                    Shape + State4 + Zs
                                                |
                                    Deterministic Routing
```

The built-in rule-based parser is a reference implementation.  
Production deployments can substitute LLM-based parsers or domain-specific NLU.
