# ─────────────────────────────────────────────────────────────────────────────
# data.py  —  all API calls (TMDB movies + Last.fm songs)
# ─────────────────────────────────────────────────────────────────────────────
import random
import requests
import streamlit as st

from config import (
    TMDB_API_KEY, LASTFM_API_KEY,
    TMDB_BASE, POSTER_BASE, LASTFM_BASE,
)

# ── Movies ────────────────────────────────────────────────────────────────────

@st.cache_data(ttl=600, show_spinner=False)
def fetch_movies(genre_ids: tuple, sort_by: str, extra_items: tuple, page: int):
    """
    Fetch movies from TMDB restricted to English OR Hindi originals.
    We make two calls (en + hi) and merge, then shuffle and return 8.
    """
    results = []
    for lang in ("en", "hi"):
        params = {
            "api_key":                TMDB_API_KEY,
            "sort_by":                sort_by,
            "vote_count.gte":         300,
            "with_genres":            ",".join(map(str, genre_ids)),
            "with_original_language": lang,
            "page":                   page,
            "language":               "en-US",   # response language (titles/overviews)
            **dict(extra_items),
        }
        try:
            r = requests.get(f"{TMDB_BASE}/discover/movie", params=params, timeout=8)
            if r.status_code == 200:
                results += r.json().get("results", [])
        except Exception:
            pass

    random.shuffle(results)
    return results[:8]


def parse_movie(raw: dict) -> dict:
    overview = raw.get("overview", "")
    return {
        "poster":   (POSTER_BASE + raw["poster_path"]) if raw.get("poster_path") else None,
        "title":    raw.get("title", "Unknown"),
        "year":     raw.get("release_date", "")[:4],
        "rating":   raw.get("vote_average", 0),
        "overview": overview[:110] + "…" if len(overview) > 110 else overview,
        "lang":     raw.get("original_language", ""),
    }


# ── Songs ─────────────────────────────────────────────────────────────────────

@st.cache_data(ttl=600, show_spinner=False)
def fetch_songs(tag: str, hindi_tag: str, page: int):
    """
    Fetch tracks from Last.fm using both an English mood tag and a Hindi one,
    then merge and return 8 shuffled tracks.
    """
    results = []
    for t in (tag, hindi_tag):
        if not t:
            continue
        params = {
            "method":  "tag.getTopTracks",
            "tag":     t,
            "api_key": LASTFM_API_KEY,
            "format":  "json",
            "limit":   30,
            "page":    page,
        }
        try:
            r = requests.get(LASTFM_BASE, params=params, timeout=8)
            if r.status_code == 200:
                results += r.json().get("tracks", {}).get("track", [])
        except Exception:
            pass

    random.shuffle(results)
    return results[:8]


def parse_song(raw: dict) -> dict:
    artist = raw.get("artist", {})
    return {
        "title":  raw.get("name", "Unknown"),
        "artist": artist.get("name", "") if isinstance(artist, dict) else str(artist),
        "url":    raw.get("url", "#"),
    }