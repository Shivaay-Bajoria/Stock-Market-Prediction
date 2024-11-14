import yfinance as yf
import streamlit as st
from datetime import date 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from plotly import graph_objs as go
import plotly.express as px

START = "2010-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

data = yf.download("AAPL", START, TODAY)
data.reset_index(inplace=True)

st.title("Exploratory Data Analysis (EDA)")

st.code("data.shape")
st.code(data.shape)

st.code("data.info")
st.code(data.info)

st.code("""fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Stock_Open'))
fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock_Close'))
fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
st.plotly_chart(fig)""")

fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Stock_Open'))
fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock_Close'))
fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
st.plotly_chart(fig)

st.code("""fig = px.histogram(data, x="Volume")
st.plotly_chart(fig)""")
# Here we use a column with categorical data
fig = px.histogram(data, x="Volume")
st.plotly_chart(fig)


st.code("""fig = px.bar(data, x='Date', y='Close')
st.plotly_chart(fig)""")
fig = px.bar(data, x='Date', y='Close')
st.plotly_chart(fig)

st.code(""""fig = px.density_heatmap(data, x='Close', y='Open')
st.plotly_chart(fig)""")
fig = px.density_heatmap(data, x="Close", y="Open")
st.plotly_chart(fig)

st.code("""fig = px.scatter_3d(data, x='Volume', y='Close', z='Date')
st.plotly_chart(fig)""")
fig = px.scatter_3d(data, x='Volume', y='Close', z='Date')
st.plotly_chart(fig)

st.code("""fig = px.box(data, y="Close")
st.plotly_chart(fig)""")
fig = px.box(data, y="Close")
st.plotly_chart(fig)

st.code("""fig = px.scatter_matrix(data, dimensions=["Open", "Close", "Date", "Volume"])
st.plotly_chart(fig)""")
fig = px.scatter_matrix(data, dimensions=["Open", "Close", "Date", "Volume"])
st.plotly_chart(fig)

st.code("""fig = px.violin(data, y="close")
st.plotly_chart(fig)""")
fig = px.violin(data, y="Close")
st.plotly_chart(fig)