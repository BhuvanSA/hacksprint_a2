import streamlit as st


def render_main_content():
    disclaimer_text = "Disclaimer: Dr. AI GURU provides general health info. For personalized advice, consult a healthcare professional. Always visit a doctor for proper medication."

    col1, col2, col3 = st.columns([1, 1, 10])

    with col3:
        st.markdown(
            f'<h1 class="marquee">{disclaimer_text}</h1>', unsafe_allow_html=True
        )

    col2_1, col2_2, col2_3 = st.columns(3)

    age_group = col2_1.selectbox(
        "Age Group",
        ["0-10", "11-18", "19-30", "31-45", "46-60", "60+"],
        key="age_group_selectbox",
    )

    gender = col2_2.selectbox(
        "Gender", ["Male", "Female", "Other"], key="gender_selectbox"
    )

    previous_medical_record = col2_3.text_area(
        "Previous Medical Record:",
        "",
        key="previous_medical_record_textarea",
        height=100,
    )
