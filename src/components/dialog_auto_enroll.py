import streamlit as st
from src.database.db import create_subject
from src.database.config import supabase
from src.database.db import enroll_student_to_subject, unenroll_student_from_subject
import time

@st.dialog("Quick enrollment")
def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data['student_id']

    res = supabase.table("subjects").select("subject_id,name").eq("subject_code",subject_code).execute()

    if not res.data:
        st.error("Subject not found.")
        if st.button("Close"):
            st.query_params.clear()
            st.rerun()
        return
    subject = res.data[0]
    check = supabase.table("subject_students").select("*").eq("subject_id",subject["subject_id"]).eq("student_id",student_id).execute()
    if check.data:
        st.info("You are already enrolled in this subject!")
        if st.button("Close"):
            st.query_params.clear()
            st.rerun()
        return
    st.markdown(f"would you like to enroll in **{subject['name']}**?")
    col1,col2 = st.columns(2)
    with col1:
        if st.button("Enroll",type="primary",width="stretch"):
            enroll_student_to_subject(student_id,subject["subject_id"])
            st.success("Enrolled successfully!")
            time.sleep(1)
            st.query_params.clear()
            st.rerun()
    with col2:      
        if st.button("Cancel",type="secondary",width="stretch"):
            st.query_params.clear()
            st.rerun()



    