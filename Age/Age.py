from datetime import datetime, timedelta
import csv
import os
import sys

# Read the CSV file and store the file data in a list
file_list = []
input_file = "test_data_updated.csv"
with open(input_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        access_times = row['access_times'].strip('[]').replace("'", "").split(", ")
        access_times = [datetime.strptime(time, "%Y-%m-%d %H:%M:%S") for time in access_times if time]
        row['access_times'] = access_times
        file_list.append(row)

file_list.sort(key=lambda x: x['access_times'][-1] if x['access_times'] else datetime.min)

# Threshold changed here
maximum_time= int(os.environ.get("MAXIMUM_SIZE", 50))
cutoff_date = datetime.now() - timedelta(days=maximum_time)

delete_files = []
kept_files = []
output_data = []  # List to store the output data

for file_data in file_list:
    last_accessed_date = file_data['access_times'][-1] if file_data['access_times'] else datetime.min

    if last_accessed_date < cutoff_date:
        delete_files.append(file_data)
        output_data.append({
            'access_time': last_accessed_date,
            'keep or delete': 'D',
            'file_id': file_data['file_id']
        })
    else:
        kept_files.append(file_data)
        output_data.append({
            'access_time': last_accessed_date,
            'keep or delete': 'K',
            'file_id': file_data['file_id']
        })

# Write the output data to a CSV file
file = sys.stdout
file.write(f"# Created: {datetime.now().isoformat()}\n")
file.write(f"# Policy: Age\n")
file.write(f"# Input: {input_file}\n")
file.write(f"# Maximum time: {maximum_time / 365} year(s)\n")
headerNames = ["access_time", "keep or delete", "file_id"]
writer = csv.DictWriter(file, fieldnames=headerNames)
writer.writeheader()
writer.writerows(output_data)