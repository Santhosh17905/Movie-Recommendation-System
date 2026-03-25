import os
import pickle
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = pickle.load(open(os.path.join(BASE_DIR, 'models/model.pkl'), 'rb'))
cosine_sim = pickle.load(open(os.path.join(BASE_DIR, 'models/cosine.pkl'), 'rb'))
movies = pickle.load(open(os.path.join(BASE_DIR, 'models/movies.pkl'), 'rb'))

movies = movies.reset_index(drop=True)
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# ---------------- CONTENT ----------------
def content_based(title):
    if title not in indices:
        return []

    idx = indices[title]
    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:11]

    movie_indices = [i[0] for i in scores]
    return movies['title'].iloc[movie_indices].tolist()

# ---------------- HYBRID ----------------
def hybrid(user_id, title):
    content_movies = content_based(title)

    movie_ids = movies[movies['title'].isin(content_movies)]['movieId']

    scores = []
    for m in movie_ids:
        pred = model.predict(user_id, m)
        scores.append((m, pred.est))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)[:10]

    recommendations = []
    for i, _ in scores:
        name = movies[movies['movieId'] == i]['title'].values
        if len(name) > 0:
            recommendations.append(name[0])

    return recommendations