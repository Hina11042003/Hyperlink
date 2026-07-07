from transformers import pipeline
generator = pipeline("text2text-generation", model="google/flan-t5-base")
prompt = "Write a short professional bio for someone skilled in Python, Django, and SQL."
result = generator(prompt, max_length=60)
print(result[0]['generated_text'])