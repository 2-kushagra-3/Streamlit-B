# ─────────────────────────────────────────────────────────────────────────────
# app.py  —  entry point:  streamlit run app.py
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st

from config import MOODS
from styles import inject_global_styles
from components.home       import render_home
from components.mood_page  import render_mood_page, render_nav
from components.handpicked import render_handpicked_page

st.set_page_config(
    page_title="🎂 Happy Birthday!",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_styles()

# ── Session state ─────────────────────────────────────────────────────────────
st.session_state.setdefault("selected_mood",    None)
st.session_state.setdefault("pending_mood",     None)   # destination after clear
st.session_state.setdefault("came_from_hp",     False)

for m in MOODS:
    st.session_state.setdefault(f"movie_page_{m['key']}", 1)
    st.session_state.setdefault(f"song_page_{m['key']}",  1)

# ── Router ────────────────────────────────────────────────────────────────────
page = st.session_state.selected_mood

# If we were on handpicked and are now on the clearing frame → jump to destination
if st.session_state.came_from_hp and page == "__clearing__":
    dest = st.session_state.pending_mood
    st.session_state.selected_mood = dest
    st.session_state.pending_mood  = None
    st.session_state.came_from_hp  = False
    st.rerun()

if page is None or page == "__clearing__":
    render_home()
elif page == "handpicked":
    render_nav("handpicked")
    render_handpicked_page()
else:
    render_mood_page(page)