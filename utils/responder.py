import os
import requests

API_TOKEN = os.getenv("HF_API_TOKEN")  # Get token from environment variable

# Use a generative model instead of question-answering model
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def get_chatgpt_response(question):
    prompt = f"Question: {question}\nAnswer:"

    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.5,
            "max_new_tokens": 50
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        try:
            result = response.json()
            generated_text = result[0]['generated_text']
            # Extract answer after "Answer:"
            if "Answer:" in generated_text:
                return generated_text.split("Answer:")[-1].strip()
            else:
                return generated_text.strip()
        except Exception as e:
            return "Sorry, I couldn't parse the response."
    else:
        return f"Error: {response.status_code} - {response.text}"
