
import io
from pathlib import Path

import streamlit as st

try:
    from streamlit_pdf_viewer import pdf_viewer
    HAS_VIEWER = True
except Exception:
    HAS_VIEWER = False

st.set_page_config(page_title="LLM Auditing Flipbook", page_icon="📘", layout="wide")

col_logo, col_title = st.columns([1,5], gap="small")
with col_logo:
    st.image("assets/dekra_logo.png", width=120, caption="Training Provider")
with col_title:
    st.markdown("### Using Large Language Models in Auditing with a Risk Perspective")
    st.caption("Digital Flipbook • Powered by Streamlit")

with st.sidebar:
    st.header("📄 Upload Your Book")
    uploaded = st.file_uploader("Upload a PDF export of your Word document", type=["pdf"])
    st.info("Tip: Export your .docx to PDF first for best fidelity. In Word: File → Save As → PDF", icon="💡")
    st.markdown("---")
    theme = st.radio("Theme", ["Dark", "Light"], horizontal=True)
    page_width = st.slider("Viewer width (px)", 600, 1300, 1000)
    page_height = st.slider("Viewer height (px)", 400, 1200, 800)

if uploaded is None:
    st.warning("Upload a PDF in the sidebar to view your flipbook.", icon="⬆️")
    cov = Path("assets/cover.png")
    if cov.exists():
        st.image(str(cov), caption="Sample cover (preview)", use_column_width=True)
    st.stop()

pdf_bytes = uploaded.read()

if HAS_VIEWER:
    bg_color = "#0f172a" if theme == "Dark" else "#ffffff"
    st.markdown(f"""
        <style>div.block-container {{ padding-top: 1rem; }}</style>
    """, unsafe_allow_html=True)
    pdf_viewer(pdf_bytes, width=page_width, height=page_height, key="flipbook", render_text=True)
else:
    st.error("streamlit-pdf-viewer not installed. Falling back to a basic download.", icon="ℹ️")
    st.download_button("Download PDF", data=pdf_bytes, file_name=uploaded.name, mime="application/pdf")
