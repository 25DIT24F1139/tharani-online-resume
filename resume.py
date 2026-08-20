import streamlit as st
import pandas as pd

# -------------------------------------------------
# PAGE CONFIG
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
# CUSTOM CSS
# -------------------------------------------------
st.markdown("""
<style>

html, body, [data-testid="stAppViewContainer"] {
    background-color: #f2f2f2;
}

.block-container {
    max-width: 1050px;
    padding-top: 25px;
    padding-bottom: 40px;
}

.resume-card {
    background: white;
    padding: 35px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    color: #222222;
}

.resume-card h1,
.resume-card h2,
.resume-card h3,
.resume-card h4,
.resume-card p,
.resume-card li {
    color: #222222;
}

.name-title {
    font-size: 40px;
    font-weight: 800;
    color: #1f3b57;
    margin-bottom: 2px;
}

.job-title {
    font-size: 18px;
    letter-spacing: 2px;
    color: #60758a;
    margin-bottom: 15px;
}

.contact-line {
    font-size: 15px;
    line-height: 1.8;
}

.section-heading {
    background-color: #1f3b57;
    color: white !important;
    padding: 7px 10px;
    font-weight: 700;
    margin-top: 12px;
    margin-bottom: 8px;
    font-size: 16px;
}

.small-text {
    font-size: 14px;
    line-height: 1.55;
}

.skill-list {
    font-size: 14px;
    line-height: 1.6;
}

hr {
    margin-top: 10px;
    margin-bottom: 10px;
}

div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #dddddd;
    padding: 10px;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# MAIN RESUME
# -------------------------------------------------
st.markdown('<div class="resume-card">', unsafe_allow_html=True)

# HEADER
photo_col, info_col = st.columns([1, 2.7], gap="large")

with photo_col:
    st.image("profile.jpg", width=180)

with info_col:
    st.markdown(
        '<div class="name-title">THARANI SEKAR</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="job-title">IT NETWORKING STUDENT</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="contact-line">
    📞 012-853 2854<br>
    📧 tharanist06@gmail.com<br>
    📍 Johor, Malaysia
    </div>
    """, unsafe_allow_html=True)

st.divider()

# TWO COLUMN CV
left_col, right_col = st.columns([1, 1.8], gap="large")

