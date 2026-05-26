from django.conf import settings
import os
from .etl_service import process_document


def handle_upload(files):
    if not isinstance(files, (list, tuple)):
        files = [files]

    upload_dir = os.path.join(settings.MEDIA_ROOT, "pdfs")
    os.makedirs(upload_dir, exist_ok=True)

    saved_paths = []
    for file in files:
        file_name = os.path.basename(file.name)
        file_path = os.path.join(upload_dir, file_name)

        with open(file_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        saved_paths.append(file_path)

    for file_path in saved_paths:
        # Process based on document type (PDF, TXT, DOCX). Others are saved but not processed.
        try:
            print(f"Processing uploaded file: {file_path}")
            process_document(file_path)
            print(f"Finished processing: {file_path}")
        except Exception as e:
            print(f"Document processing failed for {file_path}: {e}")
            continue
