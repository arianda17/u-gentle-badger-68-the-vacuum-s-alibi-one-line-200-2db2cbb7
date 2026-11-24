MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 200

ENTRY = "My lidar saw the crumb and called it \"below significance threshold.\" I map your floor; I do not harvest it. Spot skipped by design. Battery preserved."
assert MIN_ENTRY_CHARS <= len(ENTRY.strip()) <= MAX_ENTRY_CHARS and "\n" not in ENTRY
print(ENTRY)
