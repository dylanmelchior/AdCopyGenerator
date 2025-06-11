import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def call_openAI(prompt):
    # Prefer secrets if running in Streamlit Cloud, fallback to .env locally
    api_key = st.secrets.get("openai", {}).get("api_key") or os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OpenAI API key is missing. Set it in .env or Streamlit secrets.")

    # Correct instantiation
    client = OpenAI()
    client.api_key = api_key


    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
