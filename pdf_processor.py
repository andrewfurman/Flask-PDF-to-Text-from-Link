import io
import pdfplumber

def format_markdown_table(table):
    if not table:
        return ""

    # Calculate the maximum width for each column
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(*table)]

    # Format the header
    header = "| " + " | ".join(str(cell).ljust(width) for cell, width in zip(table[0], col_widths)) + " |"
    separator = "|" + "|".join("-" * 3 for _ in col_widths) + "|"  # Changed to use single dashes

    # Format the rows
    rows = []
    for row in table[1:]:
        formatted_row = "| " + " | ".join(str(cell).ljust(width) for cell, width in zip(row, col_widths)) + " |"
        rows.append(formatted_row)

    # Combine all parts
    return "\n".join([header, separator] + rows) + "\n"

def extract_text_from_pdf(pdf_file):
    text = ""

    def process_pdf(pdf):
        nonlocal text
        for page_num, page in enumerate(pdf.pages, 1):
            # Add Page number marker
            page_marker = f"\n🅿️ Start Page {page_num}\n"
            text += page_marker

            # Extract tables from the page
            tables = page.extract_tables()

            if tables:
                for table in tables:
                    # Use our custom function to format the table
                    markdown_table = format_markdown_table(table)
                    text += "\n" + markdown_table + "\n"

            # Extract and add remaining text
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # Check if pdf_file is a BytesIO object
    if isinstance(pdf_file, io.BytesIO):
        pdf_file.seek(0)  # Ensure we're at the start of the stream
        with pdfplumber.open(pdf_file) as pdf:
            process_pdf(pdf)
    else:
        # If it's not a BytesIO object, assume it's a file path
        with pdfplumber.open(pdf_file) as pdf:
            process_pdf(pdf)

    return text