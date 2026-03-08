# ─────────────────────────────────────────────────────────────────────────────
# components/movies.py  —  movie grid renderer
# ─────────────────────────────────────────────────────────────────────────────
import random
import streamlit as st

from data import fetch_movies, parse_movie


def render_movie_grid(mood: dict):
    """Render 8 movie cards in a 4-column grid for the given mood."""
    key   = mood["key"]
    page  = st.session_state.get(f"movie_page_{key}", 1)
    extra = mood.get("movie_extra", {})

    movies = fetch_movies(
        genre_ids   = tuple(mood["movie_genres"]),
        sort_by     = mood["movie_sort"],
        extra_items = tuple(sorted(extra.items())),
        page        = page,
    )

    # Shuffle button — centred
    _, c_btn, _ = st.columns([2, 1, 2])
    with c_btn:
        if st.button("🔀 Shuffle Movies", key=f"shuf_mv_{key}", use_container_width=True):
            st.session_state[f"movie_page_{key}"] = random.randint(1, 8)
            st.cache_data.clear()
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    if not movies:
        st.error("Couldn't load movies — check your TMDB API key in config.py")
        return

    cols = st.columns(4)
    for idx, raw in enumerate(movies):
        mv = parse_movie(raw)
        with cols[idx % 4]:
            img_html = (
                f'<img src="{mv["poster"]}" alt="{mv["title"]}" loading="lazy"/>'
                if mv["poster"]
                else '<div style="font-size:3rem;text-align:center;padding:32px 0;">🎬</div>'
            )
            st.markdown(f"""
            <div class="movie-card"
                 style="background:{mood['card_bg']};box-shadow:0 8px 26px rgba(0,0,0,.18);">
                {img_html}
                <div class="mc-info" style="color:{mood['text']};">
                    <div class="badge"
                         style="background:{mood['accent']};color:white;">★ {mv['rating']:.1f}</div>
                    <div class="mc-title">{mv['title']}</div>
                    <div class="mc-meta">{mv['year']}</div>
                    <div class="mc-overview">{mv['overview']}</div>
                </div>
            </div>""", unsafe_allow_html=True)