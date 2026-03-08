# ─────────────────────────────────────────────────────────────────────────────
# components/mood_page.py
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
from config import MOODS, MOOD_MAP
from styles import inject_page_styles
from components.movies import render_movie_grid
from components.songs  import render_song_list


def _navigate_to(dest: str, currently_on: str):
    """
    Navigate to dest.
    If we are currently on the handpicked page, we must pass through a
    clearing frame first so Streamlit rebuilds the widget tree from scratch.
    Otherwise the tabs from handpicked bleed into the mood page.
    """
    if currently_on == "handpicked" and dest != "handpicked":
        st.session_state.pending_mood  = dest
        st.session_state.came_from_hp  = True
        st.session_state.selected_mood = "__clearing__"
    else:
        st.session_state.selected_mood = dest
    st.rerun()


def render_nav(active: str):
    """Sticky nav: Home | all moods | 💝 Handpicked"""
    cols = st.columns([1.0] + [1.1] * len(MOODS) + [1.3, 0.05])

    with cols[0]:
        if st.button("🎂 Home", key="nav_home", use_container_width=True):
            _navigate_to(None, active)

    for i, mood in enumerate(MOODS):
        with cols[i + 1]:
            is_active = mood["key"] == active
            if st.button(
                mood["label"],
                key=f"nav_{mood['key']}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ) and not is_active:
                _navigate_to(mood["key"], active)

    with cols[len(MOODS) + 1]:
        is_hp = active == "handpicked"
        if st.button(
            "💝 Handpicked",
            key="nav_handpicked",
            use_container_width=True,
            type="primary" if is_hp else "secondary",
        ) and not is_hp:
            _navigate_to("handpicked", active)


def render_mood_page(mood_key: str):
    mood = MOOD_MAP[mood_key]

    inject_page_styles(mood_key)
    render_nav(mood_key)

    st.markdown(f"""
    <div class="mood-header" style="background:{mood['bg']};color:{mood['text']};">
        <div style="font-size:2.6rem;">{mood['emoji']}</div>
        <div class="mood-title">{mood['label'].split(' ', 1)[1]}</div>
        <div class="mood-tagline">{mood['tagline']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    tab_movies, tab_songs = st.tabs(["🎬  Movies", "🎵  Songs"])

    with tab_movies:
        with st.spinner("Loading movies…"):
            render_movie_grid(mood)

    with tab_songs:
        with st.spinner("Loading songs…"):
            render_song_list(mood)

    st.markdown("""
    <div class="app-footer">
        Made with ❤️ &nbsp;
    </div>
    """, unsafe_allow_html=True)