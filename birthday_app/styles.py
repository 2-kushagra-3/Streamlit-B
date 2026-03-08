# ─────────────────────────────────────────────────────────────────────────────
# styles.py  —  global CSS + per-page style injection
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st

# ── Per-page backgrounds ──────────────────────────────────────────────────────
_PAGE_BACKGROUNDS = {
    "home": """
        background: #0f0c1e !important;
        background-image:
            linear-gradient(135deg, #0f0c1e 0%, #16213e 45%, #0f3460 100%) !important;
    """,
    "feel_good": """
        background: #1a0500 !important;
        background-image:
            radial-gradient(ellipse at 20% 20%, rgba(255,140,0,0.35) 0%, transparent 55%),
            radial-gradient(ellipse at 80% 80%, rgba(255,60,60,0.25)  0%, transparent 55%),
            radial-gradient(ellipse at 55% 10%, rgba(255,220,0,0.20)  0%, transparent 40%) !important;
    """,
    "romantic": """
        background: #0d0010 !important;
        background-image:
            radial-gradient(ellipse at 25% 30%, rgba(220,0,130,0.45)  0%, transparent 55%),
            radial-gradient(ellipse at 75% 70%, rgba(140,0,180,0.35)  0%, transparent 55%),
            radial-gradient(ellipse at 50% 5%,  rgba(255,100,180,0.2) 0%, transparent 40%) !important;
    """,
    "action": """
        background: #040010 !important;
        background-image:
            radial-gradient(ellipse at 15% 40%, rgba(100,0,200,0.40) 0%, transparent 55%),
            radial-gradient(ellipse at 85% 60%, rgba(200,0,60,0.35)  0%, transparent 55%),
            radial-gradient(ellipse at 50% 95%, rgba(60,0,140,0.25)  0%, transparent 40%) !important;
    """,
    "nostalgia": """
        background: #100800 !important;
        background-image:
            radial-gradient(ellipse at 20% 25%, rgba(180,120,0,0.45) 0%, transparent 55%),
            radial-gradient(ellipse at 78% 75%, rgba(140,60,0,0.35)  0%, transparent 55%),
            radial-gradient(ellipse at 50% 5%,  rgba(220,180,50,0.2) 0%, transparent 40%) !important;
    """,
    "thriller": """
        background: #02000a !important;
        background-image:
            radial-gradient(ellipse at 20% 30%, rgba(0,180,220,0.20)  0%, transparent 55%),
            radial-gradient(ellipse at 80% 70%, rgba(80,0,140,0.25)   0%, transparent 55%),
            radial-gradient(ellipse at 50% 5%,  rgba(0,120,160,0.12)  0%, transparent 40%) !important;
    """,
    "handpicked": """
        background: #08001a !important;
        background-image:
            radial-gradient(ellipse at 20% 30%, rgba(120,0,255,0.30)  0%, transparent 55%),
            radial-gradient(ellipse at 80% 70%, rgba(200,0,150,0.25)  0%, transparent 55%),
            radial-gradient(ellipse at 50% 5%,  rgba(80,0,180,0.20)   0%, transparent 40%) !important;
    """,
}


def inject_page_styles(page_key: str):
    """
    Call once at the top of every page render.
    Writes the correct background for this page, explicitly clearing/overriding
    whatever the previous page may have set.
    Also resets the .handpick-note class so it only shows on the handpicked page.
    """
    bg = _PAGE_BACKGROUNDS.get(page_key, _PAGE_BACKGROUNDS["home"])

    # .handpick-note is only visible on the handpicked page
    handpick_note_css = (
        ".handpick-note { display: block; }"
        if page_key == "handpicked"
        else ".handpick-note { display: none !important; }"
    )

    st.markdown(f"""
    <style>
    /* ── Page background — overrides previous page every rerun ── */
    .stApp,
    .stApp > div,
    section.main > div {{
        {bg}
        min-height: 100vh;
    }}

    /* ── Tab panel width fix ── */
    .stTabs [data-baseweb="tab-panel"],
    .stTabs [data-baseweb="tab-panel"] > div,
    section.main .block-container {{
        width: 100% !important;
        max-width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }}

    /* ── Handpick note visibility ── */
    {handpick_note_css}
    </style>
    """, unsafe_allow_html=True)


def inject_global_styles():
    """Inject once at startup — fonts, layout, cards, tabs, etc."""
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    max-width: 100% !important;
}
section[data-testid="stSidebar"] { display: none; }

/* ── Centred tab pill bar ─────────────────────────────────────────────────── */
.stTabs { width: 100% !important; }
.stTabs [data-baseweb="tab-list"] {
    display: flex !important;
    justify-content: center !important;
    gap: 0;
    background: rgba(0,0,0,0.25);
    border-radius: 50px;
    padding: 5px;
    width: auto !important;
    margin: 0 auto !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 50px !important;
    padding: 11px 42px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: .95rem !important;
    font-weight: 500 !important;
    color: rgba(255,255,255,.5) !important;
    background: transparent !important;
    border: none !important;
    transition: all .25s ease;
}
.stTabs [aria-selected="true"] {
    background: rgba(255,255,255,.2) !important;
    color: white !important;
}
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] { display: none !important; }

/* ── Nav bar ──────────────────────────────────────────────────────────────── */
.mood-nav {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 10px 24px;
    background: rgba(5,5,15,0.9);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid rgba(255,255,255,0.07);
    flex-wrap: wrap;
    position: sticky;
    top: 0;
    z-index: 999;
}

