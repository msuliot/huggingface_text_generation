import requests
import os
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN') # api key for huggingface.co in .env file
model_name = os.getenv('MODEL_NAME') # model name for huggingface.co in .env file


def set_local_vars():
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    return api_url


def hf_api(api_url, text):
    headers = {"Authorization": f"Bearer {hf_api_key}"}

    def query(payload):
        response = requests.post(api_url, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": text,
    })
    return output


def main():
    api_url = set_local_vars()
    text = "paragraph about artificial intelligence"
    return_value = hf_api(api_url, text)
    print(return_value)


if __name__ == "__main__":
    main() 