import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.markdown(
            '<h1 style="color: #2C0AE2; font-size: 50px; margin-bottom:0;">Dr.AI GURU</h1>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<h4 style="margin-top: 0;">Your Virtual Wellness Companion with Medical AI Chatbot Expertise</h4>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<h1 style="color: red; font-size: 35px">Description :</h1>',
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h3>Dr. AI GURU is more than just a chatbot, it's your ally in achieving and maintaining optimal wellness. Engage in informative conversations, receive health recommendations, and explore a new era of personalized healthcare guidance</h3>",
            unsafe_allow_html=True,
        )