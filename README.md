# Local Semantic Search & RAG

A local Retrieval-Augmented Generation (RAG) application built with Python. The project combines semantic search, document chunking, vector storage, and a locally running language model to answer questions using a custom knowledge base.

## Overview

This project explores how to build a RAG pipeline from its core components rather than relying entirely on a high-level framework.

Documents are loaded and split into overlapping chunks. Each chunk is converted into an embedding, stored in a vector index, and retrieved according to its semantic similarity to a user's question. The most relevant chunks are then supplied to a language model to generate a context-grounded answer.

The project also includes evaluation utilities for checking answer quality and identifying claims that are not supported by the retrieved context.

## Features

- **Local embeddings:** Generate text embeddings using Sentence Transformers.
- **Semantic search:** Retrieve conceptually relevant content using embedding similarity.
- **Document chunking:** Split documents into smaller passages with configurable overlap.
- **Vector storage:** Use ChromaDB to store and retrieve document embeddings.
- **Local LLM generation:** Use Ollama to run a language model locally.
- **RAG pipeline:** Generate answers using relevant passages from the knowledge base.
- **Answer evaluation:** Evaluate generated answers against retrieved evidence and detect unsupported claims.
- **Automated tests:** Test core functionality and evaluation components.

## Architecture

```text
User question
     |
     v
Query embedding
     |
     v
Vector similarity search
     |
     v
Top relevant document chunks
     |
     v
Context + user question
     |
     v
Local language model (Ollama)
     |
     v
Generated answer
     |
     v
Evaluation against retrieved context
```

### Indexing pipeline

```text
Source documents
      |
      v
Text extraction / loading
      |
      v
Chunking with overlap
      |
      v
Embedding generation
      |
      v
ChromaDB vector storage
```

## Technology Stack

- Python
- Sentence Transformers
- NumPy
- ChromaDB
- Ollama
- Pydantic
- Python unittest framework

## Project Structure

```text
project-02-semantic-search/
├── documents/               # Sample knowledge-base documents
├── chroma_db/               # Locally generated vector database
├── main.py                  # Application entry point
├── embeddings.py            # Embedding generation
├── chunking.py              # Text chunking
├── similarity.py            # Similarity calculation
├── index.py                 # Index construction
├── search.py                # Semantic retrieval
├── vector_store.py          # Vector storage integration
├── generator.py              # LLM answer generation
├── evaluator.py              # Answer evaluation
├── evaluation.py             # Evaluation functionality
├── evaluation_generation.py  # Generation-related evaluation
├── evaluation_models.py      # Evaluation data models
├── test_evaluator.py         # Evaluator tests
├── requirements.txt          # Python dependencies
├── .gitignore
└── README.md
```

Generated database files may be created at runtime and are not required to be committed if the index can be rebuilt from the source documents.

## Requirements

- Python
- Ollama installed and running locally
- The embedding model used by `embeddings.py`
- The generation model configured in `generator.py`

The application uses local models, so an OpenAI API key is not required for this configuration.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Derobm-code/PROJECT_2_SEMANTIC_SEARCH.git
cd project-02-semantic-search
```

Replace the repository URL with the URL of this GitHub project.

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Prepare Ollama

Start Ollama and download the language model configured in `generator.py`.

For example, if the project uses Qwen3 1.7B:

```bash
ollama pull qwen3:1.7b
```

If a different model is configured in the source code, download that model instead.

### 5. Run the application

```bash
python main.py
```

Enter a question related to the documents in the knowledge base. The application should retrieve relevant passages and use them to generate an answer.

## Evaluation

The project includes evaluation code for assessing the relationship between generated answers and retrieved evidence.

The evaluation process is intended to examine:

- Whether an answer addresses the question.
- Whether its claims are covered by the available context.
- Whether claims are supported by the retrieved evidence.
- Whether unsupported statements can be detected.

Run the evaluation entry point implemented in the repository. The current source files include `evaluation.py`, `evaluation_generation.py`, and `test_evaluator.py`; use the command corresponding to the combined evaluator in the current version.

## Limitations

- Retrieval quality depends on document coverage, chunk size, chunk overlap, and the embedding model.
- A relevant retrieved passage does not guarantee a correct generated answer.
- Local language-model performance and speed depend on available hardware.
- Evaluation results depend on the evaluation criteria and test cases.
- This is a learning and portfolio project, not a production-ready knowledge-management service.

## Future Improvements

- Add a user interface for document upload and question answering.
- Improve retrieval evaluation with a representative test dataset.
- Add source citations to generated answers.
- Improve document ingestion and index persistence.
- Add logging, latency measurements, and deployment support.

## Learning Objectives

This project demonstrates practical experience with embeddings, semantic retrieval, vector storage, chunking, local LLM integration, RAG architecture, and evaluation of grounded generation.