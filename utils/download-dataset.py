from datasets import load_dataset
import os

ds = load_dataset("BeIR/scifact", "corpus")

os.makedirs("./dataset/corpus", exist_ok=True)

ds["corpus"].to_json("./dataset/corpus/corpus.jsonl")