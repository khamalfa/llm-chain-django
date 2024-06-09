# chatbot.py

from langchain_community.llms import Ollama

class Bot:
    def __init__(self):
        self.ollama = Ollama(
            base_url='http://localhost:11434',
            model="qwen2:1.5b"
        )
    
    def ask(self, question):
        return self.ollama.invoke(question)
