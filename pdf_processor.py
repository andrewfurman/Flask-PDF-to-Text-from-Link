# pdf_processor.py

import io
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

    for page in PDFPage.get_pages(pdf_file, check_extractable=True):
        interpreter.process_page(page)

    text = output_string.getvalue()

    device.close()
    output_string.close()

    return text