from datetime import datetime, timedelta
import csv
import os
import sys

# Read the CSV file and store the file data in a list
file_list = []
input_file = "test_data_updated.csv"
with open(input_file, "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Threshold changed here
maximum_time= int(os.environ.get("MAXIMUM_SIZE", 50))
cutoff =  timedelta(days=maximum_time)

delete_files = []
kept_files = []
output_data = []  # List to store the output data
file_state = {}
last_access = {}

# 0:
# 1:
# 2:
for row in rows:
    file_id = row["file_id"]
    access_time = row["access_times"]
    access_time = datetime.strptime(access_time, '%Y-%m-%d %H:%M:%S')

    file_new_state = file_state.get(file_id,0)
    if file_new_state == 2:
        output_data.append({"access_time": access_time, "state": "M", "file_id": file_id})
        continue
    previous_access_date=last_access.get(file_id,access_time)
    last_access[file_id] = access_time

    if access_time - previous_access_date < cutoff:
        file_state[file_id] = 1
        output_data.append({"access_time": access_time, "state": "H", "file_id": file_id})
    else:
        file_state[file_id] = 2
        output_data.append({"access_time": access_time, "state": "M", "file_id": file_id})

# Write the output data to a CSV file
file = sys.stdout
file.write(f"# Created: {datetime.now().isoformat()}\n")
file.write(f"# Policy: Age\n")
file.write(f"# Input: {input_file}\n")
file.write(f"# Maximum time: {maximum_time / 365} year(s)\n")
headerNames = ["access_time", "state", "file_id"]
writer = csv.DictWriter(file, fieldnames=headerNames)
writer.writeheader()
writer.writerows(output_data)