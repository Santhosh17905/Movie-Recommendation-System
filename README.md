# 🎬 Movie Recommendation System (OTT AI Platform)

## 🚀 Project Overview

This project is a **full-stack Movie Recommendation System** built using Machine Learning and deployed with a modern **OTT-style UI** using Streamlit.

It combines:

* 🎯 Content-Based Filtering
* 🤝 Collaborative Filtering (SVD)
* 🔥 Hybrid Recommendation System

Additionally, it integrates with **TMDB API** to fetch:

* Movie Posters 🎥
* Ratings ⭐
* Trailers ▶️

---

## ✨ Features

### 🧠 Machine Learning

* Content-based recommendation using cosine similarity
* Collaborative filtering using SVD
* Hybrid recommendation system

### 🎨 UI (Netflix Style)

* Sidebar navigation
* Trending movies section
* Top picks section
* Search with recommendations
* Poster display
* Trailer preview
* Expandable movie details

### ⚡ Performance

* Streamlit caching
* Optimized API calls
* Error handling

---

## 🏗️ Project Structure

Movie_Recommendation_System/
│
├── notebook/
│   └── movie_recommendation.ipynb
│
├── src/
│   ├── app.py
│   ├── model.py
│   ├── utils.py
│
├── data/
│   └── ml-1m/
│
├── models/
│   ├── model.pkl
│   ├── cosine.pkl
│   ├── movies.pkl
│
├── .env
├── requirements.txt
├── README.md
└── .gitignore

---

## 📊 Dataset

Dataset used: MovieLens (1M)

Includes:

* Movies metadata
* User ratings
* User information

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/Movie_Recommendation_System.git
cd Movie_Recommendation_System
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv myenv
```

Activate:

**Windows**

```bash
myenv\Scripts\activate
```

**Mac/Linux**

```bash
source myenv/bin/activate
```

---

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🔐 TMDB API Setup

1. Go to https://www.themoviedb.org/
2. Create account
3. Go to Settings → API
4. Generate **API Key (v3 auth)**

---

### 📌 Add `.env` File

Create `.env` in root folder:

```env
TMDB_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run src/app.py
```

## 🧠 How It Works

### Content-Based Filtering

* Uses movie metadata (genres, tags)
* Cosine similarity

### Collaborative Filtering

* Uses user ratings
* Matrix factorization (SVD)

### Hybrid System

* Combines both methods
* Improves recommendation accuracy

---

## 🚀 Future Improvements

* 🔐 User authentication system
* 📊 User watch history tracking
* ⚡ FastAPI backend
* ⚛️ React frontend (full OTT clone)
* 🧠 Deep learning recommendations
* 🎥 Auto-play trailers on hover

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit 🎨
* Pandas & NumPy 📊
* Scikit-learn 🤖
* Surprise (SVD) 📉
* TMDB API 🎬

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork and improve the project.

---

## 📜 License

This project is for educational purposes.

---

## 👨‍💻 Author

Santhosh S

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
