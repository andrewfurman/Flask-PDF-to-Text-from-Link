# PDF Link Analyzer

This is a web application that allows users to input a URL to a PDF document and extract all the text from it using the PDFMiner library.

## Usage

1. Enter a valid URL to a PDF document in the input field.
2. Click the "Process PDF" button.
3. The extracted text from the PDF will be displayed in the output area.

## PDF Processor

The `pdf_processor.py` file contains a function `extract_text_from_pdf_url(pdf_url)` that:

1. Receives a URL to a PDF document as input.
2. Downloads the PDF content from the provided URL.
3. Uses the PDFMiner library to extract all text from the PDF.
4. Returns the extracted text as a string.

## License

This project is open-source and available under the MIT License.

Default PDF Link: https://www.medicare.gov/Pubs/pdf/12026-Understanding-Medicare-Advantage-Plans.pdf