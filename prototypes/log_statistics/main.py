from collections import Counter
from sample_data import logs

level_counts = Counter(log["Level"] for log in logs)

print(f"Total Entries: {len(logs)}\n")

print("Severity Counts:")
for level, total in level_counts.items():
    print(f"{level} -> {total}")

error_logs = [
    log for log in logs
    if log["Level"] == "ERROR"
]

print(f"\nTotal Errors: {len(error_logs)}")
for log in error_logs:
    print(f'{log["Timestamp"]} -> {log["Message"]}')

message_counts = Counter(
    log["Message"] for log in logs
)

print("\nMost Common Messages:")
for message, total in message_counts.most_common():
    print(f"{message} -> {total}")

print("\nSeverity Counts (Highest to Lowest):")
for level, total in level_counts.most_common():
    print(f"{level} -> {total}")

total_entries = len(logs)
error_count = level_counts["ERROR"]

if total_entries > 0:
    error_percentage = (error_count / total_entries) * 100
else:
    error_percentage = 0

print(f"\nError Percentage: {error_percentage:.2f}%")