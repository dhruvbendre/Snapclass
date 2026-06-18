import streamlit as st
from src.components.header import header_dashboard
from src.ui.base_layout import style_base_layout
from src.ui.base_layout import style_background_dashboard
from src.database.db import create_teacher, check_teacher_exists, teacher_login, create_students
import time
from PIL import Image
from src.pipelines.face_pipeline import predict_attendence, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embeddings
from src.database.db import get_all_students,get_teacher_subjects, get_student_subjects, get_student_sttendance
import numpy as np
from src.components.dialog_enroll import dialog_enroll as enroll_dialog 
from src.components.subject_card import subject_card
from src.database.db import unenroll_student_from_subject


def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data["student_id"]
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f""""Welcome,{student_data['name']}""")
        if st.button("Go Back to home", key="loginbackbtn", shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()

    st.space()

    c1,c2 = st.columns(2)
    with c1:
        st.header("your enrolled subjects")
    with c2:
        if st.button("enroll in",type="primary",width="stretch"):
            enroll_dialog()

    st.divider()
    with st.spinner("loading your subjects"):
        subjects = get_student_subjects(student_id)
        logs = get_student_sttendance(student_id)

        stats_map = {}

        for log in logs:
            sid = log['subject_id']
            if sid not in stats_map:
                stats_map[sid] = {"total":0,"attended":0}
            stats_map[sid]["total"] += 1

            if log.get('is_present'):
                stats_map[sid]["attended"]+=1

        cols = st.columns(2)
        for i, sub_nodes in enumerate(subjects):
            sub = sub_nodes['subjects']
            sid = sub['subject_id']

            stats = stats_map.get(sid,{"total":0,"attended":0})

            def unenroll_button():
                if st.button("unenroll from this course",type="tertiary",width="stretch"):
                    unenroll_student_from_subject(student_id,sid)
                    st.success("unenrolled successfully")
                    time.sleep(1)
                    st.rerun()

            with cols[i%2]:
                subject_card(
                    name = sub['name'],
                    code = sub['subject_code'],
                    section = sub['section'],
                    stats = [
                        ("📈","Total",stats['total']),
                        ("✅","Attended",stats['attended'])
                    ],
                    footer_callback=unenroll_button
                )




def student_screen():
    style_base_layout()
    style_background_dashboard()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back to home", key="loginbackbtn", shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    # Fixed text alignment by using HTML formatting inside st.markdown
    st.markdown("<h2 style='text-align: center;'>Login using your FaceID</h2>", unsafe_allow_html=True)
    
    # Replaced non-existent st.space() with proper markdown breaks
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Initialize show_registrations state so it survives input/interaction reruns
    if "show_registrations" not in st.session_state:
        st.session_state.show_registrations = False

    photo_source = st.camera_input('align your face in the center')
    
    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner("AI is Scanning...."):
            detected, all_ids, num_faces = predict_attendence(img)

            if num_faces == 0:
                st.warning("No Faces Found")
            elif num_faces > 1:
                st.warning("multiple faces found")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    students = next((s for s in all_students if s['student_id'] == student_id), None)

                    if students:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = students
                        st.toast(f"Welcome Back, {students['name']}") 
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.info("face not recognized, you might be a new student")
                        st.session_state.show_registrations = True
                else:
                    st.info("face not recognized, you might be a new student")
                    st.session_state.show_registrations = True

    if st.session_state.show_registrations:
        with st.container(border=True):
            st.header("Register new profile")
            new_name = st.text_input("enter your name", placeholder="eg-Dhruv Bendre")
            st.subheader('Optional: voice enrollment')
            st.info("enroll your voice only for attendance")
            
            audio_data = None
            try:
                audio_data = st.audio_input("record your voice audio")
            except Exception as e:
                st.error("Audio Data Failed")

            if st.button("create your account", type="primary"):
                if new_name:
                    if photo_source:  # Guard rail check against missing or stale camera buffers
                        with st.spinner("creating a new profile"):
                            img = np.array(Image.open(photo_source))
                            encoding = get_face_embeddings(img)
                            
                            if encoding:
                                face_emb = encoding[0].tolist()
                                voice_emb = None
                                if audio_data:
                                    voice_emb = get_voice_embeddings(audio_data.read())

                                response_data = create_students(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                                if response_data:
                                    train_classifier()
                                    st.session_state.is_logged_in = True
                                    st.session_state.user_role = 'student'
                                    st.session_state.student_data = response_data[0]
                                    st.toast(f"Profile Created, welcome! {new_name}") 
                                    
                                    # Cleanup step: Turn off registration flag for future baseline logins
                                    st.session_state.show_registrations = False
                                    time.sleep(1)
                                    st.rerun()
                            else:
                                st.error("couldn't capture your facial features for recognition")
                    else:
                        st.error("Please provide a face scan via the camera component above.")
                else:
                    st.warning("Please enter your name")