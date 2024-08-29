# pdf_processor.py
import io
import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page_num, page in enumerate(reader.pages, 1):
        page_text = page.extract_text()

        # Remove multiple blank lines, keeping only single blank lines
        page_text = re.sub(r'\n{3,}', '\n\n', page_text)

        # Add Page number at the start of each page
        page_marker = f"🅿️ Start Page {page_num} - "
        text += page_marker + page_text + "\n"

    return text