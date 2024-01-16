#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import pandas as pd


# In[26]:


# app.py

import streamlit as st

def main():
    st.title("My Dashboard")

    # Your content goes here

if __name__ == "__main__":
    main()


# In[27]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\googleplaystore.csv')


# In[63]:


import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\googleplaystore.csv")

# Function to remove duplicates based on 'Category' and keep the row with the highest installs in each category
def get_highest_installs_df(data):
    data['Installs'] = data['Installs'].replace('Free', '0').str.replace(',', '').str.replace('+', '')
    data['Installs'] = pd.to_numeric(data['Installs'], errors='coerce')  # Handle 'Free' values
    highest_installs_df = data.loc[data.groupby('Category')['Installs'].idxmax()]
    return highest_installs_df

# Function to create bar chart of average ratings
def average_ratings_chart():
    selected_category = st.sidebar.selectbox("Select a Category", df['Category'].unique())
    filtered_data = df[df['Category'] == selected_category]
    average_ratings = filtered_data.groupby('Category')['Rating'].mean().reset_index()
    fig = px.bar(average_ratings, x='Category', y='Rating', title=f'Average Ratings for {selected_category}')
    st.plotly_chart(fig)

# Function to create scatter plot of Reviews vs. Ratings
def reviews_ratings_scatter():
    selected_category = st.sidebar.selectbox('Select Category', df['Category'].unique())
    filtered_data = df[df['Category'] == selected_category]
    fig = px.scatter(filtered_data, x='Rating', y='Reviews', title=f'Reviews vs. Ratings for {selected_category}',
                     labels={'Rating': 'Ratings', 'Reviews': 'Reviews'})
    st.plotly_chart(fig)

# Function to create histogram of Distribution of App Sizes
def app_sizes_histogram():
    selected_category = st.sidebar.selectbox('Select Category', df['Category'].unique())
    filtered_data = df[df['Category'] == selected_category]
    fig = px.histogram(filtered_data, x='Size', title=f'Distribution of App Sizes for {selected_category}',
                       labels={'Size': 'App Size', 'count': 'Frequency'})
    st.plotly_chart(fig)

# Function to create box plot of Distribution of Ratings
def ratings_box_plot():
    selected_category = st.sidebar.selectbox('Select Category', df['Category'].unique())
    filtered_data = df[df['Category'] == selected_category]
    fig = px.box(filtered_data, y='Rating', title=f'Distribution of Ratings for {selected_category}',
                 labels={'Rating': 'Ratings'})
    st.plotly_chart(fig)

# Function to create bar chart of App with Highest Installs in Each Category
def highest_installs_bar_chart():
    highest_installs_df = get_highest_installs_df(df)
    fig, ax = plt.subplots()
    ax.bar(highest_installs_df['Category'], highest_installs_df['Installs'])
    ax.set(xlabel='Category', ylabel='Installs', title='App with Highest Installs in Each Category')
    st.pyplot(fig)

# Function to create bubble chart of Installs vs Price for Paid Apps
def installs_vs_price_bubble_chart():
    paid_apps = df[df['Type'] == 'Paid']
    paid_apps['Installs'] = paid_apps['Installs'].replace('Free', '0').str.replace(',', '').str.replace('+', '').astype(float)
    paid_apps['Price'] = paid_apps['Price'].str.replace('$', '').astype(float)
    paid_apps = paid_apps.dropna(subset=['Rating'])
    selected_category = st.sidebar.selectbox('Select Category', paid_apps['Category'].unique())
    filtered_data = paid_apps[paid_apps['Category'] == selected_category]
    fig = px.scatter(filtered_data, x='Price', y='Installs', size='Rating',
                     title='Installs vs Price for Paid Apps',
                     labels={'Price': 'Price', 'Installs': 'Installs'})
    st.plotly_chart(fig)

# Sidebar for selecting the chart
selected_chart = st.sidebar.selectbox('Select Chart', ['Average Ratings', 'Reviews vs Ratings',
                                                      'Distribution of App Sizes', 'Distribution of Ratings',
                                                      'Highest Installs in Each Category', 'Installs vs Price for Paid Apps'])

# Display the selected chart
if selected_chart == 'Average Ratings':
    average_ratings_chart()
elif selected_chart == 'Reviews vs Ratings':
    reviews_ratings_scatter()
elif selected_chart == 'Distribution of App Sizes':
    app_sizes_histogram()
elif selected_chart == 'Distribution of Ratings':
    ratings_box_plot()
elif selected_chart == 'Highest Installs in Each Category':
    highest_installs_bar_chart()
elif selected_chart == 'Installs vs Price for Paid Apps':
    installs_vs_price_bubble_chart()


# In[ ]:




