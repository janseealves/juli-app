import streamlit as st
from pages.landing_page import landing_page
from pages.services_page import services_page

st.set_page_config(page_title='JUL.i',layout='wide')

if 'isLoggedIn' not in st.session_state:
    st.session_state.isLoggedIn = False

if 'userLogged' not in st.session_state:
    st.session_state.userLogged = None

if st.session_state.isLoggedIn:
    services_page()
else:
    landing_page()
