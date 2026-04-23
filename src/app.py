from fastapi import FastAPI
from src.rag_pipeline import build_rag_pipeline
from src.graph import build_graph

# FastAPI app
app = FastAPI()

# Build vector DB (PDF load + embeddings + Chroma)
db = build_rag_pipeline("data/college_support_data.pdf")

# Build LangGraph workflow
app_graph = build_graph()


# Root route (optional but good for testing)
@app.get("/")
def home():
    return {"message": "RAG API is running 🚀"}


# Ask API
@app.get("/ask")
def ask(query: str):
    result = app_graph.invoke({
        "query": query,
        "db": db
    })

    # format answer (new lines proper display sathi)
    formatted = result["answer"].replace("\n", "<br>")

    return {
    "query": query,
    "answer": result["answer"].split("\n")
}
