from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st


api_key = st.secrets.get("openai", {}).get("api_key")

def call_openAI(prompt):
    client = OpenAI()
    client.api_key = api_key
    response = client.responses.create(
        model="gpt-4.1",
        input = prompt
    )
    return response.output_text
