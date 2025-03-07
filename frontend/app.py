import streamlit as st


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
                st.success(f'Welcome back, {username}!')
            else:
                st.error('Please fill in both fields.')

    with st.expander('Don\'t have an account? Sign Up'):
        name = st.text_input('Your username')
        email = st.text_input('Your email address')
        password = st.text_input('Create a password', type='password')
        submit_button = st.button('Register', type='primary', use_container_width=True)
        if submit_button:
            if username and password:
                st.success(f'User registered successfully! Welcome, {username}!')
            else:
                st.error('Please fill in both fields.')

    with st.container(): 
        st.caption('© 2025 JUL.ia. All rights reserved. Created by Team JUL.ia.')

with st.container():
    st.image('assets\JUL.svg', use_container_width=True)
    st.subheader('Welcome to JUL.i!', anchor=False)

    # with st.expander('About JUL.ia'):
    st.caption('JUL.i is a smart and intuitive web app designed for expense management. With an easy-to-use interface and data visualization tools, JUL.i empowers users to take control of their finances efficiently and make informed financial decisions.')