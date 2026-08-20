import streamlit as st
import pandas as pd

# PAGE SETTINGS

st.set_page_config( 
    page_title="Tharani Sekar Resume",
    page_icon="💻",
    layout="wide"
)

# SESSION STATE

if "visitor_count" not in st.session_state:
    st.session_state.visitor_count = 0


# HEADER SECTION

photo, info = st.columns([1, 3])

with photo:
    st.image("profile.jpg", width=220)

with info:
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


# QUICK INFORMATION / METRICS

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Semester", "Semester 5")

with col2:
    st.metric("Programme", "Diploma IT")

with col3:
    st.metric("Specialization", "Networking")


# RESUME TABS

st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["About Me", "Education", "Skills", "Projects", "Contact"]
)


# ABOUT ME

with tab1:
    st.header("About Me")

    st.write(
        "I am currently pursuing a Diploma in Information Technology "
        "and I am now in Semester 5. My main interest is computer networking. "
        "I enjoy learning how networks work, configuring network devices, "
        "troubleshooting problems and exploring cybersecurity."
    )

    st.write(
        "I am a responsible and hardworking student who is always willing "
        "to learn new skills and gain more practical experience in the IT field."
    )

    st.subheader("Career Objective")

    st.write(
        "My goal is to improve my networking and information technology skills, "
        "gain practical working experience and prepare myself for a future career "
        "in the IT industry."
    )


# EDUCATION

with tab2:
    st.header("Education")

    education_data = {
        "Programme": ["Diploma in Information Technology"],
        "Semester": ["Semester 5"],
        "Field": ["Information Technology / Networking"],
        "Institution": ["Politeknik Malaysia"]
    }

    education_df = pd.DataFrame(education_data)

    st.dataframe(
        education_df,
        use_container_width=True
    )

    st.subheader("Current Study Areas")

    st.write("• Computer Networking")
    st.write("• Switching and Routing")
    st.write("• Cybersecurity")
    st.write("• Python Programming")
    st.write("• Server Administration")
    st.write("• Internet of Things (IoT)")
    st.write("• Network Security")


# SKILLS
with tab3:
    st.header("Technical Skills")

    skills_data = {
        "Skill": [
            "Cisco Packet Tracer",
            "VLAN Configuration",
            "Inter-VLAN Routing",
            "OSPF",
            "GRE Tunnel",
            "HSRP",
            "EtherChannel",
            "Python Programming",
            "Windows Server",
            "Linux",
            "Cybersecurity",
            "ESP32 / IoT"
        ],

        "Level": [
            "Intermediate",
            "Intermediate",
            "Intermediate",
            "Intermediate",
            "Basic",
            "Basic",
            "Intermediate",
            "Intermediate",
            "Intermediate",
            "Basic",
            "Basic",
            "Intermediate"
        ]
    }

    skills_df = pd.DataFrame(skills_data)

    st.data_editor(
        skills_df,
        use_container_width=True
    )

    st.subheader("Soft Skills")

    st.write("• Teamwork")
    st.write("• Communication")
    st.write("• Problem Solving")
    st.write("• Time Management")
    st.write("• Responsibility")
    st.write("• Willingness to Learn")


# PROJECTS

with tab4:
    st.header("Academic Projects")

    st.subheader("🌐 Networking Configuration Project")

    st.write(
        "Configured and tested different networking technologies using "
        "Cisco Packet Tracer, including VLANs, Inter-VLAN Routing, OSPF, "
        "GRE Tunnel, HSRP and EtherChannel."
    )

    st.subheader("📡 IoT Project")

    st.write(
        "Developed an IoT-based project using ESP32 and sensors "
        "to collect and monitor real-time data."
    )

    st.subheader("🔐 Cybersecurity Practical")

    st.write(
        "Performed basic network scanning, traffic analysis and "
        "security testing in a controlled laboratory environment."
    )

    st.subheader("🐍 Python Programming")

    st.write(
        "Developed Python programs using functions, classes, "
        "object-oriented programming and Streamlit."
    )


# CONTACT TAB
with tab5:
    st.header("Contact")

    st.write("Feel free to contact me for more information.")

    st.write("📞 **Phone:** 012-853 2854")
    st.write("📧 **Email:** tharanist06@gmail.com")
    st.write("📍 **Location:** Johor, Malaysia")

    with st.popover("📩 More Contact Details"):
        st.write("**THARANI SEKAR**")
        st.write("IT Networking Student")
        st.write("📞 012-853 2854")
        st.write("📧 tharanist06@gmail.com")
        st.write("📍 Johor, Malaysia")


# SIDEBAR
st.sidebar.title("My Resume")

st.sidebar.image("profile.jpg", width=150)

st.sidebar.subheader("THARANI SEKAR")
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


# INTERACTIVE SECTION
st.divider()
st.header("Interactive Resume")

st.write("You can interact with my online resume below.")

# User Event 1
visitor_name = st.text_input("Enter your name:")

# User Event 2
interest = st.selectbox(
    "Which IT field are you interested in?",
    [
        "Networking",
        "Cybersecurity",
        "Programming",
        "IoT"
    ]
)

# User Event 3
rating = st.slider(
    "Rate my online resume:",
    1,
    10,
    5
)

# User Event 4
contact_interest = st.checkbox(
    "I am interested in contacting Tharani"
)

# User Event 5
contact_method = st.radio(
    "Preferred contact method:",
    [
        "Email",
        "Phone"
    ]
)

# User Event 6
show_objective = st.toggle(
    "Show career objective"
)

if show_objective:
    st.info(
        "My career objective is to develop my networking and IT skills "
        "and gain practical experience in the technology industry."
    )

# User Event 7
if st.button("Submit"):
    st.session_state.visitor_count += 1

    if visitor_name:
        st.success(
            f"Thank you, {visitor_name}! Your response has been submitted."
        )
    else:
        st.success(
            "Thank you for visiting my online resume!"
        )

# Display interaction information
st.write("**Selected IT Interest:**", interest)
st.write("**Resume Rating:**", rating)
st.write("**Preferred Contact:**", contact_method)

if contact_interest:
    st.write("✅ Visitor is interested in contacting me.")

st.write(
    "**Total Interactions:**",
    st.session_state.visitor_count
)


# FOOTER
st.divider()

st.caption(
    "Online Resume | THARANI SEKAR | IT Networking Student"
)
