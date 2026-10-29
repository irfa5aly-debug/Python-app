


import streamlit as st

st.set_page_config(
    page_title="Gaming Hub",
    page_icon="🎮",
    layout="wide"
)

# Gaming theme
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #09091b, #171735);
    color: white;
}
h1, h2, h3 {
    color: #00f5ff;
}
div.stButton > button {
    background-color: #7c3aed;
    color: white;
    border-radius: 10px;
    border: none;
}
div.stButton > button:hover {
    background-color: #00bcd4;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🎮 GAMING HUB")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Games", "Leaderboard", "My Profile"]
)

# Sample game data
games = {
    "Free Fire": "🔥 Battle Royale",
    "PUBG Mobile": "🎯 Survival Shooter",
    "Minecraft": "🧱 Adventure",
    "Valorant": "⚡ Tactical Shooter"
}

if page == "Home":
    st.title("🎮 Welcome to Gaming Hub")
    st.subheader("Your Ultimate Gaming Zone")

    st.image(
        "https://images.unsplash.com/photo-1542751371-adc38448a05e",
        use_container_width=True
    )

    st.markdown("## 🚀 Explore Your Gaming World")

    col1, col2, col3 = st.columns(3)

    col1.metric("Available Games", "4")
    col2.metric("Total Players", "1,250")
    col3.metric("Online Players", "86")

    if st.button("Explore Games"):
        st.switch_page("pages/games.py") if False else (
            st.session_state.update({"explore": True})
        )

    if st.session_state.get("explore"):
        st.info("Select Games from the sidebar to continue.")

elif page == "Games":
    st.title("🕹️ Available Games")
    st.write("Choose your favorite game!")

    for game, description in games.items():
        with st.container(border=True):
            st.subheader(game)
            st.write(description)

            if st.button("Select " + game, key=game):
                st.session_state["selected_game"] = game
                st.success(f"You selected {game}!")

    if "selected_game" in st.session_state:
        st.info(
            "Current selection: "
            + st.session_state["selected_game"]
        )

elif page == "Leaderboard":
    st.title("🏆 Top Players")

    players = {
        "Rank": [1, 2, 3, 4, 5],
        "Player": [
            "ShadowX", "ProKiller", "Legend99",
            "NightWolf", "SniperKing"
        ],
        "Points": [9850, 9200, 8700, 8100, 7600]
    }

    st.dataframe(
        players,
        use_container_width=True,
        hide_index=True
    )

elif page == "My Profile":
    st.title("👤 Player Profile")

    username = st.text_input(
        "Enter your gaming username",
        placeholder="e.g. ShadowX"
    )

    favorite = st.selectbox(
        "Favorite Game",
        list(games.keys())
    )

    level = st.slider("Player Level", 1, 100, 25)

    if st.button("Save Profile"):
        if username.strip():
            st.session_state["username"] = username
            st.session_state["favorite"] = favorite
            st.session_state["level"] = level
            st.success("Profile saved for this session!")

    if "username" in st.session_state:
        st.markdown("### 🎮 Your Player Card")
        st.write("**Username:**", st.session_state["username"])
        st.write("**Favorite Game:**", st.session_state["favorite"])
        st.progress(st.session_state["level"] / 100)
        st.write("Level:", st.session_state["level"])

st.sidebar.markdown("---")
st.sidebar.caption("🎮 Gaming Hub | Play. Compete. Win.")
