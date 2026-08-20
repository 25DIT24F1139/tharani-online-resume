import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Tharani Sekar | Resume",
    page_icon="💻",
    layout="wide"
)

# Header section
photo_col, info_col = st.columns([1, 3])

with photo_col:
    st.image("profile.jpg", width=230)

with info_col:
    st.title("THARANI SEKAR")
    st.subheader("IT NETWORKING STUDENT")

    st.write(
        "I am a Semester 5 Diploma in Information Technology student "
        "with a strong interest in computer networking, cybersecurity "
        "and modern technologies. I enjoy learning new technical skills, "
        "solving problems and gaining practical experience in the IT field."
    )

    st.write("📞 **Phone:** 012-853 2854")
    st.write("📧 **Email:** tharanist06@gmail.com")
    st.write("📍 **Location:** Johor, Malaysia")

st.divider()

# Quick information
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Semester", "Semester 5")

with col2:
    st.metric("Programme", "Diploma IT")

with col3:
    st.metric("Specialization", "Networking")
