import streamlit as st
import pickle
import pandas as pd
import requests  # You need this to make API calls

# Helper function to fetch poster URL using TMDB API
def fetch_poster(movie_id):
    # Your active TMDB API key inserted below
    api_key = "8a05695ef3043ed1d01bb7ed8eab9e0d"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    
    try:
        data = requests.get(url).json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except Exception as e:
        # Fallback image if something goes wrong or poster doesn't exist
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    
    for i in movies_list:
        # 1. Get the actual TMDB movie ID from your dataframe
        # Fixed: Changed .movie_id to .id to resolve the AttributeError
        movie_id = new_df.iloc[i[0]].id 
        
        # 2. Append title
        recommended_movies.append(new_df.iloc[i[0]].title)
        
        # 3. Fetch poster using the helper function
        recommended_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_posters


# Load data
new_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = new_df['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

option = st.selectbox(
    'Select a movie to get recommendations:',
    movies_list
)

if st.button('Recommend'):
    names, posters = recommend(option)
    
    # Create 5 columns to display movies side-by-side layout
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])