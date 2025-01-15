import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def extract_data_from_url(url):
    try:
        # Fetch webpage content
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()
        return text
    except Exception as e:
        st.error(f"Failed to fetch or parse the URL: {e}")
        return None

def generate_json(data, source_url):
    return {
        "COUNTRY_CODE": {
            "country": "N/A",
            "latitude": "N/A",
            "longitude": "N/A",
            "continent": "N/A",
            "system": "N/A",
            "legislation": "N/A",
            "transposed_the_directive_2014_55_EU": "N/A",
            "format": "N/A",
            "b2g": {
                "mandatory": False,
                "description": "N/A"
            },
            "b2b": {
                "mandatory": False,
                "description": "N/A"
            },
            "saf-t": {
                "introduced": False,
                "description": "N/A"
            },
            "integrity": "N/A",
            "buyers_consent": "N/A",
            "storage_period": "N/A",
            "platform": "N/A",
            "source": source_url,
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        }
    }

def app():
    st.title("eInvoicing JSON Generator")
    st.write("Provide a URL or text to generate the corresponding JSON.")

    option = st.radio("Choose Input Type:", ["URL", "Text"])
    
    if option == "URL":
        url = st.text_input("Enter the webpage URL:")
        if url:
            data = extract_data_from_url(url)
            if data:
                json_output = generate_json(data, url)
                st.json(json_output)
    else:
        text = st.text_area("Enter the text:")
        if text:
            json_output = generate_json(text, "Provided Text")
            st.json(json_output)

if __name__ == "__main__":
    app()