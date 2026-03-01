"""
MarginIQ v5 — Enterprise AI Pricing Committee
Streamlit Deployment · Production Ready

Deploy on Streamlit Cloud:
  1. Push this folder to GitHub
  2. Go to share.streamlit.io → New App → select repo
  3. Main file: app.py
  4. Click Deploy

Local run:
  pip install streamlit
  streamlit run app.py
"""

import streamlit as st
import streamlit.components.v1 as components
import os

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MarginIQ v5 · Enterprise AI Pricing Committee",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Hide all Streamlit chrome so the HTML takes full screen ───────────────────
st.markdown("""
<style>
    /* Hide Streamlit menu, header, footer, deploy button */
    #MainMenu          { visibility: hidden !important; }
    header             { visibility: hidden !important; }
    footer             { visibility: hidden !important; }
    [data-testid="stDeployButton"]        { display: none !important; }
    [data-testid="stDecoration"]          { display: none !important; }
    [data-testid="stStatusWidget"]        { display: none !important; }
    [data-testid="collapsedControl"]      { display: none !important; }

    /* Remove all padding so the app fills 100% of screen */
    .stApp                { background: #05080E !important; }
    .block-container      { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stAppViewContainer"] { padding: 0 !important; }
    [data-testid="stVerticalBlock"]    { gap: 0 !important; padding: 0 !important; }

    /* Remove iframe border */
    iframe { border: none !important; display: block !important; }
</style>
""", unsafe_allow_html=True)

# ── Load the MarginIQ HTML ─────────────────────────────────────────────────────
html_path = os.path.join(os.path.dirname(__file__), "marginiq.html")

if not os.path.exists(html_path):
    st.error("⚠️ marginiq.html not found. Make sure it is in the same folder as app.py")
    st.stop()

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# ── Render full-screen with scroll enabled ────────────────────────────────────
# height=900 gives comfortable fit on 1080p screens.
# Increase to 1000 for 4K / large monitors.
components.html(
    html_content,
    height=900,
    scrolling=False   # Internal scrolling is handled by the app itself
)
