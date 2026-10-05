import streamlit as st

def footer_home():
    logo_url = "https://i.ibb.co/chCv6YLH/aditya-kumar-logo.png"

    st.markdown(
        f"""
        <div style="
            margin-top: 2rem;
            display:flex;
            gap:6px;
            justify-content:center;
            align-items:center;
        ">
            <p style="font-weight:bold; color:black; margin:0;">
                Created with ❤️ by
            </p>
            <img src="{logo_url}" style="max-height:25px;">
        </div>
        """,
        unsafe_allow_html=True
    )