import streamlit as st
from components.sidebar import render_sidebar
from components.main_content import render_main_content
from components.chat import render_chat
from utils.styles import set_page_style


def main():
    st.set_page_config(layout="wide")
    st.title("Dr.AI Guru:male-doctor:")

    set_page_style()

    with st.container():
        render_sidebar()
        render_main_content()
        render_chat()


if __name__ == "__main__":
    main()
