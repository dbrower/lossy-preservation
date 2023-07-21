import csv
import sys
from datetime import datetime
import random
import os

input_file = "test_data_updated.csv"

with open(input_file, "r") as input:
    reader = csv.DictReader(input)
    rows = list(reader)

output_lines = []
file_state = {}
randomChoose = []
numberOfFile = int(os.environ.get("MAXIMUM_SIZE",10**11))

for i, row in enumerate(rows):
    file_id = row["file_id"]
    access_time = datetime.strptime(row["access_times"], "%Y-%m-%d %H:%M:%S")
    file_new_state = file_state.get(file_id, 0)

    if file_new_state == 1:
        file_state[file_id] = 1
        output_lines.append({"access_time": access_time, "state": "H", "file_id": file_id})
    elif file_new_state == 0:
        randomChoose.append(row)
        file_state[file_id] = 1
        output_lines.append({"access_time": access_time, "state": "H", "file_id": file_id})
    else:
        output_lines.append({"access_time": access_time, "state": "M", "file_id": file_id})

    if len(randomChoose) >= numberOfFile:
        file1, file2 = random.sample(randomChoose, 2)
        access_time_1 = datetime.strptime(file1["access_times"], "%Y-%m-%d %H:%M:%S")
        access_time_2 = datetime.strptime(file2["access_times"], "%Y-%m-%d %H:%M:%S")

        if access_time_1 < access_time_2:
            file_state[file1["file_id"]] = 2
            randomChoose.remove(file1)
        else:
            file_state[file2["file_id"]] = 2
            randomChoose.remove(file2)

file = sys.stdout
file.write(f"# Created: {datetime.now().isoformat()}\n")
file.write(f"# Policy: LRU with Oldest File Deletion\n")
file.write(f"# Input: {input_file}\n")
file.write(f"# Maximum size: {numberOfFile}\n")
headerName = ["access_time", "state", "file_id"]
writer = csv.DictWriter(file, fieldnames=headerName)
writer.writeheader()
writer.writerows(output_lines)
