import pymupdf as fitz  # Correct import

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    text = ""

    # Loop through all the pages and extract text
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    return text

# Example usage
pdf_path = "CV.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
print(pdf_text)
