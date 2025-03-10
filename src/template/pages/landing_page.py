from dotenv import load_dotenv
from http import HTTPStatus
import os
import requests
import streamlit as st

load_dotenv()

API_URL=os.getenv('API_URL')

def landing_page():
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
                        st.session_state.isLoggedIn = True
                        st.session_state.userLogged = username
                        st.rerun()
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
                        st.success(f'Welcome to JUL.i, {st.session_state.userLogged}!')
                    else:
                        st.error('An error occurred. Please try again.')

        with st.container(): 
            st.caption('© 2025 JUL.i. All rights reserved. Created by Team JUL.i.')

    # -- Main section
    with st.container():
        st.image('assets\JUL.svg', use_container_width=True)
        """**Welcome to JUL.i!**"""

        with st.expander('About JUL.i', expanded=True):
            st.caption('JUL.i is a smart and intuitive web app designed for expense management. With an easy-to-use interface and data visualization tools, JUL.i empowers users to take control of their finances efficiently and make informed financial decisions.')
            
    st.video('assets\TEMPLATE_demonstration.mp4', loop=True, autoplay=True, muted=True)