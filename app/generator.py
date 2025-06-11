from app.prompts import build_prompt
from app.openapi_client import call_openAI
from app.scraper import extract_company_info

def generate_outputs_from_text(company_info_text):
    prompt = build_prompt(company_info_text)
    response = call_openAI(prompt)
    tagline, long_headlines, short_headlines, descriptions = parse_response(response)
    return tagline, long_headlines, short_headlines, descriptions

def generate_outputs_from_url(url):
    info = extract_company_info(url)
    return generate_outputs_from_text(info)

def parse_response(response_text):
    lines = response_text.strip().split("\n")
    tagline = lines[0]
    long_headlines = [line.strip("- ") for line in lines[1:7] if line.strip()]
    short_headlines = [line.strip("- ") for line in lines[7:23] if line.strip()]
    descriptions = [line.strip("- ") for line in lines[23:] if line.strip()]

    return tagline, long_headlines, short_headlines, descriptions