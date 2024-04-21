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
    subject_desciption = st.text_area("Please pass 'Subject' here ")
    question_count = st.text_input('No of questions to return', key="2")

    pdf = st.file_uploader("Upload learning material here (PDF only)", type=["pdf"], accept_multiple_files=True)

    submit = st.button("Create some valuable questions")

    if submit:
        with st.spinner('Wait for it...'):

            # Creating a unique ID, so that we can use the query
            # and get only the user uploaded documents from Pinecone
            st.session_state['unique_id']=uuid.uuid4().hex

            final_docs_list = create_docs(pdf, st.session_state['unique_id'])

            st.write("*Resumes uploaded* :" str(len(final_docs_list)))

            # Creating embeddings instance
            embeddings = create_embeddings_load()

            # Push data to PINECONE
            push_to_pinecone("s")

