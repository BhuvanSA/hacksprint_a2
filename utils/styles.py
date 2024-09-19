import streamlit as st


def set_page_style():
    st.markdown(
        """
        <style>
            body {
                background-color: #f0f2f6;
                margin: 0;
                padding: 0;
            }
            .container {
                display: flex;
                flex-direction: row;
                justify-content: space-between;
                padding: 20px;
            }
            .sidebar {
                background-color: #ccffff;
                padding: 20px;
                border-radius: 10px 0 0 10px;
                margin-right: 20px;
                clip-path: polygon(0 0, 100% 0, 90% 100%, 0% 100%);
            }
            .main-content {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 0 10px 10px 0;
                border: 2px solid #d3d3d3;
            }
            .marquee {
                animation: marquee 20s linear infinite;
            }
            @keyframes marquee {
                0% { transform: translateX(100%); }
                100% { transform: translateX(-100%); }
            }
            .stTextInput > div {
                width: 100% !important;
            }
            div[data-baseweb="select"][data-baseweb="select"] {
                width: 200px;
                margin-left: 0px;
            }
            div[data-baseweb="textarea"][data-baseweb="textarea"] {
                width: 200px;
                height: 40px;
                align: center;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
