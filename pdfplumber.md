# pdf_processor.py
import io
import pdfplumber

def extract_text_from_pdf(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            page_text = page.extract_text()

            # Add Page number marker on its own line
            page_marker = f"\n🅿️ Start Page {page_num}\n"
            text += page_marker + page_text + "\n"

    return text