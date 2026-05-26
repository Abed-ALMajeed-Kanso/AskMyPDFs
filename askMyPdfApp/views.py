from django.shortcuts import render, redirect
from django.conf import settings
import os

from .forms import PDFUploadForm
from .services.pdf_service import handle_upload


def home(request):
    form = PDFUploadForm()
    chat = request.session.get("chat_history", [])

    upload_error = request.session.pop("upload_error", None)
    upload_success = request.session.pop("upload_success", None)

    if request.method == "POST":

        if request.POST.get("clear_chat"):
            request.session["chat_history"] = []
            request.session.modified = True
            return redirect("home")

        elif request.FILES:
            form = PDFUploadForm(request.POST, request.FILES)
            files = request.FILES.getlist("file")

            if not files:
                files = list(request.FILES.values())

            if files:
                MAX_FILES = 30
                MAX_TOTAL = 55 * 1024 * 1024

                total_size = sum(f.size for f in files)

                if len(files) > MAX_FILES:
                    request.session["upload_error"] = f"Upload limit exceeded: maximum {MAX_FILES} files."
                    request.session["upload_success"] = None

                elif total_size > MAX_TOTAL:
                    request.session["upload_error"] = "Total upload size exceeds 55 MB. Please upload fewer or smaller files."
                    request.session["upload_success"] = None

                else:
                    handle_upload(files)
                    request.session["upload_success"] = f"Uploaded {len(files)} file(s)."
                    request.session["upload_error"] = None

            else:
                request.session["upload_error"] = "No files were uploaded. Please select one or more files."
                request.session["upload_success"] = None

            return redirect("home")

        elif "question" in request.POST:
            from .services.rag_service import ask_question

            question = request.POST["question"]
            answer = ask_question(question)

            chat.append({
                "question": question,
                "answer": answer
            })

            request.session["chat_history"] = chat
            request.session.modified = True

            return redirect("home")

    return render(request, "askMyPdfApp/home.html", {
        "form": form,
        "chat": chat,
        "upload_error": upload_error,
        "upload_success": upload_success
    })


def manage_files(request):
    from .services.elastic_service import delete_by_source
    
    upload_dir = os.path.join(settings.MEDIA_ROOT, "pdfs")
    os.makedirs(upload_dir, exist_ok=True)

    message = None

    if request.method == 'POST':
        selected = request.POST.getlist('selected')
        deleted = []

        for name in selected:
            safe_name = os.path.basename(name)
            target = os.path.join(upload_dir, safe_name)

            if os.path.exists(target) and os.path.isfile(target):
                try:
                    # Remove from filesystem
                    os.remove(target)
                    # Remove indexed documents from Elasticsearch
                    delete_by_source(safe_name)
                    deleted.append(safe_name)
                except Exception as e:
                    print(f"Failed to delete {safe_name}: {e}")
                    continue

        message = f"Deleted {len(deleted)} file(s)."

    files = []

    for fname in sorted(os.listdir(upload_dir)):
        full = os.path.join(upload_dir, fname)

        if os.path.isfile(full):
            size = os.path.getsize(full)

            files.append({
                'name': fname,
                'size': size,
                'size_kb': round(size / 1024.0, 2)
            })

    return render(request, 'askMyPdfApp/manage_files.html', {
        'files': files,
        'message': message,
        'media_url': settings.MEDIA_URL + 'pdfs/'
    })