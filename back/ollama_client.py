import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL  = "qwen2.5:3b"

def ask_ollama(prompt: str):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return result["response"]