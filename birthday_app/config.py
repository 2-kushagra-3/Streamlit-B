# ─────────────────────────────────────────────────────────────────────────────
# config.py  —  mood definitions and handpicked content
# API keys are loaded from Streamlit secrets (secrets.toml locally,
# or the Streamlit Cloud "Secrets" panel when deployed).
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st

# ── API keys — read from st.secrets, never hardcoded ─────────────────────────
TMDB_API_KEY   = st.secrets["TMDB_API_KEY"]
LASTFM_API_KEY = st.secrets["LASTFM_API_KEY"]

# API base URLs
TMDB_BASE   = "https://api.themoviedb.org/3"
POSTER_BASE = "https://image.tmdb.org/t/p/w500"
LASTFM_BASE = "https://ws.audioscrobbler.com/2.0/"

# ─────────────────────────────────────────────────────────────────────────────
# Mood definitions
# ─────────────────────────────────────────────────────────────────────────────
MOODS = [
    {
        "key":              "feel_good",
        "label":            "😂 Feel Good",
        "emoji":            "😂",
        "tagline":          "Laugh until your cheeks hurt",
        "movie_genres":     [35, 10751],
        "movie_sort":       "popularity.desc",
        "lastfm_tag":       "happy",
        "lastfm_hindi_tag": "bollywood",
        "bg":               "linear-gradient(135deg,#FF6B6B 0%,#FFE66D 50%,#FF6B6B 100%)",
        "card_bg":          "#fff9f0",
        "song_bg":          "#fff3e0",
        "accent":           "#FF6B6B",
        "text":             "#2d1b00",
    },
    {
        "key":              "romantic",
        "label":            "💕 Romantic",
        "emoji":            "💕",
        "tagline":          "Stories that make your heart flutter",
        "movie_genres":     [10749],
        "movie_sort":       "vote_average.desc",
        "lastfm_tag":       "romance",
        "lastfm_hindi_tag": "hindi romantic",
        "bg":               "linear-gradient(135deg,#f953c6 0%,#b91d73 100%)",
        "card_bg":          "#fff0f8",
        "song_bg":          "#fde8f5",
        "accent":           "#b91d73",
        "text":             "#2d0020",
    },
    {
        "key":              "action",
        "label":            "💥 Action",
        "emoji":            "💥",
        "tagline":          "Buckle up — it's going to be wild",
        "movie_genres":     [28, 12],
        "movie_sort":       "popularity.desc",
        "lastfm_tag":       "rock",
        "lastfm_hindi_tag": "hindi rock",
        "bg":               "linear-gradient(135deg,#0f0c29 0%,#302b63 50%,#24243e 100%)",
        "card_bg":          "#1a1a2e",
        "song_bg":          "#12102a",
        "accent":           "#e94560",
        "text":             "#ffffff",
    },
    {
        "key":              "nostalgia",
        "label":            "🎞️ Nostalgia",
        "emoji":            "🎞️",
        "tagline":          "Classics that stood the test of time",
        "movie_genres":     [18, 35],
        "movie_sort":       "vote_average.desc",
        "movie_extra":      {
            "primary_release_date.lte": "1999-12-31",
            "primary_release_date.gte": "1960-01-01",
        },
        "lastfm_tag":       "classic",
        "lastfm_hindi_tag": "retro hindi",
        "bg":               "linear-gradient(135deg,#8B6914 0%,#D4A843 50%,#8B6914 100%)",
        "card_bg":          "#fdf6e3",
        "song_bg":          "#f9f0d0",
        "accent":           "#8B4513",
        "text":             "#2c1a00",
    },
    {
        "key":              "thriller",
        "label":            "🔪 Thriller",
        "emoji":            "🔪",
        "tagline":          "Who did it? You won't see it coming",
        "movie_genres":     [53, 9648],
        "movie_sort":       "vote_average.desc",
        "lastfm_tag":       "dark",
        "lastfm_hindi_tag": "hindi suspense",
        "bg":               "linear-gradient(135deg,#0d0d0d 0%,#1a0a2e 50%,#0d0d0d 100%)",
        "card_bg":          "#110d1a",
        "song_bg":          "#0d0a18",
        "accent":           "#00e5ff",
        "text":             "#e0e0e0",
    },
]

