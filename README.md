Ask My PDFs

Ask My PDFs is a Django-based Retrieval-Augmented Generation (RAG) system that enables users to upload and interact with large collections of PDFs and documents using natural language.

Unlike traditional LLMs that rely only on pre-trained knowledge, this system grounds responses in user-provided data through document retrieval and contextual generation.

The platform processes uploaded documents through an ETL pipeline, chunks and indexes them using Elasticsearch, retrieves the most relevant content during queries, and sends contextual information to Llama 3.1 via Groq to generate grounded responses.

This demo project showcases practical implementation of modern GenAI and RAG architectures, combining Django backend development, document processing, Elasticsearch indexing, retrieval pipelines, and LLM inference into a unified workflow.

Features
Multi-document PDF upload support
Natural language document querying
ETL document processing pipeline
Elasticsearch-based indexing and retrieval
Context-aware LLM responses
Chat history support
Modern Django + Tailwind UI
Multiple file upload support
RAG-based grounded answering
Tech Stack
Python
Django
Elasticsearch
Groq API
LLaMA 3.1
pdfplumber
TailwindCSS
Docker
ETL Pipelines
Retrieval-Augmented Generation (RAG)
Project Architecture
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
Installation & Setup
1. Clone Repository
git clone <your-repository-url>
cd askMyPDF
2. Create Virtual Environment
python -m venv venv

Activate virtual environment:

Windows PowerShell
.\venv\Scripts\Activate.ps1

If activation fails, recreate the virtual environment or ensure Python was installed with full PowerShell support.

3. Install Dependencies
pip install django pdfplumber pandas langchain sentence-transformers streamlit groq python-dotenv python-docx elasticsearch==8.11.0 requests
4. Configure Environment Variables

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key
5. Start Elasticsearch with Docker

Make sure Docker Desktop is running.

Run Elasticsearch:

docker run -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" elasticsearch:8.11.0

Elasticsearch should now run at:

http://localhost:9200

Check indexed data:

http://localhost:9200/docs/_search?pretty
6. Configure Django Media

Inside settings.py:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
7. Run Django Server
python manage.py runserver

Application URL:

http://127.0.0.1:8000/
Example Workflow
Upload PDFs/documents
ETL pipeline extracts text
Text is chunked and indexed into Elasticsearch
User asks a question
Relevant chunks are retrieved
Context is sent to LLaMA 3.1 via Groq
AI generates grounded response
