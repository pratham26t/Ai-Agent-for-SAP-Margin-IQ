import streamlit as st
import streamlit.components.v1 as components
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MarginIQ · Enterprise AI Pricing Committee",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Hide Streamlit chrome so the app fills the whole viewport ─────────────────
st.markdown(
    """
    <style>
        /* Hide Streamlit header, footer, and sidebar toggle */
        #MainMenu  { visibility: hidden; }
        footer     { visibility: hidden; }
        header     { visibility: hidden; }

        /* Remove all default padding so our app fills 100% */
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        [data-testid="stAppViewContainer"] {
            padding: 0 !important;
        }
        [data-testid="stVerticalBlock"] {
            gap: 0 !important;
            padding: 0 !important;
        }
        iframe {
            display: block;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Load the HTML file ────────────────────────────────────────────────────────
html_path = os.path.join(os.path.dirname(__file__), "marginiq.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# ── Render it full-screen ─────────────────────────────────────────────────────
# height is set very large so the iframe never clips; scrolling is handled
# inside the HTML itself (overflow:hidden on body, internal scroll on #main).
components.html(
    html_content,
    height=900,
    scrolling=False,
)
