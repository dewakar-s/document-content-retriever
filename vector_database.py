import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
file_path = "C:/Users/dewakar/OneDrive/Documents/mindX/Forex_Trading_For_Beginners.pdf"
collection = client.get_or_create_collection(name="sample_document")

def store_in_chromadb(document_ids, document_contents):
    
    collection.add(ids=document_ids, documents=document_contents)
def search_in_chromadb(query_text, k_results):
    

    results = collection.query(
    query_texts=[query_text],
    n_results= k_results
)
    retrieved_documents = results['documents'][0]
    context = "\n\n".join(retrieved_documents)
    return context