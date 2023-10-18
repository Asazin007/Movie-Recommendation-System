import streamlit as st
import pickle
import requests
# streamlit run app.py

movies=pickle.load(open("artifacts/movies_list.pkl",'rb'))
similarity=pickle.load(open("artifacts/similarity_list.pkl",'rb'))
movies_list=movies['title'].values

st.header("Movie Recommender System")
selectvalue=st.selectbox("Select movies from dropdown",movies_list)

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path  

def recommand(movie):
    index = movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True, key=lambda vector:vector[1])
    recommand_movies=[]
    movies_id=[]
    for i in distance[1:6]:
        movie_id=movies.iloc[i[0]].id
        recommand_movies.append(movies.iloc[i[0]].title)
        movies_id.append(fetch_poster(movie_id))
    return recommand_movies, movies_id

  
        
if st.button("Show Recommend"):
    sim_movies,movies_poster=recommand(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(sim_movies[0])
        st.image(movies_poster[0])
    with col2:
        st.text(sim_movies[1])
        st.image(movies_poster[1])
    with col3:
        st.text(sim_movies[2])
        st.image(movies_poster[2])
    with col4:
        st.text(sim_movies[3])
        st.image(movies_poster[3])
    with col5:
        st.text(sim_movies[4])
        st.image(movies_poster[4])
    
    
    