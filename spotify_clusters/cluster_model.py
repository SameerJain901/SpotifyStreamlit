from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.cluster import KMeans
import streamlit as st
import numpy as np
import pickle
import pandas as pd


def do_prediction(data):
    pickle_data=pickle.load(open('spotify_clusters/Assets/pickle_data.pk','rb'))
    songs_clusters=pd.read_csv('spotify_clusters/Assets/clusters.csv.zip',compression='zip')
    acousticness = st.slider('Select level of Acousticness',0.0,1.0,0.5,0.01)
    danceability = st.slider('Select level of Danceability',0.0,1.0,0.5,0.01)
    energy = st.slider('Select level of Energy',0.0,1.0,0.5,0.01)
    instrumentalness = st.slider('Select level of Instrumentalness',0.0,1.0,0.5,0.01)
    liveness = st.slider('Select level of Liveness',0.0,1.0,0.5,0.01)
    loudness = st.slider('Select level of Loudness',-60.0,3.0,0.5,0.01)
    popularity = st.slider('Select level of Popularity',0.0,100.0,0.5,0.1)
    speechiness = st.slider('Select level of Speechiness',0.0,1.0,0.5,0.01)
    tempo = st.slider('Select level of Tempo',0.0,243.0,0.5,0.1)
    valence = st.slider('Select level of Valence',0.0,1.0,0.5,0.01)
    predict=st.button('Predict Cluster')
    if predict:
        array=np.array([acousticness,danceability,energy,instrumentalness,
                        liveness,loudness,popularity,speechiness,tempo,valence]).reshape(1,-1)
        array=pickle_data['scaler'].transform(array)
        array=pickle_data['pca'].transform(array)
        cluster=pickle_data['model'].predict(array)[0]
        st.caption('Track belongs to cluster '+str(cluster))
        cluster_data=songs_clusters[songs_clusters.cluster==cluster]
        index=np.random.choice(cluster_data.index)
        st.subheader('Random Track which belongs to same cluster:')
        st.text(cluster_data.at[index,'name'])
        st.audio(cluster_data.at[index,'preview_url'])