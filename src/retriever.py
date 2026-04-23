def retrieve_chunks(db, query):
    return db.similarity_search(query, k=3)
