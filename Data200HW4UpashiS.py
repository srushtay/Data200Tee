import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Title
st.title("Labratory 4")
st.write('Name: Srushtee Rajendra Upashi')
st.write('Student ID: 016769844')
# getting path of directory
path = os.path.dirname(__file__)
# dataset path
dataset_path = path + '/mountain_flowers.csv'
# reading the dataset
mountain_flowers = pd.read_csv(dataset_path)

categories = mountain_flowers['name']
values = mountain_flowers['petal_length']

# Create a bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')

# Rotate x-axis labels if they are long
plt.xticks(rotation=45, ha='right')

st.pyplot(plt)

st.write(mountain_flowers[['name', 'petal_length']].rename(columns={'name': 'categories'}))