MOOD_MAP = {m["key"]: m for m in MOODS}

# ─────────────────────────────────────────────────────────────────────────────
# HANDPICKED — your personal curated list (see HANDPICKED_GUIDE.md)
# ─────────────────────────────────────────────────────────────────────────────
HANDPICKED_MOVIES = [
    # ── paste your entries here, following this format ──
    {
        "title":    "Knives Out",
        "year":     "2019",
        "poster":   "https://media.themoviedb.org/t/p/w600_and_h900_face/pThyQovXQrw2m0s9x82twj48Jq4.jpg",
        "rating":   9.5,
        "overview": "Probably the most engaging out of the trilogy.",
        "note":     "I guess the 1st movie we saw togeather?",
    },
     {
        "title":    "Gifted",
        "year":     "2017",
        "poster":   "https://media.themoviedb.org/t/p/w600_and_h900_face/9Ts7Vc4wLlpI9oox9mkVUE1tBHy.jpg",
        "rating":   9.78,
        "overview": "Probably a movie I would alway come back to after a long day",
        "note":     "I happen to know that you love this movie",
    },
    {
        "title":    "Up",
        "year":     "2009",
        "poster":   "https://media.themoviedb.org/t/p/w600_and_h900_face/mFvoEwSfLqbcWwFsDjQebn9bzFe.jpg",
        "rating":   9.47,
        "overview": "The movie feels like a safe place",
        "note":     "Not sure why this is in the handpicked page, justed wanted this to be here",
    },
    {
        "title":    "Anand",
        "year":     "1971",
        "poster":   "https://media.themoviedb.org/t/p/w600_and_h900_face/vgrege8e0yk3SSdHzHfMTvk2ffc.jpg",
        "rating":   9.47,
        "overview": "Gives life a postive perspective",
        "note":     "Again, Not sure why this is in the handpicked page, justed wanted this to be here",
    },
    # add more movies below...
]

HANDPICKED_SONGS = [
    # ── paste your entries here, following this format ──
    {
        "title":    "Joy",
        "artist":   "For King & Country",
        "url":      "https://open.spotify.com/track/0vBjd0I8iefycEZ2ex1Zpi?si=dc5ffa72b10f416c",
        "note":     "Just like this song for some readon, you should give this a go!",
    },
     {
        "title":    "WHERE IS MY HUSBAND",
        "artist":   "Raye",
        "url":      "https://open.spotify.com/track/55lijDD6OAjLFFUHU9tcDm?si=8d977b6b5cc34bc8",
        "note":     "I have a feeling you happen to like this song?",
    },
    {
        "title":    "Chaand Chahiye",
        "artist":   "Ankur Tiwari",
        "url":      "https://open.spotify.com/track/1jZxJeaRMbCSg9Cg6AjXUn?si=1427beba7d144c9b",
        "note":     "Love the vibe of thi song, seems playful",
    },
    {
        "title":    "yeh Raaten Yeh Mausam",
        "artist":   "Kishore, Asha",
        "url":      "https://open.spotify.com/track/5ZKMBzpA8E2dDOmL06pK3J?si=3ac149d5512d4dfe",
        "note":     "This song always soothes me down",
    },
     {
        "title":    "505",
        "artist":   "Arctic Monkeys",
        "url":      "https://open.spotify.com/track/0BxE4FqsDD1Ot4YuBXwAPp?si=5aaf1ac7295f42d8",
        "note":     "This had to be here for some unknow reason",
    },
    {
        "title":    "Co2",
        "artist":   "Prateek Khuad",
        "url":      "https://open.spotify.com/track/3hB9lDLyAClYVZivMMl20N?si=4cc75f34d1db44d7",
        "note":     "Lov how simple this song is",
    },
    # add more songs below...
]