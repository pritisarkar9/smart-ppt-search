from app.services.pdf_loader import extract_text_from_pdf

def search_pdf(query: str):
    pdf_path = "data/pdfs/sample.pdf"
    pages = extract_text_from_pdf(pdf_path)

    # Later: generate embeddings + FAISS search
    return [
        {"page_no": i + 1, "text": page[:200]}
        for i, page in enumerate(pages)
        if query.lower() in page.lower()
    ]
