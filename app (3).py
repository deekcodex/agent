
import streamlit as st
import pandas as pd

st.title('Product Data Explorer')

st.write('This app displays information from your products CSV file.')

# Load the CSV data
try:
    df = pd.read_csv('products-10000.csv')
    st.success('Successfully loaded products-10000.csv')
    
    st.subheader('First 5 Rows of Data')
    st.dataframe(df.head())

    st.subheader('Basic Data Statistics')
    st.write(df.describe())

    # Example: Display products by category
    st.subheader('Products by Category')
    category_counts = df['Category'].value_counts().reset_index()
    category_counts.columns = ['Category', 'Count']
    st.bar_chart(category_counts.set_index('Category'))

    # You can add more interactive elements here
    # For example, a selectbox to view products of a specific category
    selected_category = st.selectbox('Select a category to view products:', df['Category'].unique())
    st.dataframe(df[df['Category'] == selected_category])


except FileNotFoundError:
    st.error('Error: products-10000.csv not found. Please make sure it\'s in the same directory as app.py.')
except Exception as e:
    st.error(f'An error occurred: {e}')
