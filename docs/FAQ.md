# FAQ

### Q: Is the proprietary MSR-V core engine included in this repository?

**A:** No. This repository provides an **IP-safe public demo** for validating governance behavior.  
The proprietary core engine is intentionally excluded to protect intellectual property.

---

### Q: Is MSR-V a language model?

**A:** No. MSR-V does not generate text. It is a **deterministic governance layer** that controls reasoning execution depth.

---

### Q: Is MSR-V a fact-checker?

**A:** No. MSR-V does not judge factual truth.  
It detects **structural defects** and governs routing decisions.

---

### Q: Can MSR-V detect hallucinations?

**A:** No. MSR-V cannot detect factual hallucinations.  
If a sentence is structurally complete (e.g., "The Earth is flat"), MSR-V will pass it.  
MSR-V governs **structural integrity**, not factual correctness.

---

### Q: What does "Fracture" mean?

**A:** Fracture indicates a **structural defect**:
- Parsing failure
- Missing essential slots
- Unstable structural signals

It does NOT mean "factually false".

---

### Q: Why does routing differ between Korean and English?

**A:** Korean (agglutinative) often enables safer shallow passes (higher BYPASS).  
English (inflectional) tends to require more structural verification (higher LITE/FULL).  
This reflects linguistic structure, not model bias.

---

### Q: What do Zs and Theta represent?

**A:** They are **internal governance signals**:
- **Zs**: Structural stability index (higher = more stable)
- **Theta (θ)**: Internal tension/torsion index (higher = more energy imbalance)

They are not probability-based confidence scores.

---

### Q: How is cost reduction calculated?

**A:** Cost reduction = weighted average of routing decisions.

- BYPASS = 100% cost saved (no LLM call)
- LITE = 70% cost saved (shallow processing)
- FULL = 0% cost saved (full inference)

Formula: `Cost Reduction = (BYPASS% × 1.0) + (LITE% × 0.7) + (FULL% × 0.0)`
