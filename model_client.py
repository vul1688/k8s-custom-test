# File name: model_client.py
import requests

english_text = "Hello world!"

response = requests.post("http://127.0.0.1:8000/hahaha", json=english_text)
french_text = response.text

print(french_text)

response = requests.post("http://127.0.0.1:8000/hehehe", json=english_text)
french_text = response.text

print(french_text)