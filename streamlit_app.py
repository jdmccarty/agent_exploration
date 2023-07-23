# Import the streamlit library
import streamlit as st

# Title of the web app
st.title('My first Streamlit app')

# Ask the user for their name
name = st.text_input('What is your name?')

# Display a welcome message
if name:
    st.write(f'Hello, {name}! Welcome to the app!')
else:
    st.write('Please enter your name.')

