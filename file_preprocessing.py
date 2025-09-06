
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from werkzeug.utils import secure_filename
import os
import vector_database


def pdf_to_chunks(file_path):
    
        try:
            
            loader = PyPDFLoader(file_path)
            document = loader.load()
            
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            chunked_documents = text_splitter.split_documents(document)
            
            document_contents = [doc.page_content for doc in chunked_documents]
            document_ids = [f"id{i}" for i in range(len(document_contents))]
            
            vector_database.store_in_chromadb(document_ids, document_contents)
        except Exception as e:
            print(f"Error loading document: {e}")
            return 'Error processing document', 500
        finally:
            
            os.remove(file_path)