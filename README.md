# 🔎 Semantic Search using Sentence Transformers

![Python](https://img.shields.io/badge/Python-3.x-blue)
![NLP](https://img.shields.io/badge/Task-Semantic_Search-green)
![Embeddings](https://img.shields.io/badge/Embeddings-Sentence_Transformers-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project implements a **Semantic Search System** using Sentence Transformers.

Unlike keyword-based search, semantic search understands the **meaning** of text and retrieves contextually relevant documents.

---

## 📌 Project Overview

Traditional search methods rely on keyword matching.

Semantic search uses:

- Sentence embeddings
- Vector similarity (cosine similarity)
- Context-aware retrieval

This allows the system to retrieve documents even when exact words do not match.

---

## 🎯 Objective

The goal of this project is to:

✅ Convert documents into vector embeddings  
✅ Store embeddings in memory  
✅ Compare query embeddings with document embeddings  
✅ Retrieve the most semantically similar document  

---

## 🧠 How It Works


Documents
↓
Sentence Transformer Model
↓
Vector Embeddings
↓
User Query
↓
Cosine Similarity
↓
Most Relevant Document


---

## 📂 Project Structure


Semantic_Search/
│
├── semantic_search.py
└── README.md


---

## ⚙️ Technologies Used

- Python 🐍  
- Sentence Transformers  
- PyTorch  
- Cosine Similarity  

---

## ▶️ Installation

```bash
pip install sentence-transformers torch
▶️ Run the Project
python semantic_search.py
💬 Example

Query:

AI changing industries

Output:

Artificial Intelligence is transforming industries.

Even without exact word match, the system understands the meaning.

🚀 Learning Outcomes

By completing this project, you will:

✔ Understand text embeddings
✔ Learn semantic similarity
✔ Build context-aware search systems
✔ Understand foundation of RAG systems

🌍 Real-World Applications

Semantic search is used in:

AI search engines

Document retrieval systems

ChatGPT-style retrieval

Recommendation systems

Enterprise knowledge assistants

👨‍💻 Author

Harsh Chauhan
AI & Data Science Enthusiast
