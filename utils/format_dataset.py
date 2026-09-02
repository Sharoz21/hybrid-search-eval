import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser(
        description="Format BeIR SciFact dataset for Pyserini indexing."
    )

    parser.add_argument(
        "--input_file",
        type=str,
        default="./dataset/corpus.jsonl",
        help="Path to the input corpus JSONL file (default: ./dataset/corpus.jsonl)",
    )

    parser.add_argument(
        "--output_file",
        type=str,
        default="./pyserini_corpus/docs.jsonl",
        help="Path where formatted output file will be saved (default: ./pyserini_corpus/docs.jsonl)",
    )

    args = parser.parse_args()
    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)

    with open(args.input_file, "r") as fin, open(args.output_file, "w") as fout:
        for line in fin:
            doc = json.loads(line)

            title = doc.get("title", "")
            text = doc.get("text", "")

            formatted_doc = {
                "id": doc["_id"],
                "contents": f"Title: {title} \n {text}".strip(),
            }

            fout.write(json.dumps(formatted_doc) + "\n")

    print(f"Formatted corpus saved to {args.output_file}")


if __name__ == "__main__":
    main()