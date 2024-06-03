from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter 
import json
import os 

DATA_PATH = 'data/'
DB_FAISS_PATH = 'vectorstore/db_faiss'

# Function to load JSON files from a directory
def load_json_files(directory):
    json_documents = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                json_documents += json.load(file)  # Each JSON file contains a list of dictionaries
    return json_documents

# Create vector database
def create_vector_db():
    json_documents = load_json_files(DATA_PATH)
    texts = [doc['input'] for doc in json_documents]  # Extract 'input' text from each dictionary

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})

    db = FAISS.from_texts(texts, embeddings)  # method call
    db.save_local(DB_FAISS_PATH)

if __name__ == "__main__":
    create_vector_db()








