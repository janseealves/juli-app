import streamlit as st

st.set_page_config(page_title='JUL.i', layout='wide')

if 'isLoggedIn' and 'userLogged' not in st.session_state:
    st.session_state.isLoggedIn = True
    st.session_state.userLogged = 'John Doe'

# -- Sidebar
with st.sidebar:
    st.logo('assets\JUL_logo.svg', size='large')
    st.image('assets\JULi.svg', use_container_width=True)
    
    st.write(f"Logged in as: {st.session_state.userLogged}")
    
    # Logout button
    if st.button("Logout", use_container_width=True):
        st.session_state.isLoggedIn = False
        st.session_state.userLogged = None
        st.rerun()
    
    with st.container(): 
        st.caption('© 2025 JUL.i. All rights reserved. Created by Team JUL.i.')

# -- Main
with st.container():
    st.image('assets\JUL.svg', use_container_width=True)
    dashboard_tab, wallets_tab, account_tab, settings_tab = st.tabs(['Dashboard', 'Wallets', '# Account', '⚙️'])

    with dashboard_tab:
        st.write('Dashboard content here')  
    
    with wallets_tab:
        st.write('Wallets content here')

    with account_tab:
        st.write('Account content here')

