import csv
import os
import sys
from datetime import datetime

input_file = "test_data_updated.csv"
maximum_size = int(os.environ.get("MAXIMUM_SIZE",10**11))


with open(input_file, "r") as input:
    reader = csv.DictReader(input)
    rows = list(reader)

output_lines = []

num_files = len(rows)
file_state = {}
LRU = []
total_size = 0

for i, row in enumerate(rows):
    file_id = row["file_id"]
    size = int(row["size"])
    access_time = row["access_times"]
    file_new_state = file_state.get(file_id,0)
    if file_new_state == 1 or file_new_state == 0:
        file_state[file_id] = 1
        output_lines.append({"access_time" : access_time, "state": "H", "file_id": file_id})
    else:
        output_lines.append({"access_time" : access_time, "state": "M", "file_id": file_id})
        continue

    # LRU logic
    if file_new_state == 0:
        total_size += size
    try:
        LRU.remove((file_id, size))
    except ValueError:
        pass
    LRU.append((file_id, size))
    while total_size > maximum_size:
        i,z = LRU.pop(0)
        total_size -= z
        file_state[i] = 2

file = sys.stdout
file.write(f"# Created: {datetime.now().isoformat()}\n")
file.write(f"# Policy: LRU\n")
file.write(f"# Input: {input_file}\n")
file.write(f"# Maximum size: {maximum_size}\n")
headerName = ["access_time","state", "file_id"]
writer = csv.DictWriter(file, fieldnames=headerName)
writer.writeheader()
writer.writerows(output_lines)


