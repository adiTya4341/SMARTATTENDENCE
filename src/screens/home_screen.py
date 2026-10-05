import streamlit as st
from src.component.header import header_home
from src.component.footer import footer_home
from src.ui.base_layout import style_base_layout,style_background_home

def home_screen():
    st.header("Home Screen")

    header_home()
    style_background_home()
    style_base_layout()

    col1,col2 =st.columns(2)

    with col1:
        st.markdown(
    "<div style='color: black; font-size: 28px; font-weight: 700; white-space: nowrap;'>I am Teacher</div>",
    unsafe_allow_html=True
)
        st.image("https://i.ibb.co/CsmQQV6X/mascot-proof.png",width=150)
        
        if st.button('Teacher Portal ->',type='primary'):
           st.session_state['login_type']='teacher'
           st.rerun()

    with col2:
        st.markdown(
    "<div style='color: black; font-size: 28px; font-weight: 700; white-space: nowrap;'>I am Student</div>",
    unsafe_allow_html=True
)
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png",width=119)
        if  st.button('Student Portal ->',type='primary'):
            st.session_state['login_type']='student'
            st.rerun()
    footer_home()
    