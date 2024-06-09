# main.py

import argparse
from langchain_community.llms import Ollama
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description='Ask a question to the Ollama model.')
    parser.add_argument('--question', type=str, required=True, help='The question to ask the Ollama model.')
    args = parser.parse_args()
    question = args.question

    ollama = Ollama(
        base_url='http://localhost:11434',
        model="qwen2:1.5b"
    )
    
    # Initialize the Ollama model
    
    # # Invoke the Ollama model with the question
    response = ollama.invoke(question)
    
    # Print the response
    print(response)

if __name__ == "__main__":
    main()
