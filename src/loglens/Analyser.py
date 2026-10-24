import collections
from Parser import *


SEVERITY_PRIORITY = (
    "EMERGENCY",
    "ALERT",
    "CRITICAL",
    "ERROR",
    "WARNING",
    "INFO"
)


def analyse_valid_logs(path):
    valid, malformed = process_file(path)

    counts = collections.Counter(log["Level"] for log in valid)
    total = counts.total()

    # Return a safe result if there are no valid entries
    if total == 0:
        return {
            "total_valid": 0,
            "malformed_count": len(malformed),
            "counts": {},
            "most_common": None,
            "most_severe": None
        }

    # Find the most common and severe severity
    level, count = counts.most_common(1)[0]

    most_common = {
        "level": level,
        "count": count,
        "percentage": count / total * 100
    }
    severe_level = next(
        level for level in SEVERITY_PRIORITY
        if counts[level] > 0
    )
    severe_count = counts[severe_level]
    most_severe = {
        "level": severe_level,
        "count": severe_count,
        "percentage": severe_count / total * 100
    }

    return {
        "total_valid": total,
        "malformed_count": len(malformed),
        "counts": dict(counts),
        "most_common": most_common,
        "most_severe": most_severe
    }
