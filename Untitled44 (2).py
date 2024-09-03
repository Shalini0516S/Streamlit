#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = {
    'Product': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Severity': [5, 4, 2, 3, 1, 4, 3, 5, 3, 4],
    'Probability': [0.9, 0.6, 0.7, 0.5, 0.8, 0.7, 0.1, 0.5, 0.3, 0.5],
    'Score': [4.5, 2.4, 1.4, 1.5, 0.8, 2.8, 0.3, 2.5, 0.9, 2]
}

df = pd.DataFrame(data)

# Streamlit App
st.title("Interactive Visualizations")

# Pie Chart: Score distribution by Product
st.header("Pie Chart: Severity Distribution by Product")
fig_pie = px.pie(df, names='Product', values='Severity', title='Score Distribution by Product')
st.plotly_chart(fig_pie)

# Bar Plot: Severity by Product
st.header("Bar Plot: Severity by Product")
fig_bar = px.bar(df, x='Product', y='Severity', title='Severity by Product', color='Severity')
st.plotly_chart(fig_bar)

# Heatmap: Severity vs Probability
st.header("Heatmap: Severity vs Probability")
heatmap_data = df.pivot_table(index='Product', columns='Severity', values='Product', aggfunc='mean')
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu')
st.pyplot(plt.gcf())

# Bubble Chart: Probability vs Severity with Score as size
st.header("Bubble Chart: Probability vs Severity with Score as Size")
fig_bubble = px.scatter(df, x='Severity', y='Probability', size='Score', color='Product', 
                        title='Bubble Chart: Probability vs Severity')
st.plotly_chart(fig_bubble)

# Slider to filter data by Severity
st.header("Filter Data by Severity")
severity_filter = st.slider("Select the minimum Severity", 1, 5, 1)
filtered_data = df[df['Severity'] >= severity_filter]

# Display filtered data
st.write("Filtered Data", filtered_data)

# Histogram: Score Distribution
st.header("Histogram: Score Distribution")
fig_hist = px.histogram(df, x='Severity', title='Histogram of Severity')
st.plotly_chart(fig_hist)

# Line Plot: Probability over Products
st.header("Line Plot: Probability over Products")
fig_line = px.line(df, x='Product', y='Probability', title='Probability over Products', markers=True)
st.plotly_chart(fig_line)

