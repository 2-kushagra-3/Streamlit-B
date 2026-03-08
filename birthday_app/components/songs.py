# ─────────────────────────────────────────────────────────────────────────────
# components/songs.py  —  song list renderer (mood-based, English + Hindi)
# ─────────────────────────────────────────────────────────────────────────────
import random
import streamlit as st
from data import fetch_songs, parse_song


def render_song_list(mood: dict):
    key  = mood["key"]
    page = st.session_state.get(f"song_page_{key}", 1)

    songs = fetch_songs(
        tag        = mood["lastfm_tag"],
        hindi_tag  = mood.get("lastfm_hindi_tag", ""),
        page       = page,
    )

    # Centred shuffle button
    _, c_btn, _ = st.columns([2, 1, 2])
    with c_btn:
        if st.button("🔀 Shuffle Songs", key=f"shuf_sg_{key}", use_container_width=True):
            st.session_state[f"song_page_{key}"] = random.randint(1, 5)
            st.cache_data.clear()
            st.rerun()

    st.markdown(
        '<p style="text-align:center;font-size:.72rem;opacity:.4;margin-top:4px;">click Listen ↗ to open</p>',
        unsafe_allow_html=True,
    )

    if not songs:
        st.error("Couldn't load songs — check your Last.fm API key in config.py")
        return

    left, right = st.columns(2)
    for idx, raw in enumerate(songs):
        song = parse_song(raw)
        card = f"""
        <div class="song-row" style="background:{mood['song_bg']};color:{mood['text']};">
            <div class="song-cover">🎵</div>
            <div class="song-info">
                <div class="song-title">{song['title']}</div>
                <div class="song-artist">{song['artist']}</div>
            </div>
            <a class="song-link" href="{song['url']}" target="_blank"
               style="color:{mood['accent']};">Listen ↗</a>
        </div>"""
        (left if idx % 2 == 0 else right).markdown(card, unsafe_allow_html=True)