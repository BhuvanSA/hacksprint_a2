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
            .left-aligned-disclaimer {
                text-align: left !important;
                font-size: 0.8rem !important;
                font-weight: normal !important;
                width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
            }
            .left-aligned-disclaimer > * {
                text-align: left !important;
                padding: 0 !important;
                margin: 0 !important;
            }
            [data-testid="column"] > div:has(> .left-aligned-disclaimer) {
                display: flex;
                justify-content: flex-start;
                align-items: flex-start;
                width: 100%;
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
            .big-left-aligned-disclaimer {
                text-align: left !important;
                font-size: 1.2rem !important;
                font-weight: normal !important;
                width: 100% !important;
                padding: 10px 0 !important;
                margin: 0 !important;
                color: #333 !important;
            }
            /* Override Streamlit's default centering */
            .stMarkdown {
                display: flex;
                justify-content: flex-start !important;
            }
            .stMarkdown > div {
                width: 100% !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
