from flask import Flask, request, render_template, redirect, url_for
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from werkzeug.utils import secure_filename
import os
import file_preprocessing 
import vector_database 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        
        secure_name = secure_filename(file.filename)
       
        file_path = os.path.join(app.root_path, secure_name)
        file.save(file_path)
        file_preprocessing.pdf_to_chunks(file_path)

    return redirect(url_for('index'))


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('search')
    print(query)
    if query:
        answer = vector_database.search_in_chromadb(query,2)
        return f'You searched for: {query} and answer is {answer}'
    return 'Please enter a search query.'