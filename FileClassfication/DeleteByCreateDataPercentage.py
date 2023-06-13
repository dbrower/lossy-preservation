# Delete the file according to the created time
# Each time delete the top 30% oldest files
# The percentage can be changed by changing the value of percentage

import csv
from datetime import datetime

def delete_files(file_list, percentage_del):
    file_list.sort(key=lambda x: datetime.strptime(x["created_date"], "%Y-%m-%d %H:%M:%S"))

    files = len(file_list)
    files_to_delete = int(percentage_del * files)
    delete_file_ids = [file_list[i]["file_id"] for i in range(files_to_delete)]
    kept_file_ids = [file_list[i]["file_id"] for i in range(files_to_delete, files)]
    return delete_file_ids, kept_file_ids

file_list = []
with open("test_data_updated.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        file_list.append(row)

# Delete the top 30% oldest files
# Change the threshold here
percentage = 0.3
num_files_to_delete = int(percentage * len(file_list))

delete_file_ids, kept_file_ids = delete_files(file_list, percentage)

print("Files to be deleted:")
for file_id in delete_file_ids:
    print(file_id)

print("\nFiles to be kept:")
for file_id in kept_file_ids:
    print(file_id)
