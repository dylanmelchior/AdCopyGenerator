import sys
import os
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import csv
import app

## Session State Variables
for key in ["tagline", "long_headlines", "short_headlines", "descriptions"]:
    if key not in st.session_state:
        st.session_state[key] = None

## Title and interface
st.title("Sales Proposition + Headline Generator")
input_type = st.radio("Choose input method:", ["Manual description", "Website URL"])
file_name = st.text_input("Enter file name (e.g., output.csv):")

## Export to csv functionality
def export_to_csv(file_name):
    headers = ["Tagline"]
    headers += [f"Short Headline {i+1}" for i in range(15)]
    headers += [f"Long Headline {i+1}" for i in range(5)]
    headers += [f"Description {i+1}" for i in range(5)]

    row = [st.session_state.tagline or ""]

    row += (st.session_state.short_headlines or [])[:15] + [""] * (15 - len(st.session_state.short_headlines or []))
    row += (st.session_state.long_headlines or [])[:5] + [""] * (5 - len(st.session_state.long_headlines or []))
    row += (st.session_state.descriptions or [])[:5] + [""] * (5 - len(st.session_state.descriptions or []))

    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerow(row)

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

## Export button functionality
if st.button("Export"):
    if all([
        st.session_state.tagline,
        st.session_state.long_headlines,
        st.session_state.short_headlines,
        st.session_state.descriptions
    ]):
        export_to_csv(file_name)
        st.success(f"Exported to {file_name}")
    else:
        st.warning("No content generated. Please run generation first.")
