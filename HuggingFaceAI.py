from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv
load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",  # example model
    task="text-generation",
    max_new_tokens=200,
    do_sample=False,
    provider="auto"
)

chat = ChatHuggingFace(llm=llm)

def get_rephrase_text(text):
    rephrase_text = chat.invoke(f"Just Rephrase the following text. No explanation: {text}")
    return rephrase_text.content

