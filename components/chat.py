import streamlit as st
from mistralai import Mistral


def render_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "input_key" not in st.session_state:
        st.session_state.input_key = 0

    age_group = st.session_state.get("age_group_selectbox", None)
    gender = st.session_state.get("gender_selectbox", None)
    medical_record = st.session_state.get("previous_medical_record_textarea", None)

    if not all([age_group, gender, medical_record]):
        st.warning(
            "Please fill in your age group, gender, and previous medical record before chatting."
        )
        return

    system_message = f"""You are Dr. AI Guru, a medical AI assistant. Your role is to provide general health information and advice based on the user's input. 
    Always consider the user's age group ({age_group}), gender ({gender}), and previous medical record: {medical_record}.
    Only respond to medical-related questions. If asked about non-medical topics, politely explain that you can only assist with health-related inquiries.
    Remember, you're providing general advice. Always recommend consulting a healthcare professional for personalized medical advice or treatment."""

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.text_input(
        "Hello, How can I help you?", key=f"user_input_{st.session_state.input_key}"
    )

    if prompt:
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
                            {"role": "system", "content": system_message},
                            *[
                                {"role": m["role"], "content": m["content"]}
                                for m in st.session_state.messages
                            ],
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
        # Increment the input key to clear the input field
        st.session_state.input_key += 1
        st.rerun()  # Rerun the app to update the chat history and clear the input
