import pickle
import streamlit as st
import requests
from requests.exceptions import RequestException

API_KEY = "aeb55506caafa7850ecebbca0a4989c8"

@st.cache_data
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        data = requests.get(url)
        data.raise_for_status()
        data = data.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except RequestException:
        return None

@st.cache_data
def fetch_cast(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US"
        data = requests.get(url)
        data.raise_for_status()
        data = data.json()
        return [actor['name'] for actor in data['cast'][:5]]
    except RequestException:
        return []

movies = pickle.load(open('movie_list.pkl', 'rb'))
all_genres = sorted(set(genre for genres in movies['genres'] for genre in genres))

st.header('Movie Recommender System')
st.subheader("Search Movies by Genre")
selected_genre = st.selectbox("Select a genre", all_genres)

if st.button("Show Recommendations"):
    def recommend_all_movies_in_genre(selected_genre):
        genre_filtered = movies[movies['genres'].apply(lambda x: selected_genre in x)]
        if genre_filtered.empty:
            st.warning(f"No movies found for genre: {selected_genre}")
            return
        st.write(f"Movies in the genre '{selected_genre}':")
        for index, row in genre_filtered.iterrows():
            poster_url = fetch_poster(row['movie_id'])
            cast = fetch_cast(row['movie_id'])
            with st.container():
                if poster_url:
                    st.image(poster_url, width=150)
                st.markdown(f"### {row['title']}")
                st.caption(f"Genres: {', '.join(row['genres'])}")
                st.write("**Cast**: " + ", ".join(cast) if cast else "**Cast**: No cast information available.")
                st.divider()

    recommend_all_movies_in_genre(selected_genre)
