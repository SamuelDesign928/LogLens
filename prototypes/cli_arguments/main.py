import argparse

parser = argparse.ArgumentParser(
    description="Experiment with command-line arguments"
)

parser.add_argument("filename")
parser.add_argument(
    "--level",
    choices=["INFO", "WARNING", "ERROR"],
    default="INFO"
)
parser.add_argument("--output")

args = parser.parse_args()

print(f"Input file: {args.filename}")
print(f"Severity filter: {args.level}")
print(f"Report file: {args.output}")