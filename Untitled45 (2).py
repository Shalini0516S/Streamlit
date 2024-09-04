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

# Custom color scale function
def get_color(severity):
    if severity >= 4:
        return 'red'
    elif severity == 3:
        return 'yellow'
    else:
        return 'green'

df['Color'] = df['Severity'].apply(get_color)

# Streamlit App
st.title("Interactive Visualizations")

# Pie Chart: Severity distribution by Product
st.header("Pie Chart: Severity Distribution by Product")
fig_pie = px.pie(df, names='Product', values='Severity', title='Severity Distribution by Product',
                 color='Severity',
                 color_discrete_map={
                     5: 'red',
                     4: 'orange',
                     3: 'yellow',
                     2: 'lightgreen',
                     1: 'green'
                 })
st.plotly_chart(fig_pie)

# Bar Plot: Severity by Product
st.header("Bar Plot: Severity by Product")
fig_bar = px.bar(df, x='Product', y='Severity', title='Severity by Product', color='Severity',
                 color_continuous_scale=['green', 'yellow', 'red'])
st.plotly_chart(fig_bar)

# Heatmap: Severity vs Probability
st.header("Heatmap: Severity vs Probability")
heatmap_data = df.pivot_table(index='Product', columns='Severity', values='Probability', aggfunc='mean')
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, cmap='RdYlGn', cbar_kws={'label': 'Probability'})
st.pyplot(plt.gcf())

# Bubble Chart: Probability vs Severity with Score as size
st.header("Bubble Chart: Probability vs Severity with Score as Size")
fig_bubble = px.scatter(df, x='Severity', y='Probability', size='Score', color='Severity',
                        title='Bubble Chart: Probability vs Severity',
                        color_continuous_scale=['green', 'yellow', 'red'],
                        text='Product')  # Add product names inside bubbles
fig_bubble.update_traces(textposition='top center')
st.plotly_chart(fig_bubble)

# Slider to filter data by Severity
st.header("Filter Data by Severity")
severity_filter = st.slider("Select the minimum Severity", 1, 5, 1)
filtered_data = df[df['Severity'] >= severity_filter]

# Display filtered data
st.write("Filtered Data", filtered_data)

# Histogram: Severity Distribution
st.header("Histogram: Severity Distribution")
df['Severity Level'] = df['Severity'].apply(lambda x: 'High' if x >= 4 else ('Medium' if x == 3 else 'Low'))
fig_hist = px.histogram(df, x='Severity', title='Histogram of Severity', color='Severity Level',
                        color_discrete_map={'High': 'red', 'Medium': 'yellow', 'Low': 'green'},
                        text_auto=True)  # Add product names on bars
st.plotly_chart(fig_hist)

# Line Plot: Probability over Products
st.header("Line Plot: Probability over Products")

# Creating the line plot with a specific color and increased line width
fig_line = px.line(
    df,
    x='Product',
    y='Probability',
    title='Probability over Products',
    markers=True,
    line_shape='linear'
)

# Updating line properties for visibility
fig_line.update_traces(
    line=dict(color='blue', width=4),  # Set line color and increase line width
    marker=dict(size=10, color='red')  # Customize marker size and color
)

# Show the plot
st.plotly_chart(fig_line)

