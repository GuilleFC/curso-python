# Cómo hacer peticiones a APIs con Python
# con y sin dependencias

import os
os.system("clear")

# 1. Sin dependencias (díficil y sin dependencias)
import urllib.request
import urllib.error
import json

api_posts = "https://jsonplaceholder.typicode.com/posts/1"

# try:
#     response = urllib.request.urlopen(api_posts)
#     data = response.read()
#     json_data = json.loads(data.decode('utf-8'))
#     print(json_data)
#     response.close()
# except urllib.error.URLError as e:
#     print(f"Error en la solicitud: {e}")

# 2. Con dependencia (request)
import requests

# print("\nGET:")
# response = requests.get(api_posts)
# json = response.json()
# print(json[0])


# 3. Un POST
# print("\nPOST:")
# try:
#     input = {
#         "title": "codex",
#         "body": "dev",
#         "userId": 5
#     }
#     response = requests.post(api_posts, json=input)
#     print(response.status_code)
#     print(response.json())
# except requests.exceptions.RequestException as e:
#     print(f"Error en la solicitud: {e}")

# 3. Un PUT
# print("\nPUT:")
# try:
#     input = {
#         "title": "codex",
#         "body": "dev",
#         "userId": 5
#     }
#     response = requests.put(api_posts, json=input)
#     print(response.status_code)
#     print(response.json())
# except requests.exceptions.RequestException as e:
#     print(f"Error en la solicitud: {e}")

# Usar la API de GPT-4o de OpenAI
# Ref: https://platform.openai.com/docs/api-reference/making-requests

OPENAI_KEY = "sk-XXXXXXXX"

import json

def call_openai_gpt(api_key, prompt):
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])

# Llamar a la API de DEEPSEEK

import json

def call_deepseek(api_key, prompt):
  url = "https://api.deepseek.com/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  print(response.json())
  return response.json()

api_response = call_deepseek(DEEPSEEK_API_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])