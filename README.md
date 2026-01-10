# MSR-V White Governance Engine — Public Demo (IP-Safe)

![Version](https://img.shields.io/badge/version-2.5.3--final-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)
![Status](https://img.shields.io/badge/status-public--demo-orange)
![Governance](https://img.shields.io/badge/focus-reasoning--governance-brightgreen)

**Deterministic Governance for Reasoning Depth, Cost, and Structural Risk**

> **“Control reasoning depth — not tokens.”**

This repository provides an **IP-safe public demo** of **MSR-V**,  
a **white-box reasoning governance engine** that determines **when**, **how**, and **how deeply**
reasoning should be executed in LLM-based systems.

MSR-V is **not a language model** and **not a fact-checker**.  
It is a **deterministic control layer** that governs reasoning **before inference occurs**.

---

## 🧠 What MSR-V Is

MSR-V is a **reasoning governance architecture** that:

- Diagnoses **structural stability** of reasoning
- Classifies reasoning into **interpretable structural states**
- Routes execution deterministically to:
  **BYPASS / LITE / FULL**
- Reduces **unnecessary computation, latency, and cost**
- Provides **white-box traceability** for every decision

MSR-V operates **above** LLMs and is **model-agnostic by design**.

---

## ❌ What MSR-V Is Not

- ❌ A language model  
- ❌ A fact-checking or truth-validation system  
- ❌ A black-box classifier  
- ❌ A replacement for LLMs  

> MSR-V does **not** decide whether an answer is true.  
> It decides whether **reasoning should occur at all**.

---

## 🧩 Core Governance Concepts (Demo Scope)

### Structural Axes (DROS)
Reasoning is decomposed into explicit, independent axes:

- **D** — Definition integrity  
- **R** — Relation consistency  
- **O** — Operation validity (incl. negation)  
- **S** — System / domain context  

### Structural States (State-4)
Each input is diagnosed as one of:

- **Harmony** — structurally coherent  
- **Alignment** — coherent on critical axes  
- **Divergence** — exploratory or unstable  
- **Fracture** — structurally broken (even if fluent)

> **Fracture ≠ factual error**  
> Fracture = internal structural inconsistency

### Deterministic Routing
Based on structural diagnosis:

| Route | Meaning |
|------|--------|
| **BYPASS** | Structurally trivial — skip deep reasoning |
| **LITE** | Low to medium risk — shallow reasoning |
| **FULL** | Structurally complex or unstable — deep reasoning |

Routing is driven by **structural necessity**, not confidence scores.

---

## 📊 Demo Benchmark Overview (Governance Behavior)

> **Important**  
> Metrics in this demo describe **governance behavior**,  
> not model accuracy or factual correctness.

| Domain | Samples | BYPASS | LITE | FULL | Avg Latency | Safety | Cost Reduction |
|-------|--------:|-------:|-----:|-----:|------------:|-------:|---------------:|
| Korean – Normal | 1,000 | 62.5% | 37.5% | 0.0% | 0.22 ms | 100% | 93.12% |
| Korean – Negation | 1,000 | 68.5% | 31.5% | 0.0% | 0.19 ms | 100% | 93.42% |
| English – Normal | 1,000 | 0.0% | 92.3% | 7.7% | 0.38 ms | 100% | 83.07% |
| English – Negation | 1,000 | 0.0% | 88.7% | 11.3% | 0.33 ms | 100% | 79.83% |
| Korean – Hard | 100 | 58.0% | 41.0% | 1.0% | 0.54 ms | 100% | 92.00% |
| English – Hard | 100 | 0.0% | 92.0% | 8.0% | 0.67 ms | 100% | 82.80% |
| **Weighted Avg** | **4,200** | **32.6%** | **62.7%** | **4.7%** | **0.29 ms** | **100%** | **87.40%** |

- **Safety = 100%** → no structurally fractured cases routed to BYPASS
- **Cost reduction** reflects avoided unnecessary reasoning execution
- Results demonstrate **deterministic governance behavior**

---

## 🚀 Quickstart

### 1) CLI Demo
```bash
python demo/demo_cli.py --lang EN --text "Quantum robots cure cancer 100%."
python demo/demo_cli.py --lang KO --interactive

2) Web UI (Streamlit)

pip install -r requirements.txt
streamlit run demo/app_streamlit.py

The demo displays:

Structural state (State-4)

Routing decision

Zs / θ indicators

Governance rationale



---

📁 Repository Structure

msrv-public-demo/
├── demo/        # CLI + Web UI (IP-safe wrappers)
├── data/        # Sanitized sample JSON traces
├── reports/     # Aggregated benchmark summaries (markdown)
├── docs/        # Architecture & governance notes
└── requirements.txt


---

🔒 Intellectual Property Notice

This repository does not include:

Proprietary MSR-V 2.5.x core logic

Private datasets or raw production logs

Any production inference components


The demo is intentionally limited to:

deterministic routing behavior

interpretable governance outputs

simulation-based benchmark evidence



---

⚠️ Disclaimer

This is a research-grade public demo intended for:

architectural inspection

governance behavior validation

discussion of deterministic reasoning control


It does not make performance, accuracy, or factual correctness claims.


---

👤 Author

ChanKi.arch
Lead Architect, Chan Ki Labs
📧 ChanKi.arch@proton.me
