from dotenv import load_dotenv
import os
import requests
import streamlit as st
from http import HTTPStatus

load_dotenv()

API_URL=os.getenv('API_URL')

# -- Sidebar
with st.sidebar:
    st.logo('assets\JUL_logo.svg', size='large')
    st.image('assets\JULi.svg', use_container_width=True)

    with st.expander('Already a user? Log In'):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        submit_button = st.button('Log In', type='primary', use_container_width=True)
        if submit_button:
            if username and password:
                response = requests.post(
                    f'{API_URL}/auth',
                    data={'username': username, 'password': password}
                )
                if response.status_code == HTTPStatus.ACCEPTED:
                    st.success(f'Welcome back, {username}!')
                else:
                    st.error('Invalid credentials. Please try again.')

    with st.expander('Don\'t have an account? Sign Up'):
        username = st.text_input('Your username')
        email = st.text_input('Your email address')
        password = st.text_input('Create a password', type='password')
        submit_button = st.button('Register', type='primary', use_container_width=True)
        if submit_button:
            if username and email and password:
                response = requests.post(
                    f'{API_URL}/users',
                    json={'username': username, 'email': email, 'password': password}
                )
                if response.status_code == HTTPStatus.CREATED:
                    st.success(f'Welcome to JUL.i, {username}!')
                else:
                    st.error('An error occurred. Please try again.')

    with st.container(): 
        st.caption('© 2025 JUL.i All rights reserved. Created by Team JUL.ia.')

with st.container():
    st.image('assets\JUL.svg', use_container_width=True)
    st.subheader('Welcome to JUL.i!', anchor=False)

    # with st.expander('About JUL.ia'):
    st.caption('JUL.i is a smart and intuitive web app designed for expense management. With an easy-to-use interface and data visualization tools, JUL.i empowers users to take control of their finances efficiently and make informed financial decisions.')
