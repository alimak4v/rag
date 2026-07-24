<div align="center">

# RAG

**A minimal local RAG assistant with semantic memory.**

Python · Qdrant · Sentence Transformers · OpenAI API

</div>

## Overview

RAG is a lightweight command-line assistant that stores facts locally and retrieves relevant memories before generating an answer. Retrieved context is used only when it helps answer the current question.

```text
Question → Embedding → Qdrant search → Relevant memory → LLM response
```

## Stack

| Component | Purpose |
|---|---|
| **Python 3.12+** | Application logic |
| **Qdrant** | Local vector storage and similarity search |
| **Sentence Transformers** | Multilingual text embeddings |
| **OpenAI API** | Streaming answer generation |
| **uv** | Fast dependency and environment management |

## Quick start

```bash
git clone https://github.com/alimak4v/rag.git
cd rag
uv sync
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=your_model
# OPENAI_BASE_URL=https://your-endpoint.example/v1
```

Run the assistant:

```bash
uv run main.py
```

> The embedding model is downloaded automatically on the first launch. Vector data is stored locally in `./knowledge`.
