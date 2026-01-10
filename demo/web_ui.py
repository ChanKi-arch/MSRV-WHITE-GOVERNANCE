#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Streamlit Web UI for MSR-V Public Demo."""

import json
import glob
import os
import streamlit as st
from engine import MSRVPublicEngine

st.set_page_config(page_title="MSR-V Public Demo", layout="wide")
st.title("MSR-V White Engine - Public Demo")

st.warning(
    "**This demo does NOT run the real MSR-V engine.** "
    "It replays precomputed traces or applies conservative heuristics. "
    "The proprietary core is excluded to protect IP."
)

eng = MSRVPublicEngine()

col1, col2 = st.columns([2, 1])

with col1:
    lang = st.selectbox("Language", ["EN", "KO"], index=0)
    text = st.text_area("Input", height=140, placeholder="Paste a sentence...")
    run = st.button("Inspect")

with col2:
    st.subheader("Output Fields")
    st.markdown(
        """
- **Route**: BYPASS / LITE / FULL
- **State4**: Harmony / Divergence / Alignment / Fracture
- **Zs**: Structural stability index
- **Theta**: Internal tension index
- **Shape**: Structural shape indicator
"""
    )

if run:
    if not text.strip():
        st.warning("Please enter input text first.")
    else:
        out = eng.inspect(text, lang=lang)
        st.subheader("Result")
        st.json(out)

st.divider()
st.subheader("Bundled Reports")

# Look for reports in current directory
report_patterns = ["REPORT_*.md", "BENCHMARK_*.md", "*.md"]
reports = []
for pattern in report_patterns:
    reports.extend(glob.glob(pattern))

# Filter out README
reports = [r for r in reports if "README" not in r]
reports = sorted(set(reports))

if reports:
    choice = st.selectbox("Select Report", [os.path.basename(r) for r in reports], index=0)
    for r in reports:
        if os.path.basename(r) == choice:
            with open(r, "r", encoding="utf-8") as f:
                st.markdown(f.read())
            break
else:
    st.info("No report files found in current directory.")
