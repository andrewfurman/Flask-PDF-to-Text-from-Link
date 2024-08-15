# pdf_processor.py

import io
import requests
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

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

def extract_text_from_pdf(pdf_file):
    resource_manager = PDFResourceManager()
    output_string = io.StringIO()
    laparams = LAParams()
    converter = TextConverter(resource_manager, output_string, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, converter)

    try:
        for page in PDFPage.get_pages(pdf_file, check_extractable=True):
            interpreter.process_page(page)
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {str(e)}")

    text = output_string.getvalue()
    converter.close()
    output_string.close()

    return text

def get_url_text(url):
    try:
        pdf_file = download_pdf(url)
        text = extract_text_from_pdf(pdf_file)
        return text
    except Exception as e:
        return f"Error processing PDF: {str(e)}"