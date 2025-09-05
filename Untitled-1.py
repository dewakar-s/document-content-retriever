from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
file_path = "C:/Users/dewakar/OneDrive/Documents/mindX/Forex_Trading_For_Beginners.pdf"

loader = PyPDFLoader(file_path)
document = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunked_documents = text_splitter.split_documents(document)


document_contents = [doc.page_content for doc in chunked_documents]
document_ids = [f"id{i}" for i in range(len(document_contents))]

collection = client.get_or_create_collection(name="sample_document")
collection.add(ids=document_ids,documents=document_contents)

print(chunked_documents)
