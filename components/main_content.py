import streamlit as st


def update_session_state(key):
    def callback():
        st.session_state[key] = st.session_state[f"{key}_widget"]

    return callback


def render_main_content():
    disclaimer_text = "Disclaimer: Dr. AI GURU provides general health information based on your input. For medical advice, diagnosis, or treatment, always consult with a qualified healthcare professional."

    col1, col2, col3 = st.columns([1, 1, 10])

    with col3:
        st.markdown(
            f'<h1 class="marquee">{disclaimer_text}</h1>', unsafe_allow_html=True
        )

    col2_1, col2_2, col2_3 = st.columns(3)

    age_group = col2_1.selectbox(
        "Age Group (required)",
        ["", "0-10", "11-18", "19-30", "31-45", "46-60", "60+"],
        key="age_group_selectbox_widget",
        on_change=update_session_state("age_group_selectbox"),
    )

    gender = col2_2.selectbox(
        "Gender (required)",
        ["", "Male", "Female", "Other"],
        key="gender_selectbox_widget",
        on_change=update_session_state("gender_selectbox"),
    )

    previous_medical_record = col2_3.text_area(
        "Previous Medical Record (required):",
        "",
        key="previous_medical_record_textarea_widget",
        height=100,
        on_change=update_session_state("previous_medical_record_textarea"),
    )

    # Initialize session state if not already set
    if "age_group_selectbox" not in st.session_state:
        st.session_state.age_group_selectbox = age_group
    if "gender_selectbox" not in st.session_state:
        st.session_state.gender_selectbox = gender
    if "previous_medical_record_textarea" not in st.session_state:
        st.session_state.previous_medical_record_textarea = previous_medical_record

    # Add a submit button for user information
    if st.button("Save Personal Information"):
        if all([age_group, gender, previous_medical_record]):
            st.success("Personal information saved successfully!")
        else:
            st.error("Please fill in all required fields.")
