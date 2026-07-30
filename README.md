# Ask My PDFs

## Overview

Ask My PDFs is a Django-based Retrieval-Augmented Generation (RAG) system that enables users to upload and interact with large collections of PDF and document files using natural language.

Unlike traditional LLM systems that rely only on pre-trained knowledge, this system grounds responses in user-provided documents through a retrieval-based pipeline.

Documents are processed using an ETL workflow, chunked, and indexed into Elasticsearch. At query time, the system retrieves the most relevant segments and sends them to LLaMA 3.1 (via Groq) to generate grounded, context-aware responses.

This project demonstrates a practical implementation of modern GenAI systems combining Django backend development, document processing, search infrastructure, and LLM inference in a unified RAG architecture.

## Features

- Multi-document PDF upload support  
- Natural language document querying  
- ETL pipeline for document processing  
- Elasticsearch-based indexing and retrieval  
- Context-aware LLM responses using Groq (LLaMA 3.1)  
- Session-based chat history  
- Modern TailwindCSS frontend  
- Multi-file upload support  
- RAG-based grounded answering  

## Tech Stack

- Python  
- Django  
- Elasticsearch  
- Groq API  
- LLaMA 3.1  
- pdfplumber  
- TailwindCSS  
- Docker  
- ETL pipelines  
- Retrieval-Augmented Generation (RAG)  

## Architecture

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
LLaMA 3.1 (Groq)  
↓  
Grounded AI Response  

## Notes
Demo RAG system (not production-ready)
Uses Elasticsearch instead of vector database
Session-based chat history
Groq used for fast LLM inference

## Summary

A lightweight end-to-end RAG system built with Django, Elasticsearch, and LLMs, focused on grounded document-based question answering over large-scale user-provided data.
