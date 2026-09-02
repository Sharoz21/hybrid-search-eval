import argparse
import os
from datasets import load_dataset


def main():
    parser = argparse.ArgumentParser(
        description="Download and save BeIR SciFact dataset splits as JSONL."
    )
    parser.add_argument(
        "--split",
        type=str,
        default="corpus",
        choices=["corpus", "queries", "qrels"],
        help="Dataset split to download (default: corpus)",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="./dataset",
        help="Directory where the output JSONL file will be saved (default: ./dataset)",
    )

    args = parser.parse_args()

    print(f"Loading BeIR/scifact split: '{args.split}'...")
    ds = load_dataset("BeIR/scifact", args.split)

    target_dir = os.path.join(args.output_dir, args.split)
    os.makedirs(target_dir, exist_ok=True)

    output_path = os.path.join(args.output_dir, f"{args.split}.jsonl")
    print(f"Saving to {output_path}...")
    ds[args.split].to_json(output_path)
    print("Done!")


if __name__ == "__main__":
    main()