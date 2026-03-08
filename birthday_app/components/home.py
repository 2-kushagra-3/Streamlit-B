# ─────────────────────────────────────────────────────────────────────────────
# components/home.py
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
from config import MOODS
from styles import inject_page_styles


def render_home():
    inject_page_styles("home")

    st.balloons()

    st.markdown("""
    <style>
    .home-btn-row div[data-testid="stButton"] > button {
        background: rgba(255,255,255,0.07) !important;
        border: 1.5px solid rgba(255,255,255,0.22) !important;
        color: rgba(255,255,255,0.88) !important;
        border-radius: 50px !important;
        font-size: .88rem !important;
        font-weight: 500 !important;
        transition: all .22s ease !important;
        width: 100% !important;
    }
    .home-btn-row div[data-testid="stButton"] > button:hover {
        background: rgba(255,255,255,0.16) !important;
        border-color: rgba(255,255,255,0.5) !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 24px rgba(0,0,0,0.4) !important;
    }
    .bday-name {
        font-family: 'Playfair Display', serif !important;
        font-size: clamp(3rem, 10vw, 6rem) !important;
        font-weight: 700 !important;
        color: #ffffff !important;
        letter-spacing: .04em !important;
        line-height: 1.05 !important;
        text-align: center !important;
        margin: 0 0 6px !important;
        text-shadow:
            0 0 0px #fff,
            0 0 18px rgba(255, 230, 80, 0.9),
            0 0 40px rgba(255, 180, 0, 0.7),
            0 0 80px rgba(255, 140, 0, 0.4),
            0 4px 12px rgba(0, 0, 0, 0.7) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        display:flex; flex-direction:column; align-items:center;
        text-align:center; padding: 60px 20px 0; position:relative;
    ">
        <div class="confetti-bg"></div>
        <div class="bday-emoji">🎬</div>
        <div class="stars">
            <span class="star">⭐</span><span class="star">🌟</span>
            <span class="star">✨</span><span class="star">🌟</span><span class="star">⭐</span>
        </div>
        <h1 class="bday-name">Your Cinema Menu</h1>
        <p class="bday-subtitle">A gift that was made for your birthday, and kept alive because, why not? 🎞️</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="bday-card">
        <div class="bday-message-text">
            Your birthday might be over, but that doesn't mean the party has to stop. You can still keep celebrating and make the most of it.🎂<br><br>
            This started as a <strong>birthday gift</strong>, a little world of
            <strong>movies and music</strong>, put together with care. But great stories don't
            have expiry dates, and good songs don't stop mattering just because the cake is gone.
            <strong>So it stays</strong>. 🎁<br><br>
            Feel free to drop by anytime you're in the mood for a good laugh, a romantic tale, an adrenaline rush, a blast from the past, or a thrilling story that keeps you guessing.
            We've got something for every emotion, so you can always find what you're looking for. 🎞️<br><br>
            Sometimes you just need something to match your mood, and that's it - no special occasion or reason needed. You can find the perfect thing to watch or listen to, and it'll be right there waiting for you. It's always available, whenever you want it. 🥂✨
        </div>
        <div class="card-divider"></div>
        <p class="mood-prompt">✦ &nbsp; what's your mood today? &nbsp; ✦</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="home-btn-row">', unsafe_allow_html=True)
    _, inner, _ = st.columns([0.3, 5.4, 0.3])
    with inner:
        btn_cols = st.columns(len(MOODS))
        for i, mood in enumerate(MOODS):
            with btn_cols[i]:
                if st.button(mood["label"], key=f"home_pick_{mood['key']}", use_container_width=True):
                    st.session_state.selected_mood = mood["key"]
                    st.rerun()

        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
        _, hp_col, _ = st.columns([1.5, 2, 1.5])
        with hp_col:
            if st.button("💝 My Handpicked List", key="home_handpicked", use_container_width=True):
                st.session_state.selected_mood = "handpicked"
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)