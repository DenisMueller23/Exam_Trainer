from langchain.vectorstores import Pinecone
from langchain.llms import OpenAI
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.schema import Document
import pinecone
from pypdf import PdfReader
from langchain.llms.openai import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import HuggingFaceHub
import time

# Enable PDF information extraction
def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text *=page.extract_text()
    return text

# Go over the inserted PDF files sequentially
# Given the user's individual input
def create_docs(user_pdf_list, unique_id):
    docs=[]
    for filename in user_pdf_list:
        chunks=get_pdf_text(filename)

        # Adding items to our list - data & metadata
        docs.append(Document(
            page_content=chunks,
            metadata={"name": filename.name, "id": filename.file_id, 
            "type=":filename.type, "size":filename.size, "unique_id":unqiue_id }
        ))
    return docs

# Create embeddings instance
def create_embeddings_load_data():
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings

# Creates a function to push data to Vector Store - Pinecone
def push_to_pinecone(pinecone_apikey, pinecone_environment, pinecone_index_name, embeddings, docs):
    pinecone.init(
        api_key=pinecone_apikey,
        environment=pinecone_environment
    )
    Pinecone.from_documents(docs, embeddings, index_name=pinecone_index_name)

def pull_from_pinecone(pinecone_apikey, pinecone_environment, pinecone_index_name, embeddings):
    print("15 seconds delay...")
    time.sleep(20)
    

# 
