from datetime import datetime
from pathlib import Path

# Checks if the data entered is a valid date in correct format
def valDate(string):
        try:
            datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False


def parse_line(line):
    line = line.strip()
    if not line: return None
    parts = line.split(maxsplit=3)

    # Requires timestamp, level and message
    if len(parts) < 4:
        raise ValueError("Log entry has missing fields")

    # Checks severity level
    if parts[2] not in ("DEBUG", "NOTICE", "CRITICAL", "ALERT", "EMERGANCY", "ERROR", "INFO", "WARNING"):
        raise ValueError("Invalid severity level")

    # Validate timestamp and gets message
    timestamp = " ".join(parts[:2])
    if not valDate(timestamp):
        raise ValueError("Invalid timestamp")
    message = " ".join(parts[3:])
    if not message:
        raise ValueError("Missing message")

    # Return only a validated log entry
    log_template = {
        "Timestamp": timestamp,
        "Level": parts[2],
        "Message": message
    }

    return log_template


def process_file(path):
    valid = []
    malformed = []

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                result = parse_line(line)
                if result is not None:
                    valid.append(result)
            except ValueError as e:
                malformed.append({"Line" : line.rstrip("\n"),
                                  "Reason" : str(e)})
    return valid, malformed



"""
test_lines = [
    "2026-10-12 09:15:23 INFO Application started",
    "2026-13-12 09:15:23 INFO Application started",
    "2026-10-12 09:15:23 DEBUG Debugging enabled",
    "2026-10-12 09:15:23 INFO"
]

for line in test_lines:
    try:
        print(parse_line(line))
    except ValueError as e:
        print(f"Malformed line: {e}")
"""