import streamlit as st
from src.database.db import create_subject
from src.database.config import supabase
import time
from src.database.db import enroll_student_to_subject, unenroll_student_from_subject
@st.dialog("enroll in subjects")
def dialog_enroll():
    st.write("enter the subject code provided by your teacher to enroll")
    join_code = st.text_input("Subject Code",placeholder="eg : CS101")
    st.button("enroll now",type="primary",width="stretch")
    if join_code:
        res = supabase.table("subjects").select("subject_id,name,subject_code").eq("subject_code",join_code).execute()
        if res.data:
            subject = res.data[0]
            student_id = st.session_state.student_data["student_id"]

            check = supabase.table("subject_students").select("*").eq("subject_id",subject["subject_id"]).eq("student_id",student_id).execute()
            if check.data:
                st.warning("you are already enrolled in this subject")
            else:
                enroll_student_to_subject(student_id,subject["subject_id"])
                st.success("enrolled sucessfully")
                time.sleep(1)
                st.rerun()
    else:
        st.warning("please enter a valid subject code")



    