📄 Ask My PDFs

Ask My PDFs is a Django-based Retrieval-Augmented Generation (RAG) system that allows users to upload and interact with large collections of PDFs and documents using natural language.

Unlike traditional LLMs that rely only on pre-trained knowledge, this system grounds responses in user-provided documents using retrieval-based context injection.

It processes documents through an ETL pipeline, chunks and indexes them in Elasticsearch, retrieves relevant content at query time, and uses LLaMA 3.1 (via Groq API) to generate accurate, context-aware responses.

This project demonstrates a practical implementation of modern GenAI and RAG architectures using Django, Elasticsearch, and LLM inference in a unified workflow.

🚀 Features
📚 Multi-document PDF upload support
💬 Natural language document querying
⚙️ ETL pipeline for document processing
🔎 Elasticsearch-based indexing and retrieval
🧠 Context-aware LLM responses (Groq + LLaMA 3.1)
💾 Session-based chat history
🎨 Modern Django + Tailwind CSS UI
📂 Multi-file upload handling
🔗 RAG-based grounded answering system
🧰 Tech Stack
Python
Django
Elasticsearch
Groq API
LLaMA 3.1
pdfplumber
Tailwind CSS
Docker
ETL Pipelines
Retrieval-Augmented Generation (RAG)
🏗️ System Architecture
User Uploads PDFs
        ↓
Document Extraction (ETL)
        ↓
Text Chunking
        ↓
Elasticsearch Indexing
        ↓
User Question
        ↓
Relevant Chunk Retrieval
        ↓
LLaMA 3.1 via Groq
        ↓
Grounded AI Response
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone <your-repo-url>
cd askMyPDF
2️⃣ Create virtual environment
python -m venv venv

Activate (Windows PowerShell):

.\venv\Scripts\Activate.ps1

If activation fails, reinstall Python with “Add to PATH” and PowerShell support enabled.

3️⃣ Install dependencies
pip install django pdfplumber pandas langchain sentence-transformers streamlit groq python-dotenv python-docx elasticsearch==8.11.0 requests
4️⃣ Configure environment variables

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key
5️⃣ Start Elasticsearch (Docker)

Make sure Docker Desktop is running, then:

docker run -p 9200:9200 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  elasticsearch:8.11.0

Elasticsearch will be available at:

http://localhost:9200

Check indexed data:

http://localhost:9200/docs/_search?pretty
6️⃣ Configure Django media settings
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
7️⃣ Run the server
python manage.py runserver

Open:

http://127.0.0.1:8000/
🔁 Example Workflow
User uploads PDFs/documents
ETL pipeline extracts text
Text is chunked and indexed into Elasticsearch
User asks a question
Relevant chunks are retrieved
Context is sent to LLaMA 3.1 via Groq API
Model generates grounded response
📌 Notes
This is a demo RAG system, not a production-grade deployment
Designed for educational and portfolio purposes
Performance depends on Elasticsearch indexing and chunk quality
