import pandas as pd
import streamlit as st
import plotly.express as px
data=pd.read_csv("IRIS.csv")
st.set_page_config(layout='wide')
st.write(data.head(10))
st.write("Unique Values",data["species"].unique())
figure=st.plotly_chart(px.scatter(data,x='sepal_width',y='sepal_length',color='species'))
