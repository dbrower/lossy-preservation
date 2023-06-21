from datetime import datetime
import csv
import os

input_file = "test_data_updated.csv"
output_directory = "LRU"
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
rows_sorted = sorted(rows, key=lambda x: x['created_date'])

for i, row in enumerate(rows_sorted):
    file_id = row["file_id"]
    access_times = row["access_times"].split(",")
    num_accesses = len(access_times)

    # "H": means the file has been found in the system
    for access_time in access_times:
        output_lines.append(f"{access_time},H,{file_id}")

    # Delete the file if it satisties the following requirement:
        # 1. The creation date of the file is the top 30% oldest
        # 2. The number of access time is less than 10 times
        # 3. The last accessed time is more than 5 years since now.
    if i < threshold and num_accesses < 10:
        last_access_time = access_times[-1].strip("[' ").strip("']")
        if last_access_time:
            last_access_datetime = datetime.strptime(last_access_time, "%Y-%m-%d %H:%M:%S")
            years_since_last_access = (datetime.now() - last_access_datetime).days / 365
            if years_since_last_access > 5:
                output_lines.append(f"{last_access_time},D,{file_id}")

    # if the file has been deleted before, mark "M"
    for access_time in access_times:
        output_lines.append(f"{access_time},M,{file_id}")

with open(output_file, "w") as output:
    output.write("\n".join(output_lines).replace("[", "").replace("]", ""))
