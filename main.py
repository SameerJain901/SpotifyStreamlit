import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import spotify_clusters.spotify_utils as spu
import spotify_clusters.eda as eda
import spotify_clusters.cluster_model as cm
import pickle

st.set_page_config(  # Alternate names: setup_page, page, layout
	layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
    )

st.title("Spotify Tracks Clusters")
data=pd.read_csv('spotify_clusters/Assets/spotify_data.csv.zip',compression='zip')
cdata=pd.read_csv('spotify_clusters/Assets/cdata.csv')
scaled_data=pd.read_csv('spotify_clusters/Assets/scaled_data.csv.zip',compression='zip')
reduced_data=pd.read_csv('spotify_clusters/Assets/reduced_data.csv.zip',compression='zip')


st.sidebar.header('Select page to show: ')
pages=['About the Data','EDA','Model Prediction',
]
out=st.sidebar.radio('Page:',pages)
if out=='About the Data':
    st.header("About the data")
    st.markdown('''
    The data has following features:
    - __acousticness__: A measure from 0 to 1 to determine the track is acoustic or not.
    - __available_markets__: Country codes where the track is a available.
    - __danceability__: Rythmic score from 0-1 which determines how easier is it to dance.
    - __energy__: Amount of energy in the track from 0-1.
    - __instrumentalness__: Instrumentalness of the track.
    - __key__: Track key value.
    - __liveness__: Quality of track from 0-1.
    - __loudness__: Higher the value louder the track.
    - __name__: Name of the track.
    - __popularity__: Track popularity score.
    - __preview_url__: Preview link of the track.
    - __speechiness__: Amount of vocals in the track.
    - __tempo__: Tempo of the track.
    - __time_signature__: Length of the track in minutes.
    - __valence__: Positivity score of the track.''')
    st.subheader('Dataset sample')
    st.dataframe(data.head(10))

elif out=='EDA':
    eda.do_eda(data,cdata,scaled_data,reduced_data)
else:
    cm.do_prediction(data)
