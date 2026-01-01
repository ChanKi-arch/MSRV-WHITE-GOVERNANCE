import json
import glob
import os
import streamlit as st
from engine import MSRVPublicEngine

st.set_page_config(page_title="MSR-V Public Demo", layout="wide")
st.title("MSR-V White Engine — Public Demo (IP-Safe)")
st.caption(
    "This demo replays precomputed traces + conservative heuristics. "
    "The proprietary core is NOT shipped."
)

eng = MSRVPublicEngine()

col1, col2 = st.columns([2, 1])

with col1:
    lang = st.selectbox("Language", ["EN", "KO"], index=1)  # KO default
    text = st.text_area("Input", height=140, placeholder="Paste a sentence…")
    run = st.button("Inspect")

with col2:
    st.subheader("What you are seeing")
    st.markdown(
        """
- **Route**: BYPASS / LITE / FULL
- **State4**: Harmony / Divergence / Alignment / Fracture
- **Zs / θ**: stability & torsion (demo-scale)
- **Trace**: all fields are transparent and exportable
"""
    )

if run:
    if not text.strip():
        st.warning("Please paste input text first.")
    else:
        out = eng.inspect(text, lang=lang)
        st.subheader("Result")
        st.json(out)

st.divider()
st.write("Markdown reports bundled with this demo:")

# Look for reports in current directory or /docs
report_dirs = [".", "docs", "data"]
reports = []
for d in report_dirs:
    reports.extend(glob.glob(os.path.join(d, "REPORT_*.md")))
    reports.extend(glob.glob(os.path.join(d, "BENCHMARK_*.md")))

reports = sorted(set(reports))

if reports:
    choice = st.selectbox("Select Report", [os.path.basename(r) for r in reports], index=0)
    # Find actual path
    for r in reports:
        if os.path.basename(r) == choice:
            with open(r, "r", encoding="utf-8") as f:
                st.markdown(f"### {choice}")
                st.markdown(f.read())
            break
else:
    st.info("No REPORT_*.md or BENCHMARK_*.md files found.")
