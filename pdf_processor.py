# pdf_processor.py
import io
import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def extract_text_from_pdf(pdf_file):
    resource_manager = PDFResourceManager()
    output_string = io.StringIO()
    laparams = LAParams()
    device = TextConverter(resource_manager, output_string, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)

    text = ""
    for page_num, page in enumerate(PDFPage.get_pages(pdf_file, check_extractable=True), 1):
        output_string.seek(0)
        output_string.truncate(0)

        interpreter.process_page(page)
        page_text = output_string.getvalue()

        # Remove multiple blank lines, keeping only single blank lines
        page_text = re.sub(r'\n{3,}', '\n\n', page_text)

        # Add Page number at the start of each page
        page_marker = f"🅿️ Start Page {page_num} - "
        text += page_marker + page_text

    device.close()
    output_string.close()

    return text