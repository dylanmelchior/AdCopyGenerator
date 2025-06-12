import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
# Prefer secrets if running in Streamlit Cloud, fallback to .env locally
api_key = st.secrets.get("openai", {}).get("api_key") # or os.getenv("OPENAI_API_KEY")

def call_openAI(prompt):

    if not api_key:
        raise ValueError("OpenAI API key is missing. Set it in .env or Streamlit secrets.")

    # Correct instantiation
    client = OpenAI(api_key=api_key)


    response = client.responses.create(
        model="gpt-4.1",
        input = prompt
    )

    return response.output_text
