from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def call_openAI(prompt):
    api_key = st.secrets.get("openai", {}).get("api_key") or os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-4.1",
        input = prompt
    )
    return response.output_text
