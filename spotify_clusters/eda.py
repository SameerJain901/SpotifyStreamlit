import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import spotify_clusters.spotify_utils as spu

def do_eda(data,cdata,scaled_data,reduced_data):
    reduced_data.columns=['A','B','C']
    colb=st.selectbox('Select column name to compare:',['acousticness', 'danceability', 'energy',
        'instrumentalness', 'liveness', 'loudness', 
        'popularity', 'speechiness', 'tempo', 'valence'],6,lambda x:x.capitalize())
    gcat=data.groupby(['time_signature'])[colb].mean().reset_index()
    fig=px.bar(gcat,x=gcat.index,y=gcat[colb],color=gcat[colb]
                ,color_continuous_scale='greens')
    fig.layout.coloraxis.colorbar.title = colb.capitalize()
    fig.update_layout( xaxis_title="Time Signature",
        yaxis_title=colb.capitalize(),
        font=dict(family="Courier New, monospace",
            size=12,color="#56ab91"
        ))
    st.plotly_chart(fig)


    colc=st.selectbox('Select measure to see:', ['acousticness', 'danceability', 'energy',
                    'instrumentalness', 'liveness', 'loudness', 
                    'popularity', 'speechiness', 'tempo', 'valence'],6,lambda x:x.capitalize())
    country_options = st.multiselect(
        'Select countries to compare',
        spu.ccodes,
        ['IN','GB'],format_func=spu.getCountryName)
    st.plotly_chart(spu.getWorldFigure(cdata,'avg_'+colc.lower(),country_options))

    st.subheader("Eblow plot for n clusters")
    fig=go.Figure(go.Scatter(x=list(range(1, spu.max_cluster_count+1)),y=spu.inertias,mode='lines+markers',marker_color='green'))
    fig.update_layout( xaxis_title="N_Clusters",
        yaxis_title='Inertia',
        font=dict(family="Courier New, monospace",
            size=12,color="#56ab91"
        ))
    st.plotly_chart(fig)
    st.caption('K value is 5 clusters.')
    st.subheader('Visualizing Clustes')
    fig=px.scatter(x=reduced_data['B'],y=reduced_data['C'],color=scaled_data['cluster'],hover_name=['Cluster '+str(x) for x in scaled_data['cluster']]
    ,color_continuous_scale='algae')
    fig.update_layout( xaxis_title="PCA Column A",
        yaxis_title='PCA Column B',
        font=dict(family="Courier New, monospace",
            size=12,color="#56ab91"
        ))
    st.plotly_chart(fig)