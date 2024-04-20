import streamlit as st
from dotenv import load_dotenv
from utils import *
import uuid

if 'unique_id' not in st.session_state:
    st.session_state['unique_id']=''


# creating session variables
def main():
    load_dotenv()

    st.set_page_config(page_title="Exam Trainer Application")
    st.title("This is your environment to test your knowledge and master anything")
    st.subheader("Try me and thrive in your upcoming Examns")
    subject_desciption = st.text_area("Please pass "Subject" here ")
    question_count = st.text_input('No of questions to return', key="2")