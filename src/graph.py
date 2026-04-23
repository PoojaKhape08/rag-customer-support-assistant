from langgraph.graph import StateGraph
from typing import TypedDict


class State(TypedDict):
    query: str
    db: object
    docs: list
    answer: str


def process_node(state):
    from src.retriever import retrieve_chunks
    from src.llm import generate_answer

    query = state["query"]
    db = state["db"]

    docs = retrieve_chunks(db, query)
    answer = generate_answer(docs, query)

    return {
        "query": query,
        "db": db,
        "docs": docs,
        "answer": answer
    }


def decision_node(state):
    query = state["query"].lower()
    docs = state["docs"]

    if not docs:
        return "human"

    context = " ".join([doc.page_content.lower() for doc in docs])

    keywords = [
        "course", "courses",
        "admission", "admissions",
        "fee", "fees",
        "hostel",
        "facility", "facilities",
        "placement",
        "exam", "examination",
        "document", "documents"
    ]

    domain_match = any(k in query for k in keywords)

    if not domain_match:
        return "human"

    common_words = ["course", "courses", "admission", "fee", "hostel"]

    if any(w in query for w in common_words):
        return "final"
        return "human"


def human_node(state):
    return {
        **state,
        "answer": "⚠️ Escalated to human support"
    }


def build_graph():
    graph = StateGraph(State)

    graph.add_node("process", process_node)
    graph.add_node("human", human_node)

    graph.set_entry_point("process")

    graph.add_conditional_edges(
        "process",
        decision_node,
        {
            "human": "human",
            "final": "__end__"
        }
    )

    graph.add_edge("human", "__end__")

    return graph.compile()
