📄 Ask My PDFs
🧠 Overview

Ask My PDFs is a Django-based Retrieval-Augmented Generation (RAG) system that enables users to upload and interact with large collections of PDFs and documents using natural language.

Unlike traditional LLMs that rely only on pre-trained knowledge, this system grounds responses in user-provided documents using retrieval-based context.

It processes documents through an ETL pipeline, chunks and indexes them using Elasticsearch, retrieves relevant content at query time, and uses LLaMA 3.1 (via Groq API) to generate context-aware responses.

This project demonstrates a practical implementation of modern GenAI and RAG architecture using Django, Elasticsearch, and LLM inference.

✨ Features
Multi-document PDF upload support
Natural language document querying
ETL pipeline for document processing
Elasticsearch-based indexing and retrieval
Context-aware LLM responses (Groq + LLaMA 3.1)
Session-based chat history
Modern Django + Tailwind UI
Multi-file upload handling
RAG-based grounded answering
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
🏗️ Architecture
User Uploads PDFs
        ↓
ETL Document Extraction
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
Grounded Response
⚙️ Installation & Setup
1. Clone Repository
git clone <repo-url>
cd askMyPDF
2. Create Virtual Environment
python -m venv venv

Activate:

.\venv\Scripts\Activate.ps1
3. Install Dependencies
pip install django pdfplumber pandas langchain sentence-transformers streamlit groq python-dotenv python-docx elasticsearch==8.11.0 requests
4. Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
5. Run Elasticsearch (Docker)
docker run -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" elasticsearch:8.11.0

Check:

http://localhost:9200/docs/_search?pretty
6. Django Settings
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
7. Run Server
python manage.py runserver

Open:

http://127.0.0.1:8000/
🔁 Workflow
Upload PDFs
→ ETL Processing
→ Chunking
→ Elasticsearch Indexing
→ Query Input
→ Retrieval of Relevant Chunks
→ LLaMA 3.1 Response Generation
📌 Notes
This is a demo RAG system
Focuses on grounding LLM responses in user documents
Not a production deployment
