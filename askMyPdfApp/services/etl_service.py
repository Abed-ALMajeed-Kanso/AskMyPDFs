import os
import pdfplumber

from .chunk_service import chunk_text
from .elastic_service import index_chunk


def _process_text_and_index(text, meta=None):
    """
    1. chunk text
    2. index each chunk separately
    """
    meta = meta or {}

    if not text:
        print(f"No text extracted for {meta.get('source')}. Skipping indexing.")
        return []

    chunks = chunk_text(text)
    if not chunks:
        print(f"No text chunks created for {meta.get('source')}. Skipping indexing.")
        return []

    print(f"Indexing {len(chunks)} text chunk(s) for {meta.get('source')}." )
    index_chunk(chunks, meta=meta)

    return chunks


def process_pdf(file_path):
    full_text = ""

    with pdfplumber.open(file_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            if text:
                full_text += text + "\n"
            print(f"Extracted {len(text)} chars from page {page_number} of {os.path.basename(file_path)}")

    return _process_text_and_index(
        full_text,
        meta={"source": os.path.basename(file_path)}
    )


def process_txt(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    return _process_text_and_index(
        text,
        meta={"source": os.path.basename(file_path)}
    )


def process_docx(file_path):
    try:
        import docx
    except Exception as e:
        print(f"DOCX processing unavailable for {file_path}: {e}")
        return []

    try:
        doc = docx.Document(file_path)
        text = "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        print(f"Failed to extract text from DOCX {file_path}: {e}")
        return []

    return _process_text_and_index(
        text,
        meta={"source": os.path.basename(file_path)}
    )


def process_document(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return process_pdf(file_path)
    elif ext == ".txt":
        return process_txt(file_path)
    elif ext == ".docx":
        return process_docx(file_path)

    print(f"Unsupported file extension '{ext}' for {file_path}. Skipping document processing.")
    return []