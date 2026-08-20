import streamlit as st
import pandas as pd
import base64
from pathlib import Path
import streamlit.components.v1 as components


# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Tharani Sekar Resume",
    page_icon="📄",
    layout="wide"
)


# ============================================================
# SESSION STATE
# ============================================================
if "visitor_count" not in st.session_state:
    st.session_state.visitor_count = 0


# ============================================================
# LOAD PROFILE PICTURE
# ============================================================
image_path = Path("profile.jpg")

if image_path.exists():
    with open(image_path, "rb") as image_file:
        profile_base64 = base64.b64encode(
            image_file.read()
        ).decode("utf-8")
else:
    profile_base64 = ""


# ============================================================
# STREAMLIT PAGE STYLE
# ============================================================
st.markdown(
    """
    <style>

    .stApp {
        background-color: #e6e6e6;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #d0d0d0;
        padding: 12px;
        border-radius: 7px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# REAL RESUME DESIGN
# ============================================================
resume_html = f"""
<!DOCTYPE html>
<html>

<head>

<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    padding: 0;
    background: #e6e6e6;
    font-family: Arial, Helvetica, sans-serif;
}}

.resume {{
    width: 760px;
    min-height: 1075px;
    margin: 10px auto;
    background: white;
    color: #222222;
    padding: 35px 40px;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.18);
}}


/* ================= HEADER ================= */

.header {{
    display: grid;
    grid-template-columns: 185px 1fr;
    column-gap: 28px;
    align-items: center;
    margin-bottom: 22px;
}}

.photo-area {{
    text-align: center;
}}

.photo {{
    width: 155px;
    height: 155px;
    border-radius: 50%;
    object-fit: cover;
    object-position: center;
    border: 4px solid #243b53;
}}

.name {{
    color: #243b53;
    font-size: 38px;
    line-height: 0.98;
    font-weight: 800;
    letter-spacing: 0.5px;
}}

.job-title {{
    margin-top: 10px;
    color: #333333;
    font-size: 15px;
    letter-spacing: 1.5px;
}}

.contact-top {{
    margin-top: 15px;
    font-size: 11.5px;
    line-height: 1.8;
    color: #333333;
}}


/* ================= BODY ================= */

.main-grid {{
    display: grid;
    grid-template-columns: 34% 66%;
    column-gap: 22px;
}}

.left {{
    padding-right: 3px;
}}

.right {{
    padding-left: 3px;
}}


.section-title {{
    background: #243b53;
    color: white;
    font-size: 11.5px;
    letter-spacing: 0.5px;
    text-align: center;
    padding: 5px 7px;
    margin-top: 15px;
    margin-bottom: 9px;
    font-weight: bold;
}}

.text {{
    font-size: 11.5px;
    line-height: 1.45;
    text-align: justify;
}}

.list {{
    margin: 0;
    padding-left: 18px;
}}

.list li {{
    font-size: 11.5px;
    line-height: 1.45;
    margin-bottom: 4px;
}}


.item-title {{
    font-size: 12px;
    font-weight: bold;
    color: #243b53;
    margin-top: 8px;
}}

.item-subtitle {{
    font-size: 11px;
    font-weight: bold;
    margin-top: 2px;
}}

.item-date {{
    font-size: 10.5px;
    color: #555555;
    margin-top: 1px;
}}

.item-text {{
    font-size: 11.3px;
    line-height: 1.42;
    margin-top: 4px;
    margin-bottom: 8px;
}}


/* ================= SKILL BARS ================= */

.skill-row {{
    display: grid;
    grid-template-columns: 105px 1fr 30px;
    align-items: center;
    gap: 7px;
    margin-bottom: 8px;
}}

.skill-name {{
    font-size: 10.5px;
}}

.skill-bg {{
    width: 100%;
    height: 6px;
    background-color: #d5dbe0;
    border-radius: 5px;
    overflow: hidden;
}}

.skill-fill {{
    height: 100%;
    background-color: #243b53;
}}

.skill-percent {{
    font-size: 10px;
    color: #555555;
}}


/* ================= DECORATION ================= */

.top-shape {{
    position: absolute;
}}

</style>

</head>


<body>

