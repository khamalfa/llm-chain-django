import ollama

modelfile='''
FROM qwen2
SYSTEM Kamu adalah hadrini, sales dan customer service hadirin
SYSTEM You only need to speak Bahasa Indonesia
'''

new_model = ollama.create(model='qwen2:1.5b', modelfile=modelfile)
print(new_model)