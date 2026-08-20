import streamlit as st
import pandas as pd
import base64
from pathlib import Path

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Tharani Sekar Resume",
    page_icon="📄",
    layout="wide"
)

# =========================================================
# SESSION STATE
# =========================================================
if "visitor_count" not in st.session_state:
    st.session_state.visitor_count = 0


# =========================================================
# CONVERT PROFILE IMAGE TO BASE64
# =========================================================
image_path = Path("profile.jpg")

if image_path.exists():
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
else:
    encoded_image = ""


# =========================================================
# PAGE CSS
# =========================================================
st.markdown("""
<style>

/* Whole Streamlit background */
[data-testid="stAppViewContainer"] {
    background: #d9d9d9;
}

/* Reduce Streamlit default spacing */
.block-container {
    max-width: 950px;
    padding-top: 25px;
    padding-bottom: 50px;
}

/* Hide Streamlit top empty header space */
[data-testid="stHeader"] {
    background: transparent;
}

/* Resume page */
.resume-page {
    width: 100%;
    background: white;
    color: #222;
    padding: 38px 42px;
    box-sizing: border-box;
    font-family: Arial, Helvetica, sans-serif;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.16);
    min-height: 1120px;
}

/* Header */
.resume-header {
    display: grid;
    grid-template-columns: 180px 1fr;
    align-items: center;
    gap: 25px;
    margin-bottom: 22px;
}

.profile-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
}

.profile-photo {
    width: 155px;
    height: 155px;
    border-radius: 50%;
    object-fit: cover;
    border: 5px solid #243b53;
}

.name {
    font-size: 39px;
    line-height: 1;
    font-weight: 800;
    color: #243b53;
    letter-spacing: 1px;
    margin: 0;
}

.role {
    font-size: 16px;
    color: #444;
    letter-spacing: 2px;
    margin-top: 8px;
}

/* Main two columns */
.resume-grid {
    display: grid;
    grid-template-columns: 34% 66%;
    gap: 22px;
}

/* Section bars */
.section-title {
    background: #243b53;
    color: white;
    font-size: 13px;
    font-weight: bold;
    text-align: center;
    padding: 6px 8px;
    margin-top: 16px;
    margin-bottom: 10px;
    letter-spacing: 0.5px;
}

.left-column {
    padding-right: 5px;
}

.right-column {
    padding-left: 5px;
}

/* Normal text */
.resume-page p {
    font-size: 12.5px;
    line-height: 1.55;
    margin: 4px 0;
}

.resume-page ul {
    margin-top: 6px;
    padding-left: 20px;
}

.resume-page li {
    font-size: 12.5px;
    margin-bottom: 5px;
}

/* Contact section */
.contact-item {
    font-size: 12px;
    margin: 8px 0;
}

/* Main section item headings */
.item-title {
    font-size: 13px;
    font-weight: bold;
    color: #243b53;
    margin-top: 9px;
}

.item-subtitle {
    font-size: 12px;
    font-weight: bold;
    margin-top: 2px;
}

.item-date {
    font-size: 11.5px;
    color: #555;
}

/* Skill bars */
.skill-row {
    display: grid;
    grid-template-columns: 120px 1fr 35px;
    align-items: center;
    gap: 8px;
    margin: 8px 0;
}

.skill-name {
    font-size: 11.5px;
}

.skill-bar {
    height: 6px;
    background: #d6dce2;
    border-radius: 4px;
    overflow: hidden;
}

.skill-fill {
    height: 100%;
    background: #243b53;
}

.skill-percent {
    font-size: 11px;
    color: #555;
}

/* Divider */
.resume-divider {
    height: 1px;
    background: #dedede;
    margin: 10px 0;
}

/* Streamlit requirement area */
.requirement-box {
    background: white;
    color: #222;
    padding: 15px;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# ACTUAL RESUME
# =========================================================
resume_html = f"""
<div class="resume-page">

    <!-- HEADER -->
    <div class="resume-header">

        <div class="profile-wrapper">
            <img
                src="data:image/jpeg;base64,{encoded_image}"
                class="profile-photo"
            >
        </div>

        <div>
            <div class="name">THARANI<br>SEKAR</div>
            <div class="role">IT NETWORKING STUDENT</div>
        </div>

    </div>


    <!-- TWO COLUMN RESUME -->
    <div class="resume-grid">

        <!-- ================= LEFT COLUMN ================= -->
        <div class="left-column">

            <div class="section-title">ABOUT ME</div>

            <p>
                I am a Semester 5 Diploma in Information Technology student
                with a strong interest in computer networking, cybersecurity
                and modern technologies. I enjoy learning new technical skills,
                solving problems and gaining practical experience in the IT field.
            </p>


            <div class="contact-item">📞 012-853 2854</div>
            <div class="contact-item">📧 tharanist06@gmail.com</div>
            <div class="contact-item">📍 Johor, Malaysia</div>


            <div class="section-title">LANGUAGE</div>

            <ul>
                <li>Bahasa Melayu</li>
                <li>English</li>
                <li>Tamil</li>
            </ul>


            <div class="section-title">EXPERTISE</div>

            <ul>
                <li>Cisco Packet Tracer</li>
                <li>Network Configuration</li>
                <li>VLAN & Inter-VLAN Routing</li>
                <li>OSPF Routing</li>
                <li>Python Programming</li>
                <li>Windows Server</li>
                <li>Cybersecurity</li>
                <li>ESP32 / IoT</li>
            </ul>


            <div class="section-title">SOFT SKILLS</div>

            <ul>
                <li>Teamwork</li>
                <li>Communication</li>
                <li>Problem Solving</li>
                <li>Time Management</li>
                <li>Willingness to Learn</li>
            </ul>

        </div>


        <!-- ================= RIGHT COLUMN ================= -->
        <div class="right-column">

            <div class="section-title">EDUCATION</div>

            <div class="item-title">
                Diploma in Information Technology
            </div>

            <div class="item-subtitle">
                Politeknik Malaysia
            </div>

            <div class="item-date">
                Semester 5 | Networking
            </div>

            <p>
                Current studies include Computer Networking,
                Switching and Routing, Cybersecurity,
                Python Programming, Server Administration
                and Internet of Things.
            </p>


            <div class="section-title">ACADEMIC PROJECTS</div>


            <div class="item-title">
                Networking Configuration Project
            </div>

            <p>
                Configured VLANs, Inter-VLAN Routing,
                OSPF, GRE Tunnel, HSRP and EtherChannel
                using Cisco Packet Tracer.
            </p>


            <div class="item-title">
                IoT Project
            </div>

            <p>
                Developed an IoT-based project using ESP32
                and sensors to collect and monitor real-time data.
            </p>


            <div class="item-title">
                Cybersecurity Practical
            </div>

            <p>
                Performed basic network scanning,
                traffic analysis and security testing
                in a controlled laboratory environment.
            </p>


            <div class="item-title">
                Python Programming
            </div>

            <p>
                Developed Python programs using functions,
                classes, object-oriented programming
                and Streamlit.
            </p>


            <div class="section-title">CAREER OBJECTIVE</div>

            <p>
                To strengthen my knowledge and practical skills
                in networking and information technology while
                gaining industry experience that will prepare
                me for a professional career in IT.
            </p>


            <div class="section-title">SKILLS SUMMARY</div>


            <div class="skill-row">
                <div class="skill-name">Networking</div>

                <div class="skill-bar">
                    <div class="skill-fill"
                         style="width:85%;">
                    </div>
                </div>

                <div class="skill-percent">85%</div>
            </div>


            <div class="skill-row">
                <div class="skill-name">Cisco</div>

                <div class="skill-bar">
                    <div class="skill-fill"
                         style="width:80%;">
                    </div>
                </div>

                <div class="skill-percent">80%</div>
            </div>


            <div class="skill-row">
                <div class="skill-name">Python</div>

                <div class="skill-bar">
                    <div class="skill-fill"
                         style="width:75%;">
                    </div>
                </div>

                <div class="skill-percent">75%</div>
            </div>


            <div class="skill-row">
                <div class="skill-name">Cybersecurity</div>

                <div class="skill-bar">
                    <div class="skill-fill"
                         style="width:70%;">
                    </div>
                </div>

                <div class="skill-percent">70%</div>
            </div>


            <div class="skill-row">
                <div class="skill-name">Windows Server</div>

                <div class="skill-bar">
                    <div class="skill-fill"
                         style="width:75%;">
                    </div>
                </div>

                <div class="skill-percent">75%</div>
            </div>

        </div>

    </div>

</div>
"""

st.markdown(resume_html, unsafe_allow_html=True)


# =========================================================
# REQUIRED STREAMLIT ELEMENTS
# Kept BELOW the resume so the CV remains clean.
# =========================================================

st.write("")
st.write("")

with st.expander("📌 Streamlit Resume Features"):

    st.subheader("Resume Information")

    # -----------------------------------------------------
    # METRIC + COLUMNS
    # -----------------------------------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Semester", "5")

    with col2:
        st.metric("Programme", "Diploma IT")

    with col3:
        st.metric("Field", "Networking")


    # -----------------------------------------------------
    # TABS
    # -----------------------------------------------------
    tab1, tab2, tab3 = st.tabs(
        [
            "Education",
            "Skills",
            "Contact"
        ]
    )


    # -----------------------------------------------------
    # STATIC DATAFRAME
    # -----------------------------------------------------
    with tab1:

        education_data = {
            "Programme": [
                "Diploma in Information Technology"
            ],
            "Semester": [
                "Semester 5"
            ],
            "Field": [
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


    # -----------------------------------------------------
    # DATA EDITOR
    # -----------------------------------------------------
    with tab2:

        skills_data = {
            "Skill": [
                "Networking",
                "Cisco Packet Tracer",
                "Python",
                "Windows Server",
                "Cybersecurity",
                "ESP32 / IoT"
            ],

            "Level": [
                "Intermediate",
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


    # -----------------------------------------------------
    # POPOVER
    # -----------------------------------------------------
    with tab3:

        st.write("My contact information")

        with st.popover("View Contact Details"):

            st.write("**THARANI SEKAR**")
            st.write("IT Networking Student")
            st.write("📞 012-853 2854")
            st.write("📧 tharanist06@gmail.com")
            st.write("📍 Johor, Malaysia")


# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.image(
    "profile.jpg",
    width=130
)

st.sidebar.title(
    "THARANI SEKAR"
)

st.sidebar.write(
    "IT Networking Student"
)

st.sidebar.divider()

st.sidebar.subheader(
    "Contact"
)

st.sidebar.write(
    "📞 012-853 2854"
)

st.sidebar.write(
    "📧 tharanist06@gmail.com"
)

st.sidebar.write(
    "📍 Johor, Malaysia"
)

st.sidebar.divider()

st.sidebar.subheader(
    "Languages"
)

st.sidebar.write(
    "• Bahasa Melayu"
)

st.sidebar.write(
    "• English"
)

st.sidebar.write(
    "• Tamil"
)


# =========================================================
# 7 USER EVENTS
# =========================================================

with st.expander("🖱 Interactive Resume Section"):

    st.write(
        "This section demonstrates the required user events."
    )

    # EVENT 1 - TEXT INPUT
    visitor_name = st.text_input(
        "Enter your name"
    )

    # EVENT 2 - SELECTBOX
    interest = st.selectbox(
        "Which IT area are you interested in?",
        [
            "Networking",
            "Cybersecurity",
            "Programming",
            "Internet of Things"
        ]
    )

    # EVENT 3 - SLIDER
    rating = st.slider(
        "Rate my resume",
        1,
        10,
        5
    )

    # EVENT 4 - CHECKBOX
    contact_interest = st.checkbox(
        "I am interested in contacting Tharani"
    )

    # EVENT 5 - RADIO
    contact_method = st.radio(
        "Preferred contact method",
        [
            "Email",
            "Phone"
        ]
    )

    # EVENT 6 - TOGGLE
    show_objective = st.toggle(
        "Show career objective"
    )

    if show_objective:
        st.info(
            "My goal is to strengthen my networking "
            "and IT skills and gain industry experience."
        )

    # EVENT 7 - BUTTON
    if st.button("Submit"):

        st.session_state.visitor_count += 1

        if visitor_name:

            st.success(
                f"Thank you, {visitor_name}, "
                "for viewing my resume!"
            )

        else:

            st.success(
                "Thank you for viewing my resume!"
            )

    st.caption(
        f"Total interactions: "
        f"{st.session_state.visitor_count}"
    )


# =========================================================
# FOOTER
# =========================================================
st.caption(
    "THARANI SEKAR | IT NETWORKING STUDENT"
)
