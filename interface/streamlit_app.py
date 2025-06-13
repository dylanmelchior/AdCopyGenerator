import sys
import os
import io

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import csv
import app

## Session State Variables
for key in ["tagline", "long_headlines", "short_headlines", "descriptions"]:
    if key not in st.session_state:
        st.session_state[key] = None

st.write("API key loaded:", bool(st.secrets.get("openai", {}).get("api_key")))

## Title and interface
st.title("Sales Proposition + Headline Generator")
input_type = st.radio("Choose input method:", ["Manual description", "Website URL"])
file_name = st.text_input("Enter file name (e.g., output.csv):")

def get_csv_buffer(tagline, short_headlines, long_headlines, descriptions):
    output = io.StringIO()
    writer = csv.writer(output)
    headers = ["Campaign"] + ["Asset Group"] + [f"Headline {i+1}" for i in range(15)] + [f"Long headline {i+1}" for i in range(5)] + [f"Description {i+1}" for i in range(5)]
    row = [""] + [""] + short_headlines + long_headlines + descriptions
    writer.writerow(headers)
    writer.writerow(row)
    return output.getvalue()

## Helper Method to Display Output
def display_output():
    st.subheader("Tagline")
    st.write(st.session_state.tagline)

    st.subheader("Long Headlines")
    for h in st.session_state.long_headlines:
        st.write(f"- {h}")

    st.subheader("Short Headlines")
    for h in st.session_state.short_headlines:
        st.write(f"- {h}")

    st.subheader("Descriptions")
    for d in st.session_state.descriptions:
        st.write(f"- {d}")

## Manual Description Input Functionality
if input_type == "Manual description":
    text_input = st.text_area("Paste company description here:")
    if st.button("Generate from Text"):
        st.session_state.tagline, st.session_state.long_headlines, st.session_state.short_headlines, st.session_state.descriptions = app.generator.generate_outputs_from_text(text_input)
        display_output()

## Website URL Scrape Input Functionality
elif input_type == "Website URL":
    url_input = st.text_input("Enter company website:")
    if st.button("Generate from URL"):
        outputs = app.generator.generate_outputs_from_url(url_input)
        st.session_state.tagline, st.session_state.long_headlines, st.session_state.short_headlines, st.session_state.descriptions = app.generator.generate_outputs_from_url(url_input)
        st.write("DEBUG output from generate_outputs_from_url:", outputs)
        display_output()

csv_data = get_csv_buffer(st.session_state.tagline, st.session_state.short_headlines, st.session_state.long_headlines, st.session_state.descriptions)
st.download_button("Download CSV", data=csv_data, file_name="adcopy_outputs.csv", mime="text/csv")