# -------------------------------------------------
# LEFT COLUMN
# -------------------------------------------------
with left_col:

    st.markdown(
        '<div class="section-heading">ABOUT ME</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="small-text">
    I am a Semester 5 Diploma in Information Technology student with
    a strong interest in computer networking, cybersecurity and modern
    technologies. I enjoy learning new technical skills, solving problems
    and gaining practical experience in the IT field.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">LANGUAGES</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="skill-list">
    • Bahasa Melayu<br>
    • English<br>
    • Tamil
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">TECHNICAL SKILLS</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="skill-list">
    • Cisco Packet Tracer<br>
    • VLAN Configuration<br>
    • Inter-VLAN Routing<br>
    • OSPF<br>
    • GRE Tunnel<br>
    • HSRP<br>
    • EtherChannel<br>
    • Python Programming<br>
    • Windows Server<br>
    • Linux<br>
    • Cybersecurity<br>
    • ESP32 / IoT
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">SOFT SKILLS</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="skill-list">
    • Teamwork<br>
    • Communication<br>
    • Problem Solving<br>
    • Time Management<br>
    • Responsibility<br>
    • Willingness to Learn
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# RIGHT COLUMN
# -------------------------------------------------
with right_col:

    st.markdown(
        '<div class="section-heading">EDUCATION</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Diploma in Information Technology")
    st.write("**Politeknik Malaysia**")
    st.write("Semester 5")
    st.write("Specialization: Networking")

    st.markdown("""
    <div class="small-text">
    Current study areas include Computer Networking, Switching and Routing,
    Cybersecurity, Python Programming, Server Administration and
    Internet of Things.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">ACADEMIC PROJECTS</div>',
        unsafe_allow_html=True
    )

    st.markdown("#### Networking Configuration Project")
    st.markdown("""
    <div class="small-text">
    Configured and tested VLANs, Inter-VLAN Routing, OSPF, GRE Tunnel,
    HSRP and EtherChannel using Cisco Packet Tracer.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### IoT Project")
    st.markdown("""
    <div class="small-text">
    Developed an IoT-based project using ESP32 and sensors to collect
    and monitor real-time data.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Cybersecurity Practical")
    st.markdown("""
    <div class="small-text">
    Performed basic network scanning, traffic analysis and security
    testing in a controlled laboratory environment.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Python Programming")
    st.markdown("""
    <div class="small-text">
    Developed Python programs using functions, classes,
    object-oriented programming and Streamlit.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">CAREER OBJECTIVE</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="small-text">
    To strengthen my knowledge and practical skills in networking and
    information technology while gaining industry experience that will
    prepare me for a professional career in IT.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# STREAMLIT REQUIREMENTS
# -------------------------------------------------
st.divider()
st.header("Resume Information & Interaction")

# METRIC + COLUMNS
m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Current Semester", "5")

with m2:
    st.metric("Programme", "Diploma IT")

with m3:
    st.metric("Field", "Networking")

# TABS
tab1, tab2, tab3 = st.tabs(
    ["Education Details", "Skills Details", "Contact"]
)

# DATAFRAME
with tab1:
    education_data = {
        "Programme": ["Diploma in Information Technology"],
        "Semester": ["Semester 5"],
        "Specialization": ["Networking"],
        "Institution": ["Politeknik Malaysia"]
    }

    education_df = pd.DataFrame(education_data)

    st.dataframe(
        education_df,
        use_container_width=True,
        hide_index=True
    )

# DATA EDITOR
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

# POPOVER
with tab3:
    st.write("Contact information")

    with st.popover("View Contact Details"):
        st.write("**THARANI SEKAR**")
        st.write("IT Networking Student")
        st.write("📞 012-853 2854")
        st.write("📧 tharanist06@gmail.com")
        st.write("📍 Johor, Malaysia")

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.image("profile.jpg", width=130)

st.sidebar.title("THARANI SEKAR")
st.sidebar.write("IT Networking Student")

st.sidebar.divider()

st.sidebar.subheader("Contact")
st.sidebar.write("📞 012-853 2854")
st.sidebar.write("📧 tharanist06@gmail.com")
st.sidebar.write("📍 Johor, Malaysia")

st.sidebar.divider()

st.sidebar.subheader("Languages")
st.sidebar.write("• Bahasa Melayu")
st.sidebar.write("• English")
st.sidebar.write("• Tamil")

# -------------------------------------------------
# 7 USER EVENTS
# -------------------------------------------------
st.divider()

with st.expander("Interactive Resume Section"):

    st.write("Try the interactive elements below.")

    # 1 - TEXT INPUT
    visitor_name = st.text_input("Enter your name")

    # 2 - SELECTBOX
    interest = st.selectbox(
        "Which IT field are you interested in?",
        [
            "Networking",
            "Cybersecurity",
            "Programming",
            "Internet of Things"
        ]
    )

    # 3 - SLIDER
    rating = st.slider(
        "Rate this resume",
        1,
        10,
        5
    )

    # 4 - CHECKBOX
    contact_interest = st.checkbox(
        "I am interested in contacting Tharani"
    )

    # 5 - RADIO
    contact_method = st.radio(
        "Preferred contact method",
        ["Email", "Phone"]
    )

    # 6 - TOGGLE
    show_objective = st.toggle(
        "Show career objective"
    )

    if show_objective:
        st.info(
            "My goal is to improve my networking and IT skills "
            "and gain more practical industry experience."
        )

    # 7 - BUTTON
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

    st.write("Selected interest:", interest)
    st.write("Resume rating:", rating)
    st.write("Preferred contact:", contact_method)

    if contact_interest:
        st.write("✅ Visitor is interested in contacting me.")

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
