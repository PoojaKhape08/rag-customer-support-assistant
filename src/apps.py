from fastapi import FastAPI
from src.rag_pipeline import build_rag_pipeline
from src.graph import build_graph

# FastAPI app
app = FastAPI()

# Build vector DB (PDF load + embeddings + Chroma)
db = build_rag_pipeline("data/college_support_data.pdf")

# Build LangGraph workflow
app_graph = build_graph()



@app.get("/")
def home():
    return {"message": "RAG API is running 🚀"}



@app.get("/ask")
def ask(query: str):
    result = app_graph.invoke({
        "query": query,
        "db": db
    })

   
    formatted = result["answer"].replace("\n", "<br>")

    return {
    "query": query,
    "answer": result["answer"].split("\n")
}
