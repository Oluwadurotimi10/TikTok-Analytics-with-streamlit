#importing streamlit
import streamlit as st
import pandas as pd

#importng plotly for visualization
import plotly.express as px

#using subprocess to run main.py script from command line
from subprocess import call

#setting page width to wide
st.set_page_config(layout='wide')

#creating input
hashtag = st.text_input('Search for a hashtag here', value = "")

#create sidebar
st.sidebar.markdown("<div> <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdXGyYtPASMPvHBvQ2cBEd19ZFDRT1oLjs0A&usqp=CAU' width=100 /> <hi style='display:inline-block'> Tiktok Analytics </h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("Trending tiktoks can be analyzed on this dashboard with the help of python and streamlit")
st.sidebar.markdown("To begin; <ol> <li> Enter the <b> hashtag </b> of the tiktok you wish to analyze </li> <li> Hit the <b> get data </b> button </li> <li> Get your <b> results </b> </li> </ol>", unsafe_allow_html=True)

#creating button
if st.button('Get data'):
    #function to get data
    st.write(hashtag)
    call(['python', 'start.py', hashtag])

    #loading existing data
    data = pd.read_csv('tiktok_data.csv')

    #plotly visualizations 
    fig = px.histogram(data, x ='desc', hover_data=['desc'], y='stats_diggCount', height = 300)
    st.plotly_chart(fig, use_container_width=True)

    #split columns
    left_col, right_col = st.columns(2)

    #video stats
    scatter1  = px.scatter(data, x='stats_shareCount', y='stats_commentCount', hover_data=['desc'], size='stats_playCount', color='stats_playCount')
    left_col.plotly_chart(scatter1, use_container_width=True )

    scatter2  = px.scatter(data, x='authorStats_videoCount', y='authorStats_heartCount', hover_data=['author_nickname'], size='authorStats_followerCount', color='authorStats_followerCount')
    left_col.plotly_chart(scatter2, use_container_width=True )

    #showing tabular data on streamlit
    data