import streamlit as st
import pickle
import pandas as pd
import numpy as np

def recommend(movie):
    movie_index=new_df[new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    for i in movies_list:
        st.write(new_df.iloc[i[0]].title)


new_df=pickle.load(open('movies.pkl','rb'))
movies_list=new_df['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

option=st.selectbox(
    'How would you like to be contacted?',
    movies_list
)
if st.button('Recommend'):
    recommend(option)