import argparse
import json
from itertools import islice
from pyserini.index.lucene import LuceneIndexer

BATCH_SIZE = 20

def main():
    parser = argparse.ArgumentParser("Indexing corpus using BM25")
    parser.add_argument(
            "--input_file",
            type=str,
            default="./pyserini_corpus/docs.jsonl",
            help="Path to the input corpus JSONL file to index (default: ./pyserini_corpus/docs.jsonl)",
        )

    args = parser.parse_args()
    
    indexer = LuceneIndexer(args=["-index","indexes/bm25","-storePositions", "-storeDocvectors", "-storeRaw"])

    batch = []

    with open(args.input_file, "r") as f:
        for line in islice(f, 20):
            doc = json.loads(line)
            batch.append(doc)

    if batch:
        indexer.add_batch_dict(batch)

    indexer.close()

if __name__ == "__main__":
    main()

