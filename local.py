from transformers import pipeline, AutoTokenizer
from transformers import AutoModelForCausalLM, TFAutoModelForCausalLM

import os
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN') # api key for huggingface.co in .env file
model_name = os.getenv('MODEL_NAME') # model name for huggingface.co in .env file
pipeline_task = os.getenv('PIPELINE_TASK') # pipeline task for huggingface.co in .env file
os.environ['TOKENIZERS_PARALLELISM'] = 'true'


def hf_local(text):
    # This will download the model and tokenizer to your local machine and run on your local machine. 
    # saved and cached ~/.cache/huggingface
    tokenizer = AutoTokenizer.from_pretrained(model_name, return_tensors="pt") # return_tensors="pt" or "tf"
    model = AutoModelForCausalLM.from_pretrained(model_name) 
    pipe = pipeline(pipeline_task, model=model, tokenizer=tokenizer)
    output = pipe(text)
    return output


def main():
    text = "paragraph about artificial intelligence" 
    return_value = hf_local(text)
    print(return_value)

if __name__ == "__main__":
    main() 