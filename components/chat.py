import streamlit as st
from mistralai import Mistral


def render_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if prompt := st.text_input("How Are You Feeling Today?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            client = Mistral(api_key=st.secrets["MISTRAL_API_KEY"])
            if client:
                try:
                    chat_response = client.chat.complete(
                        model="mistral-large-latest",
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                        stream=False,
                    )
                    if chat_response and chat_response.choices:
                        full_response = chat_response.choices[0].message.content
                        message_placeholder.markdown(full_response)
                    else:
                        st.error("No response received from the API.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
