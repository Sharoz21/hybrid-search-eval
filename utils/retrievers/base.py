from abc import ABC, abstractmethod
from pyserini.search.lucene import LuceneSearcher


class BaseRetriever(ABC):
    searcher: LuceneSearcher

    def __init__(self, searcher: LuceneSearcher) -> None:
        self.searcher = searcher

    @abstractmethod
    def search(self, query: str, top_k: int) -> list[tuple[int, float]]:
        "Ranked list of (docid, score)"
        ...

