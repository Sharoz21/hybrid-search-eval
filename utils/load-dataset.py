import json

with open("./dataset/corpus/corpus.jsonl") as f:
    dataset = [json.loads(line) for line in f]

