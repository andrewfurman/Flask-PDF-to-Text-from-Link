from pdfminer.high_level import extract_text
import io
from urllib.request import urlopen

def extract_text_from_pdf_url(pdf_url):
    try:
        # Open the URL and read the PDF content
        with urlopen(pdf_url) as response:
            pdf_content = response.read()

        # Create a BytesIO object from the PDF content
        pdf_file = io.BytesIO(pdf_content)

        # Extract text from PDF
        text = extract_text(pdf_file)

        return text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"