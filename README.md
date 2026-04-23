#  RAG-Based Customer Support Assistant

An AI-powered Customer Support Assistant built using **Retrieval-Augmented Generation (RAG)** with **LangGraph workflow orchestration** and **Human-in-the-Loop (HITL)** support.

---

##  Project Overview

This project implements an intelligent customer support system that:
- Processes a PDF knowledge base
- Retrieves relevant information using vector embeddings
- Generates context-aware responses using an LLM
- Uses a graph-based workflow for decision-making
- Escalates queries to humans when confidence is low

---

##  Key Features

🔹 PDF Document Processing  
🔹 Intelligent Text Chunking  
🔹 Semantic Embeddings Generation  
🔹 Vector Database (ChromaDB)  
🔹 Context-Aware Answer Generation (LLM)  
🔹 LangGraph Workflow Execution  
🔹 Conditional Routing Logic  
🔹 Human-in-the-Loop (HITL) Escalation  

---

##  System Architecture

The system consists of two main pipelines:

###  Document Ingestion Pipeline
- Load PDF  
- Chunk text  
- Generate embeddings  
- Store in ChromaDB  

###  Query Processing Pipeline
- Accept user query  
- Retrieve relevant chunks  
- Generate response using LLM  
- Apply decision logic  
- Return answer or escalate  

---

##  Tech Stack

| Component | Technology |
|----------|-----------|
| Language | Python |
| Framework | LangChain |
| Workflow | LangGraph |
| Vector DB | ChromaDB |
| LLM | OpenAI / Gemini |
| Data Source | PDF |

---

##  Project Structure
rag-customer-support-assistant/
│
├── src/
│ ├── loader.py
│ ├── chunker.py
│ ├── embeddings.py
│ ├── retriever.py
│ ├── graph.py
│ ├── llm.py
│
├── data/
│ └── sample.pdf
│
├── main.py
├── requirements.txt
│
├── HLD.pdf
├── LLD.pdf
├── Technical_Documentation.pdf
│
└── README.md


---

##  How to Run

### 1️ Install Dependencies

pip install -r requirements.txt

### 2️ Run the Application

python main.py

### demo / screenshot
<img width="1919" height="997" alt="image" src="https://github.com/user-attachments/assets/073117f4-bece-491e-8712-2eacead3a4c0" />

### Sample Queries
What is the refund policy?
How can I apply for admission?
What documents are required?

### Workflow (LangGraph)
Input Query → Processing Node
Retrieval → LLM Generation
Confidence Check → Decision
Output OR HITL Escalation

### Key Concepts Used
Retrieval-Augmented Generation (RAG)
Vector Similarity Search
Graph-based Workflow (LangGraph)
Human-in-the-Loop (HITL)

### Challenges & Trade-offs
Accuracy vs Speed
Chunk Size vs Context Quality
Cost vs Performance

### Future Enhancements
Multi-document support
Conversational memory
Feedback-based learning
Web application deployment
