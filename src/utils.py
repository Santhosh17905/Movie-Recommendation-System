import requests
import os
from dotenv import load_dotenv
import streamlit as st
import re

# ---------------- LOAD ENV ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, "..", ".env")
load_dotenv(env_path)

API_KEY = os.getenv("TMDB_API_KEY")

# ---------------- CLEAN TITLE ----------------
def clean_title(title):
    return re.sub(r"\(\d{4}\)", "", title).strip()

# ---------------- GET TRAILER ----------------
def get_trailer(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}"
        data = requests.get(url).json()

        for vid in data.get("results", []):
            if vid["type"] == "Trailer" and vid["site"] == "YouTube":
                return f"https://www.youtube.com/watch?v={vid['key']}"
    except:
        return None

    return None

# ---------------- FETCH SINGLE ----------------
@st.cache_data(show_spinner=False, ttl=86400)
def fetch_poster(movie_name):
    try:
        if not API_KEY:
            return None

        clean = clean_title(movie_name)

        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={clean}"
        data = requests.get(url, timeout=10).json()

        if not data.get("results"):
            return None

        # pick first with poster
        for movie in data["results"]:
            if movie.get("poster_path"):
                movie_id = movie.get("id")

                return {
                    "title": movie.get("title"),
                    "poster": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
                    "backdrop": f"https://image.tmdb.org/t/p/w500{movie.get('backdrop_path')}" if movie.get("backdrop_path") else None,
                    "rating": movie.get("vote_average"),
                    "overview": movie.get("overview"),
                    "release": movie.get("release_date"),
                    "trailer": get_trailer(movie_id)
                }

        return None

    except:
        return None

# ---------------- BATCH FETCH ----------------
@st.cache_data(show_spinner=False)
def fetch_posters_batch(movie_list):
    results = {}
    for movie in movie_list:
        results[movie] = fetch_poster(movie)
    return results