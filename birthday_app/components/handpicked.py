# ─────────────────────────────────────────────────────────────────────────────
# components/handpicked.py  —  your personal curated movies & songs
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
from config import HANDPICKED_MOVIES, HANDPICKED_SONGS
from styles import inject_page_styles

# Visual theme for the handpicked page
THEME = {
    "bg":       "linear-gradient(135deg,#1a0a2e 0%,#2d1060 50%,#1a0a2e 100%)",
    "page_bg":  """
        background: #08001a !important;
        background-image:
            radial-gradient(ellipse at 20% 30%, rgba(120,0,255,0.3)  0%, transparent 55%),
            radial-gradient(ellipse at 80% 70%, rgba(200,0,150,0.25) 0%, transparent 55%),
            radial-gradient(ellipse at 50% 5%,  rgba(80,0,180,0.2)   0%, transparent 40%) !important;
    """,
    "card_bg":  "#120828",
    "song_bg":  "#0e0520",
    "accent":   "#c084fc",
    "text":     "#f0e6ff",
}


def _movie_card(movie: dict) -> str:
    poster   = movie.get("poster", "")
    title    = movie.get("title", "Unknown")
    year     = movie.get("year", "")
    rating   = movie.get("rating", 0)
    overview = movie.get("overview", "")
    note     = movie.get("note", "")

    img_html = (
        f'<img src="{poster}" alt="{title}" loading="lazy"/>'
        if poster and "REPLACE" not in poster
        else '<div style="font-size:3rem;text-align:center;padding:32px 0;background:rgba(192,132,252,0.08);">🎬</div>'
    )
    note_html = (
        f'<div class="handpick-note">💬 {note}</div>' if note else ""
    )
    return f"""
    <div class="movie-card" style="background:{THEME['card_bg']};box-shadow:0 8px 26px rgba(0,0,0,.4);">
        {img_html}
        <div class="mc-info" style="color:{THEME['text']};">
            <div class="badge" style="background:{THEME['accent']};color:#08001a;">★ {rating:.1f}</div>
            <div class="mc-title">{title}</div>
            <div class="mc-meta">{year}</div>
            <div class="mc-overview">{overview}</div>
            {note_html}
        </div>
    </div>"""


def _song_row(song: dict) -> str:
    title  = song.get("title", "Unknown")
    artist = song.get("artist", "")
    url    = song.get("url", "#")
    note   = song.get("note", "")

    # Detect platform for icon
    if "spotify.com" in url:
        icon, platform = "🟢", "Spotify"
    elif "youtu" in url:
        icon, platform = "▶️", "YouTube"
    elif "jiosaavn" in url:
        icon, platform = "🎵", "JioSaavn"
    elif "gaana" in url:
        icon, platform = "🎵", "Gaana"
    else:
        icon, platform = "🎵", "Listen"

    note_html = f'<div style="font-size:.7rem;opacity:.5;margin-top:3px;">💬 {note}</div>' if note else ""
    link_html = (
        f'<a class="song-link" href="{url}" target="_blank" style="color:{THEME["accent"]};">{icon} {platform} ↗</a>'
        if url and "REPLACE" not in url
        else f'<span style="font-size:.7rem;opacity:.35;">no link yet</span>'
    )
    return f"""
    <div class="song-row" style="background:{THEME['song_bg']};color:{THEME['text']};">
        <div class="song-cover" style="background:rgba(192,132,252,0.12);">🎵</div>
        <div class="song-info">
            <div class="song-title">{title}</div>
            <div class="song-artist">{artist}</div>
            {note_html}
        </div>
        {link_html}
    </div>"""


def render_handpicked_page():
    inject_page_styles("handpicked")

    # Header banner
    st.markdown(f"""
    <div class="mood-header" style="background:{THEME['bg']};color:{THEME['text']};">
        <div style="font-size:2.6rem;">💝</div>
        <div class="mood-title">Handpicked for You</div>
        <div class="mood-tagline">A personal selection</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Unique container key — ensures Streamlit never reuses widget state
    # from mood pages (which also have a Movies/Songs tab pair)
    with st.container(key="handpicked_container"):

        tab_movies, tab_songs = st.tabs(["🎬  Movies", "🎵  Songs"])

        # ── Movies tab ────────────────────────────────────────────────────────
        with tab_movies:
            movies              = [m for m in HANDPICKED_MOVIES if "REPLACE" not in m.get("poster", "")]
            placeholder_movies  = [m for m in HANDPICKED_MOVIES if "REPLACE"     in m.get("poster", "")]

            if not HANDPICKED_MOVIES:
                st.markdown(f"""
                <div style="text-align:center;padding:60px 20px;color:{THEME['text']};opacity:.5;">
                    <div style="font-size:3rem;margin-bottom:16px;">🎬</div>
                    <div style="font-size:1.1rem;font-weight:500;">No movies added yet</div>
                    <div style="font-size:.85rem;margin-top:8px;">
                        Open <code>config.py</code> and fill in <code>HANDPICKED_MOVIES</code>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                cols = st.columns(4)
                for idx, movie in enumerate(movies + placeholder_movies):
                    with cols[idx % 4]:
                        st.markdown(_movie_card(movie), unsafe_allow_html=True)

        # ── Songs tab ─────────────────────────────────────────────────────────
        with tab_songs:
            if not HANDPICKED_SONGS:
                st.markdown(f"""
                <div style="text-align:center;padding:60px 20px;color:{THEME['text']};opacity:.5;">
                    <div style="font-size:3rem;margin-bottom:16px;">🎵</div>
                    <div style="font-size:1.1rem;font-weight:500;">No songs added yet</div>
                    <div style="font-size:.85rem;margin-top:8px;">
                        Open <code>config.py</code> and fill in <code>HANDPICKED_SONGS</code>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                left, right = st.columns(2)
                for idx, song in enumerate(HANDPICKED_SONGS):
                    (left if idx % 2 == 0 else right).markdown(
                        _song_row(song), unsafe_allow_html=True
                    )

    st.markdown("""
    <div class="app-footer">
        Made with ❤️ &nbsp;
    </div>
    """, unsafe_allow_html=True)