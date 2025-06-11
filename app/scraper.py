from bs4 import BeautifulSoup
import requests

def extract_company_info(url):
    try:
        response = requests.get(url)
        if response.status_code == 403:
            return None

        soup = BeautifulSoup(response.text, 'html.parser')

        content = []
        for tag in soup.find_all(['p', 'h1', 'h2']):
            text = tag.text.strip()
            if text:
                content.append(text)

        return "\n".join(content)[:2950]
    except Exception as e:
        return f"Error scraping site: {e}"