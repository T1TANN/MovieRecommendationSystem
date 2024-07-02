import streamlit as st
import pickle
import pandas as pd
movie_dict=pickle.load(open("movie_dict.pkl","rb"))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open("similarity.pkl","rb"))

st.title("Movie Recommander System")