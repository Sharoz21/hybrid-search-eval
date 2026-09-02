from .base import BaseRetriever
from pyserini.search.lucene import LuceneSearcher

class BM25Retriever(BaseRetriever):
    def __init__(self, index_path: str, k1: float = 0.9) -> None:
        searcher = LuceneSearcher(index_path)
        searcher.set_bm25(k1)
        super().__init__(searcher)

    def search(self, query: str, top_k: int) -> list[tuple[int, float]]:
        hits = self.searcher.search(query, top_k)
        return [(hit.docid, hit.score) for hit in hits]


    