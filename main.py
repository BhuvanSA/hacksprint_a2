# Import necessary libraries
from openai import OpenAI   # Assuming OpenAI library is used, make sure it's installed
import streamlit as st
#hacksprint_a2-Phoenix
# Set the page layout width
st.set_page_config(layout="wide")
st.title("Dr.AI Guru:male-doctor:")

# Define CSS for the page layout
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
            animation: marquee 30s linear infinite;
        }

        @keyframes marquee {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }

        .stTextInput > div {
            width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Main container for layout
with st.container():
    # Sidebar (col1)
    with st.sidebar:
        st.markdown('<h1 style="color: #2C0AE2; font-size: 50px; margin-bottom:0;">Dr.AI GURU</h1>', unsafe_allow_html=True)
        st.markdown('<h4 style="margin-top: 0;">Your Virtual Wellness Companion with Medical AI Chatbot Expertise</h4>', unsafe_allow_html=True)
        disclaimer_text = 'Disclaimer: Dr. AI GURU provides general health info. For personalized advice, consult a healthcare professional. Always visit a doctor for proper medication.'
        #st.markdown(f'<h1 class="marquee">{disclaimer_text}</h1>', unsafe_allow_html=True)
        st.markdown('<h1 style="color: red; font-size: 35px">Description :</h1>', unsafe_allow_html=True)
        st.markdown('<h3>Dr. AI GURU is more than just a chatbot, it\'s your ally in achieving and maintaining optimal wellness. Engage in informative conversations, receive health recommendations, and explore a new era of personalized healthcare guidance</h3>', unsafe_allow_html=True)

    # Main content area (col3)
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 10])

        with col3:
            st.markdown(f'<h1 class="marquee">{disclaimer_text}</h1>', unsafe_allow_html=True)

        st.markdown(
            """
            <style>
                @keyframes marquee {
                    0% { transform: translateX(100%); }
                    100% { transform: translateX(-100%); }
                }

                .marquee {
                    width: 375%;
                    animation: marquee 20s linear infinite;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        col2_1, col2_2, col2_3 = st.columns(3)
        age_group = "Not provided"
        age_group = col2_1.selectbox("Age Group", ["0-10", "11-18", "19-30", "31-45", "46-60", "60+"], key="age_group_selectbox")

        st.markdown(
            """
            <style>
                div[data-baseweb="select"][data-baseweb="select"] {
                    width: 100px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        gender = "Not provided"
        gender = col2_2.selectbox("Gender", ["Male", "Female", "Other"], key="gender_selectbox")

        st.markdown(
            """
            <style>
                div[data-baseweb="select"][data-baseweb="select"] {
                    width: 200px;
                    margin-left: 0px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        previous_medical_record = "noting"
        previous_medical_record = col2_3.text_area("Previous Medical Record:", "", key="previous_medical_record_textarea", height=100)

        st.markdown(
            """
            <style>
                div[data-baseweb="textarea"][data-baseweb="textarea"] {
                    width: 200px;height:40px;align:center;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

    # OpenAI Chat Application
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if prompt := st.text_input("How Are You Feeling Today?"):
        newPrompt = "PLEASE SAY I DON'T HAVE INFORMATION ABOUT THAT AND DON'T HELP IN ANY WAY FOR NON-MEDICAL PROMPTS" + prompt + f"Do note that I am {gender}, belonging to {age_group} age group. I previously had {previous_medical_record} medical conditions,"  
        st.session_state.messages.append({"role": "user", "content": newPrompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            # OpenAI API call with context
            client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
            for response in client.chat.completions.create(
                model="local-model",
                messages=[{"role": m["role"], "content": m["content"]}
                          for m in st.session_state.messages], stream=True):
                full_response += response.choices[0].delta.content if response.choices[0].delta.content else ""
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
