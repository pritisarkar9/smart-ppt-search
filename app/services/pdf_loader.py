import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str) -> list[str]:
    """
    Extract text from each page of a PDF.
    Returns a list where each item = one page's text
    """
    doc = fitz.open(pdf_path)
    pages_text = []

    for page_num, page in enumerate(doc):
        text = page.get_text()
        pages_text.append(text.strip())

    doc.close()
    return pages_text