<div class="resume">


    <!-- ================================================= -->
    <!-- HEADER -->
    <!-- ================================================= -->

    <div class="header">

        <div class="photo-area">

            <img
                src="data:image/jpeg;base64,{profile_base64}"
                class="photo"
            >

        </div>


        <div>

            <div class="name">
                THARANI<br>SEKAR
            </div>

            <div class="job-title">
                IT NETWORKING STUDENT
            </div>

            <div class="contact-top">

                ☎ 012-853 2854
                &nbsp;&nbsp; | &nbsp;&nbsp;

                ✉ tharanist06@gmail.com
                <br>

                📍 Johor, Malaysia

            </div>

        </div>

    </div>


    <!-- ================================================= -->
    <!-- MAIN 2 COLUMN RESUME -->
    <!-- ================================================= -->

    <div class="main-grid">


        <!-- ================= LEFT ================= -->

        <div class="left">


            <div class="section-title">
                ABOUT ME
            </div>

            <div class="text">

                I am a Semester 5 Diploma in Information
                Technology student with a strong interest in
                computer networking, cybersecurity and modern
                technologies.

                I enjoy learning new technical skills,
                solving problems and gaining practical
                experience in the IT field.

            </div>


            <div class="section-title">
                LANGUAGE
            </div>

            <ul class="list">

                <li>Bahasa Melayu</li>
                <li>English</li>
                <li>Tamil</li>

            </ul>


            <div class="section-title">
                EXPERTISE
            </div>

            <ul class="list">

                <li>Cisco Packet Tracer</li>
                <li>Network Configuration</li>
                <li>VLAN Configuration</li>
                <li>Inter-VLAN Routing</li>
                <li>OSPF</li>
                <li>GRE Tunnel</li>
                <li>HSRP</li>
                <li>EtherChannel</li>
                <li>Python Programming</li>
                <li>Windows Server</li>
                <li>Linux</li>
                <li>Cybersecurity</li>
                <li>ESP32 / IoT</li>

            </ul>


            <div class="section-title">
                SOFT SKILLS
            </div>

            <ul class="list">

                <li>Teamwork</li>
                <li>Communication</li>
                <li>Problem Solving</li>
                <li>Time Management</li>
                <li>Responsibility</li>
                <li>Willingness to Learn</li>

            </ul>


        </div>


        <!-- ================= RIGHT ================= -->

        <div class="right">


            <div class="section-title">
                EDUCATION
            </div>


            <div class="item-title">

                Diploma in Information Technology

            </div>


            <div class="item-subtitle">

                Politeknik Malaysia

            </div>


            <div class="item-date">

                Semester 5 | Networking

            </div>


            <div class="item-text">

                Current study areas include Computer Networking,
                Switching and Routing, Cybersecurity,
                Python Programming, Server Administration
                and Internet of Things.

            </div>



            <div class="section-title">
                ACADEMIC PROJECTS
            </div>


            <div class="item-title">

                Networking Configuration Project

            </div>

            <div class="item-text">

                Configured and tested VLANs, Inter-VLAN Routing,
                OSPF, GRE Tunnel, HSRP and EtherChannel
                using Cisco Packet Tracer.

            </div>



            <div class="item-title">

                IoT Project

            </div>

            <div class="item-text">

                Developed an IoT-based project using ESP32
                and sensors to collect and monitor
                real-time data.

            </div>



            <div class="item-title">

                Cybersecurity Practical

            </div>

            <div class="item-text">

                Performed basic network scanning,
                traffic analysis and security testing
                in a controlled laboratory environment.

            </div>



            <div class="item-title">

                Python Programming

            </div>

            <div class="item-text">

                Developed Python programs using functions,
                classes, object-oriented programming
                and Streamlit.

            </div>



            <div class="section-title">
                CAREER OBJECTIVE
            </div>


            <div class="item-text">

                To strengthen my knowledge and practical skills
                in networking and information technology while
                gaining industry experience that will prepare me
                for a professional career in IT.

            </div>



            <div class="section-title">
                SKILLS SUMMARY
            </div>


            <div class="skill-row">

                <div class="skill-name">
                    Networking
                </div>

                <div class="skill-bg">

                    <div
                        class="skill-fill"
                        style="width:85%">
                    </div>

                </div>

                <div class="skill-percent">
                    85%
                </div>

            </div>



            <div class="skill-row">

                <div class="skill-name">
                    Cisco
                </div>

                <div class="skill-bg">

                    <div
                        class="skill-fill"
                        style="width:80%">
                    </div>

                </div>

                <div class="skill-percent">
                    80%
                </div>

            </div>



            <div class="skill-row">

                <div class="skill-name">
                    Python
                </div>

                <div class="skill-bg">

                    <div
                        class="skill-fill"
                        style="width:75%">
                    </div>

                </div>

                <div class="skill-percent">
                    75%
                </div>

            </div>



            <div class="skill-row">

                <div class="skill-name">
                    Cybersecurity
                </div>

                <div class="skill-bg">

                    <div
                        class="skill-fill"
                        style="width:70%">
                    </div>

                </div>

                <div class="skill-percent">
                    70%
                </div>

            </div>



            <div class="skill-row">

                <div class="skill-name">
                    Windows Server
                </div>

                <div class="skill-bg">

                    <div
                        class="skill-fill"
                        style="width:75%">
                    </div>

                </div>

                <div class="skill-percent">
                    75%
                </div>

            </div>


        </div>


    </div>


