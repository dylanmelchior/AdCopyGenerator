import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st

openai.api_key = st.secrets.get("openai", {}).get("api_key")

def call_openAI(prompt):
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4.1",
        input = prompt
    )
    return response.output_text
