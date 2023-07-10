from datetime import datetime
import csv
import os

input_file = "test_data_updated.csv"
output_directory = ""
output_file = os.path.join(output_directory, "output_data.txt")

with open(input_file, "r") as input:
    reader = csv.DictReader(input)
    rows = list(reader)

output_lines = []
# Add the header of the txt file
output_lines.append(f"Created: {datetime.now().isoformat()}")
output_lines.append(f"Policy: LRU")
output_lines.append(f"Input: {input_file}")

# The oldest 30% of files
num_files = len(rows)
threshold = int(num_files * 0.3)
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
        output_lines.append(f"{access_time},H,{file_id}")
    else:
        output_lines.append(f"{access_time},M,{file_id}")
        continue

    # LRU logic
    if file_new_state == 0:
        total_size += size
    try:
        LRU.remove((file_id, size))
    except ValueError:
        pass
    LRU.append((file_id, size))
    while total_size > 10**11:
        i,z = LRU.pop(0)
        total_size -= z
        file_state[i] = 2


with open(output_file, "w") as output:
    output.write("\n".join(output_lines).replace("[", "").replace("]", ""))