</div>

</body>

</html>
"""


# ============================================================
# IMPORTANT:
# Render HTML using components.html instead of st.markdown
# ============================================================
components.html(
    resume_html,
    height=1130,
    scrolling=False
)


# ============================================================
# REQUIRED STREAMLIT FEATURES
# ============================================================
st.divider()

st.subheader("Resume Details")


# ============================================================
# METRIC + COLUMN
# ============================================================
metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric(
        "Current Semester",
        "5"
    )

with metric2:
    st.metric(
        "Programme",
        "Diploma IT"
    )

with metric3:
    st.metric(
        "Field",
        "Networking"
    )


# ============================================================
# TABS
# ============================================================
tab1, tab2, tab3 = st.tabs(
    [
        "Education",
        "Skills",
        "Contact"
    ]
)


# ============================================================
# PANDAS + STATIC DATAFRAME
# ============================================================
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

    education_df = pd.DataFrame(
        education_data
    )

    st.dataframe(
        education_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# DATA EDITOR
# ============================================================
with tab2:

    skills_data = {

        "Skill": [

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

    skills_df = pd.DataFrame(
        skills_data
    )

    st.data_editor(
        skills_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# POPOVER
# ============================================================
with tab3:

    st.write(
        "Contact me using the information below."
    )

    with st.popover(
        "View Contact Details"
    ):

        st.write(
            "**THARANI SEKAR**"
        )

        st.write(
            "IT Networking Student"
        )

        st.write(
            "📞 012-853 2854"
        )

        st.write(
            "📧 tharanist06@gmail.com"
        )

        st.write(
            "📍 Johor, Malaysia"
        )


# ============================================================
# SIDEBAR
# ============================================================
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


# ============================================================
# 7 USER EVENTS
# ============================================================
st.divider()

with st.expander(
    "Interactive Resume"
):

    st.write(
        "Interactive elements for the Streamlit assignment."
    )


    # 1. TEXT INPUT
    visitor_name = st.text_input(
        "Enter your name"
    )


    # 2. SELECTBOX
    interest = st.selectbox(
        "Choose an IT area",
        [
            "Networking",
            "Cybersecurity",
            "Programming",
            "Internet of Things"
        ]
    )


    # 3. SLIDER
    rating = st.slider(
        "Rate my resume",
        min_value=1,
        max_value=10,
        value=5
    )


    # 4. CHECKBOX
    contact_interest = st.checkbox(
        "I am interested in contacting Tharani"
    )


    # 5. RADIO
    contact_method = st.radio(
        "Preferred contact method",
        [
            "Email",
            "Phone"
        ]
    )


    # 6. TOGGLE
    show_objective = st.toggle(
        "Show career objective"
    )


    if show_objective:

        st.info(
            "My career objective is to strengthen "
            "my networking and IT skills and gain "
            "professional industry experience."
        )


    # 7. BUTTON
    if st.button(
        "Submit"
    ):

        st.session_state.visitor_count += 1


        if visitor_name:

            st.success(
                f"Thank you, {visitor_name}, "
                "for viewing my resume."
            )

        else:

            st.success(
                "Thank you for viewing my resume."
            )


    st.caption(
        f"Total interactions: "
        f"{st.session_state.visitor_count}"
    )


# ============================================================
# FOOTER
# ============================================================
st.divider()

st.caption(
    "THARANI SEKAR | IT NETWORKING STUDENT"
)
