from pathlib import Path

file = Path("logs/sample.log")
entry = file.read_text().splitlines()

entry_lis = {}
error_total = {}


for line in entry:
    words = line.split()

    log_template = {
        "Timestamp": " ".join(words[:2]),
        "Level": words[2],
        "Message": " ".join(words[3:])
    }

    level = log_template["Level"]

    if level not in entry_lis:
        entry_lis[level] = []

    entry_lis[level].append({
        "Timestamp": log_template["Timestamp"],
        "Message": log_template["Message"]
    })

    error_total[level] = error_total.get(level, 0) + 1

total_entries = sum(error_total.values())
print(f"Total Enteries{total_entries}\n")

for key, value in error_total.items():
    print(f"{key} -> {value}")

print("\n")

for level, logs in entry_lis.items():
    print(f"\n{level} messages:")

    for log in logs:
        print(f'{log["Timestamp"]} -> {log["Message"]}')
