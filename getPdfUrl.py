# getPdfUrl.py

import io
import requests
from pdf_processor import extract_text_from_pdf

def download_pdf(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', '').lower()
        if 'application/pdf' not in content_type:
            raise ValueError(f"URL does not point to a PDF. Content-Type: {content_type}")
        return io.BytesIO(response.content)
    except requests.RequestException as e:
        raise Exception(f"Error downloading PDF: {str(e)}")

def get_url_text(url):
    try:
        pdf_file = download_pdf(url)
        text = extract_text_from_pdf(pdf_file)
        return text
    except Exception as e:
        return f"Error processing PDF: {str(e)}"