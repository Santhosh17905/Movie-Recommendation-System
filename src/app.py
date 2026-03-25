import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import pandas as pd
from model import hybrid, content_based
from utils import fetch_poster, fetch_posters_batch
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_pickle("models/movies.pkl")

movies = load_data()

# ---------------- CSS ----------------
st.markdown("""
<style>
body { background-color: #141414; color: white; }

.title { font-size: 50px; font-weight: bold; }

.card {
    border-radius: 12px;
    overflow: hidden;
    transition: transform 0.3s ease;
}
.card:hover {
    transform: scale(1.08);
}

.movie-title {
    text-align: center;
    font-size: 14px;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- MOVIE CARD ----------------
def movie_card(movie_name, data=None):
    if not data:
        data = fetch_poster(movie_name)

    if not data:
        st.image("https://via.placeholder.com/300x450?text=No+Image")
        st.write(movie_name)
        return

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(data.get("poster") or "https://via.placeholder.com/300x450")
    st.markdown(f"<div class='movie-title'>{data.get('title')}</div>", unsafe_allow_html=True)
    st.markdown(f"⭐ {data.get('rating', 'N/A')}")

    with st.expander("▶ Details"):
        if data.get("backdrop"):
            st.image(data["backdrop"])
        st.write("📅 Release:", data.get("release"))
        st.write("📝 Overview:", data.get("overview"))
        if data.get("trailer"):
            st.video(data["trailer"])

    st.write("DEBUG:", movie_name, fetch_poster(movie_name))
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- GRID / SCROLL ----------------
def show_movies(movie_list):
    posters = fetch_posters_batch(movie_list)

    html = "<div style='display:flex; overflow-x:auto; padding:10px'>"
    for movie in movie_list:
        data = posters.get(movie)
        poster = data["poster"] if data and data.get("poster") else "https://via.placeholder.com/150x220"
        html += f"""
        <div style="margin-right:15px; text-align:center;">
            <img src="{poster}" width="150" style="border-radius:10px;">
            <p style="width:150px; font-size:14px;">{movie}</p>
        </div>
        """
    html += "</div>"

    components.html(html, height=300, scrolling=True)

# ---------------- NEW FEATURE: Title Banner ----------------
def show_title():
    st.markdown("""
    <h1 style='font-size:35px; font-weight:900; text-align:center; color:black; margin-bottom:10px'>
    🎬 Movie Recommendation System
    </h1>
    <p style='text-align:center; font-size:18px; color:gray;'>
    Discover movies you'll love instantly
    </p>
    """, unsafe_allow_html=True)

# ---------------- NEW FEATURE: Featured Movie Banner ----------------
def featured_movie():
    movie = movies.sample(1)['title'].values[0]
    data = fetch_poster(movie)
    if data and data.get("backdrop"):
        st.image(data["backdrop"], use_container_width=True)
        st.markdown(f"""
        <h2 style='color:white;'>{data.get("title")}</h2>
        <p>{data.get("overview", "")[:200]}...</p>
        """, unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio("Menu", ["🏠 Home", "🔍 Search", "🎯 Recommend"])

# ---------------- HOME ----------------
if menu == "🏠 Home":
    # --- New Title ---
    show_title()

    # --- Refresh Button ---
    if st.button("🔄 Refresh Movies"):
        st.cache_data.clear()

    # --- Featured Movie ---
    featured_movie()

    # --- Existing Trending and Top Picks ---
    st.markdown("## 🔥 Trending Now")
    try:
        show_movies(movies.sample(10)['title'].values)
    except:
        st.error("Error loading trending movies")

    st.markdown("## ⭐ Top Picks")
    try:
        show_movies(movies.sample(10)['title'].values)
    except:
        st.error("Error loading top picks")

# ---------------- SEARCH ----------------
elif menu == "🔍 Search":
    movie_list = movies['title'].values
    selected = st.selectbox("Search Movie", movie_list)

    st.markdown("## 🎬 Similar Movies")

    try:
        recs = content_based(selected)
        show_movies(recs)
    except:
        st.error("Error in recommendation")

# ---------------- RECOMMEND ----------------
elif menu == "🎯 Recommend":
    movie_list = movies['title'].values
    selected = st.selectbox("Choose Movie", movie_list)
    user_id = st.number_input("User ID", min_value=1)

    if st.button("Recommend"):
        try:
            recs = hybrid(user_id, selected)
            st.markdown("## 🍿 Recommended For You")
            show_movies(recs)
        except:
            st.error("Error generating recommendations")