/* ── Birthday hero ────────────────────────────────────────────────────────── */
.bday-emoji {
    font-size: 4.5rem; animation: bounce 1.5s infinite;
    margin-bottom: 14px; display: block; text-align: center;
}
@keyframes bounce {
    0%,100% { transform: translateY(0); }
    50%      { transform: translateY(-13px); }
}
.confetti-bg {
    position: fixed; inset: 0; pointer-events: none; z-index: 0;
    background-image:
        radial-gradient(circle at 20% 20%, rgba(255,107,107,.12) 0%, transparent 50%),
        radial-gradient(circle at 80% 80%, rgba(78,205,196,.12)  0%, transparent 50%),
        radial-gradient(circle at 60% 30%, rgba(255,230,109,.08) 0%, transparent 40%);
}
.bday-name {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.4rem,8vw,4.8rem);
    color: #FFE66D;
    margin: 0 0 8px;
    text-shadow: 0 0 40px rgba(255,230,109,.4);
    line-height: 1.1;
    text-align: center;
}
.bday-subtitle {
    font-size: clamp(.9rem,2.5vw,1.25rem);
    color: rgba(255,255,255,.65);
    margin-bottom: 28px;
    font-weight: 300;
    letter-spacing: .05em;
    text-align: center;
}
.stars { display: flex; gap: 6px; margin-bottom: 20px; justify-content: center; }
.star  { font-size: 1.3rem; animation: twinkle 2s infinite; }
.star:nth-child(2) { animation-delay: .3s; }
.star:nth-child(3) { animation-delay: .6s; }
.star:nth-child(4) { animation-delay: .9s; }
.star:nth-child(5) { animation-delay: 1.2s; }
@keyframes twinkle {
    0%,100% { opacity: 1; transform: scale(1); }
    50%      { opacity: .3; transform: scale(.8); }
}

/* ── Glass card on home page ─────────────────────────────────────────────── */
.bday-card {
    max-width: 700px;
    margin: 0 auto;
    background: rgba(255,255,255,.06);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255,255,255,.14);
    border-radius: 28px;
    padding: 34px 42px 24px;
}
.bday-message-text {
    font-size: 1.02rem;
    line-height: 1.85;
    color: rgba(255,255,255,.87);
    font-weight: 300;
}
.bday-message-text strong { color: #FFE66D; font-weight: 500; }
.card-divider {
    height: 1px;
    background: rgba(255,255,255,.1);
    margin: 22px 0 16px;
}
.mood-prompt {
    font-size: .8rem;
    color: rgba(255,255,255,.4);
    letter-spacing: .16em;
    text-transform: uppercase;
    text-align: center;
    margin-bottom: 14px;
}

/* ── Mood page header banner ──────────────────────────────────────────────── */
.mood-header {
    padding: 36px 40px 24px;
    text-align: center;
    border-radius: 0 0 36px 36px;
    margin-bottom: 0;
}
.mood-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.7rem,5vw,2.8rem);
    margin: 6px 0 5px;
    line-height: 1.1;
}
.mood-tagline { font-size: .95rem; opacity: .72; font-weight: 300; letter-spacing: .03em; }

/* ── Buttons ──────────────────────────────────────────────────────────────── */
div[data-testid="stButton"] > button {
    border-radius: 50px !important;
    font-weight: 500 !important;
    padding: 8px 24px !important;
    transition: all .2s ease !important;
}

/* ── Movie card ───────────────────────────────────────────────────────────── */
.movie-card {
    border-radius: 16px;
    overflow: hidden;
    transition: transform .3s ease, box-shadow .3s ease;
    margin-bottom: 4px;
}
.movie-card:hover { transform: translateY(-7px); }
.movie-card img   { width: 100%; aspect-ratio: 2/3; object-fit: cover; display: block; }
.mc-info { padding: 11px 12px; }
.mc-title {
    font-family: 'Playfair Display', serif;
    font-weight: 700; font-size: .92rem;
    margin: 0 0 3px; line-height: 1.3;
}
.mc-meta     { font-size: .73rem; opacity: .6;  margin-bottom: 5px; }
.mc-overview { font-size: .71rem; opacity: .55; line-height: 1.5; }
.badge {
    display: inline-block; padding: 2px 8px;
    border-radius: 20px; font-size: .7rem; font-weight: 700; margin-bottom: 5px;
}

/* ── Handpick note (hidden by default; shown only on handpicked page) ─────── */
.handpick-note {
    font-size: .7rem;
    color: #c084fc;
    opacity: .85;
    margin-top: 6px;
    font-style: italic;
    display: none;
}

/* ── Song row ─────────────────────────────────────────────────────────────── */
.song-row {
    display: flex; align-items: center; gap: 13px;
    padding: 11px 14px; border-radius: 14px; margin-bottom: 9px;
    transition: transform .2s ease;
}
.song-row:hover { transform: translateX(4px); }
.song-cover {
    width: 48px; height: 48px; border-radius: 10px;
    flex-shrink: 0; background: rgba(255,255,255,.08);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem;
}
.song-info  { flex: 1; min-width: 0; }
.song-title {
    font-weight: 500; font-size: .87rem;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.song-artist { font-size: .75rem; opacity: .6; margin-top: 2px; }
.song-link   { font-size: .74rem; opacity: .55; white-space: nowrap; text-decoration: none; }
.song-link:hover { opacity: 1; }

/* ── Footer ───────────────────────────────────────────────────────────────── */
.app-footer {
    text-align: center; padding: 26px;
    opacity: .28; font-size: .75rem;
    border-top: 1px solid rgba(255,255,255,.05);
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)