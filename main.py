from src.rag_pipeline import build_rag_pipeline
from src.graph import build_graph

def main():
    db = build_rag_pipeline("data/college_support_data.pdf")

    app = build_graph()

    while True:
        query = input("\nAsk question: ")

        if query.lower() == "exit":
            break

        result = app.invoke({
            "query": query,
            "db": db
        })

        print("\nAnswer:\n", result["answer"])


if __name__ == "__main__":
    main()
