from utils.retrievers.bm25 import BM25Retriever

ranked_docs = BM25Retriever("./indexes/bm25").search("myelodysplasia", 5)

for doc in ranked_docs:
    print(f"doc_id: {doc[0]} score: {doc[1]:.3f}")
