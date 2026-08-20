import streamlit as st
import pandas as pd

# -------------------------------------------------
# PAGE SETTING
# -------------------------------------------------
st.set_page_config(
    page_title="Tharani Sekar Resume",
    page_icon="📄",
    layout="wide"
)

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "visitor_count" not in st.session_state:
    st.session_state.visitor_count = 0


# -------------------------------------------------
# CUSTOM DESIGN
# -------------------------------------------------
st.markdown("""
<style>

.block-container {
    max-width: 1000px;
    padding-top: 25px;
    padding-bottom: 40px;
}

h1 {
    font-size: 42px !important;
    margin-bottom: 0px;
}

h2 {
    font-size: 22px !important;
}

h3 {
    color: #243B53;
}

.resume-title {
    font-size: 18px;
    letter-spacing: 2px;
    color: #526777;
    margin-top: -10px;
}

.section-title {
    background-color: #243B53;
    color: white;
    padding: 7px 12px;
    font-weight: bold;
    margin-top: 15px;
    margin-bottom: 10px;
}

.contact-text {
    font-size: 15px;
    line-height: 1.8;
}

.small-text {
    font-size: 15px;
    line-height: 1.7;
}

div[data-testid="stMetric"] {
    border: 1px solid #DDDDDD;
    padding: 10px;
    border-radius: 5px;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# RESUME HEADER
# -------------------------------------------------
photo_col, name_col = st.columns([1, 2.7])

with photo_col:
    st.image("profile.jpg", width=210)

with name_col:
    st.markdown("# THARANI SEKAR")

    st.markdown(
        '<div class="resume-title">IT NETWORKING STUDENT</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown("""
    <div class="contact-text">
    📞 012-853 2854<br>
    📧 tharanist06@gmail.com<br>
    📍 Johor, Malaysia
    </div>
    """, unsafe_allow_html=True)

st.divider()


# -------------------------------------------------
# MAIN RESUME TWO COLUMN DESIGN
# -------------------------------------------------
left, right = st.columns([1, 1.8], gap="large")


# =================================================
# LEFT SIDE
# =================================================
with left:

    st.markdown(
        '<div class="section-title">ABOUT ME</div>',
        unsafe_allow_html=True
    )

    st.write(
        "I am a Semester 5 Diploma in Information Technology student "
        "with a strong interest in computer networking, cybersecurity "
        "and modern technologies. I enjoy learning new technical skills, "
        "solving problems and gaining practical experience in the IT field."
    )


    st.markdown(
        '<div class="section-title">LANGUAGES</div>',
        unsafe_allow_html=True
    )

    st.write("• Bahasa Melayu")
    st.write("• English")
    st.write("• Tamil")


    st.markdown(
        '<div class="section-title">TECHNICAL SKILLS</div>',
        unsafe_allow_html=True
    )

    st.write("• Cisco Packet Tracer")
    st.write("• VLAN Configuration")
    st.write("• Inter-VLAN Routing")
    st.write("• OSPF")
    st.write("• GRE Tunnel")
    st.write("• HSRP")
    st.write("• EtherChannel")
    st.write("• Python Programming")
    st.write("• Windows Server")
    st.write("• Linux")
    st.write("• Cybersecurity")
    st.write("• ESP32 / IoT")


    st.markdown(
        '<div class="section-title">SOFT SKILLS</div>',
        unsafe_allow_html=True
    )

    st.write("• Teamwork")
    st.write("• Communication")
    st.write("• Problem Solving")
    st.write("• Time Management")
    st.write("• Responsible")
    st.write("• Willing to Learn")


# =================================================
# RIGHT SIDE
# =================================================
with right:

    st.markdown(
        '<div class="section-title">EDUCATION</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Diploma in Information Technology")
    st.write("**Politeknik Malaysia**")
    st.write("Semester 5")
    st.write("Specialization: Networking")

    st.write("")

    st.write(
        "Current study areas include Computer Networking, "
        "Switching and Routing, Cybersecurity, Python Programming, "
        "Server Administration and Internet of Things."
    )


    st.markdown(
        '<div class="section-title">ACADEMIC PROJECTS</div>',
        unsafe_allow_html=True
    )

    st.markdown("#### Networking Configuration Project")

    st.write(
        "Configured and tested VLANs, Inter-VLAN Routing, OSPF, "
        "GRE Tunnel, HSRP and EtherChannel using Cisco Packet Tracer."
    )

    st.markdown("#### IoT Project")

    st.write(
        "Developed an IoT-based project using ESP32 and sensors "
        "to collect and monitor real-time data."
    )

    st.markdown("#### Cybersecurity Practical")

    st.write(
        "Performed basic network scanning, traffic analysis and "
        "security testing in a controlled laboratory environment."
    )

    st.markdown("#### Python Programming")

    st.write(
        "Developed Python programs using functions, classes, "
        "object-oriented programming and Streamlit."
    )


    st.markdown(
        '<div class="section-title">CAREER OBJECTIVE</div>',
        unsafe_allow_html=True
    )

    st.write(
        "To develop my knowledge and practical skills in networking "
        "and information technology while gaining industry experience "
        "that will prepare me for a professional career in IT."
    )


# -------------------------------------------------
# QUICK RESUME SUMMARY
# -------------------------------------------------
st.divider()

m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Current Semester", "5")

with m2:
    st.metric("Programme", "Diploma IT")

with m3:
    st.metric("Field", "Networking")


# -------------------------------------------------
# STREAMLIT REQUIREMENTS
# -------------------------------------------------
st.divider()

st.subheader("Additional Resume Information")

tab1, tab2, tab3 = st.tabs(
    ["Education Details", "Skills Details", "Contact"]
)


# -------------------------------------------------
# DATAFRAME
# -------------------------------------------------
with tab1:

    education_data = {
        "Programme": [
            "Diploma in Information Technology"
        ],
        "Semester": [
            "Semester 5"
        ],
        "Specialization": [
            "Networking"
        ],
        "Institution": [
            "Politeknik Malaysia"
        ]
    }

    education_df = pd.DataFrame(education_data)

    st.dataframe(
        education_df,
        use_container_width=True,
        hide_index=True
    )


# -------------------------------------------------
# DATA EDITOR
# -------------------------------------------------
with tab2:

    skills_data = {
        "Technical Skill": [
            "Cisco Networking",
            "Python Programming",
            "Windows Server",
            "Cybersecurity",
            "ESP32 / IoT"
        ],

        "Level": [
            "Intermediate",
            "Intermediate",
            "Intermediate",
            "Basic",
            "Intermediate"
        ]
    }

    skills_df = pd.DataFrame(skills_data)

    st.data_editor(
        skills_df,
        use_container_width=True,
        hide_index=True
    )


# -------------------------------------------------
# POPOVER
# -------------------------------------------------
with tab3:

    st.write("You can contact me using the information below.")

    with st.popover("View Contact Information"):

        st.write("**THARANI SEKAR**")
        st.write("IT Networking Student")
        st.write("📞 012-853 2854")
        st.write("📧 tharanist06@gmail.com")
        st.write("📍 Johor, Malaysia")


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.image("profile.jpg", width=140)

st.sidebar.title("THARANI SEKAR")

st.sidebar.write("IT Networking Student")

st.sidebar.divider()

st.sidebar.write("📞 012-853 2854")
st.sidebar.write("📧 tharanist06@gmail.com")
st.sidebar.write("📍 Johor, Malaysia")

st.sidebar.divider()

st.sidebar.subheader("Resume Navigation")

resume_section = st.sidebar.selectbox(
    "View:",
    [
        "Full Resume",
        "Education",
        "Skills",
        "Projects"
    ]
)


# -------------------------------------------------
# INTERACTIVE SECTION - 7 USER EVENTS
# -------------------------------------------------
st.divider()

with st.expander("Interactive Resume Section"):

    st.caption(
        "This section demonstrates Streamlit user interaction elements."
    )

    # EVENT 1
    visitor_name = st.text_input(
        "Enter your name"
    )

    # EVENT 2
    area_interest = st.selectbox(
        "Area of interest",
        [
            "Networking",
            "Cybersecurity",
            "Programming",
            "Internet of Things"
        ]
    )

    # EVENT 3
    rating = st.slider(
        "Rate this resume",
        1,
        10,
        5
    )

    # EVENT 4
    contact_interest = st.checkbox(
        "Interested to contact me"
    )

    # EVENT 5
    contact_method = st.radio(
        "Preferred contact method",
        [
            "Email",
            "Phone"
        ]
    )

    # EVENT 6
    show_objective = st.toggle(
        "Show career objective"
    )

    if show_objective:
        st.info(
            "My goal is to develop my networking and IT skills "
            "and gain practical industry experience."
        )

    # EVENT 7
    if st.button("Submit"):

        st.session_state.visitor_count += 1

        if visitor_name:

            st.success(
                f"Thank you, {visitor_name}, for viewing my resume."
            )

        else:

            st.success(
                "Thank you for viewing my resume."
            )

    st.caption(
        f"Total interactions: {st.session_state.visitor_count}"
    )


# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.divider()

st.caption(
    "THARANI SEKAR | IT NETWORKING STUDENT | ONLINE RESUME"
)
