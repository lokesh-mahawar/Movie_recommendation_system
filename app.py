import streamlit as st
import pickle

# Load processed data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        return "Movie not found"
    
    idx = movies[movies['title'].str.lower() == movie].index[0]
    distances = list(enumerate(similarity[idx]))
    movies_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    
    return [movies.iloc[i[0]].title for i in movies_list]

# --- Streamlit App ---
st.title("🎬 Movie Recommender")

selected_movie = st.selectbox("Choose a movie", movies['title'].sort_values().values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    if recommendations == "Movie not found":
        st.error("Sorry, movie not found!")
    else:
        st.subheader("You may also like:")
        for movie in recommendations:
            st.write(movie)
