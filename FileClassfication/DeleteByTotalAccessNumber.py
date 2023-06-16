# Delete the file according to the number of access time they have
# The threshold can be changed by changing the variable called min_access.

import csv
def delete_files(file_list, min):
    delete_file_ids = [file["file_id"] for file in file_list if len(file["access_times"]) < min]
    kept_file_ids = [file["file_id"] for file in file_list if len(file["access_times"]) >= min]
    return delete_file_ids, kept_file_ids

file_list = []
with open("test_data_updated.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["access_times"] = row["access_times"].split(",")
        file_list.append(row)

# Change the threshold here
min_access= 50

delete_file_ids, kept_file_ids = delete_files(file_list, min_access)

print("Files to be deleted:")
for file_id in delete_file_ids:
    print(file_id)

print("\nFiles to be kept:")
for file_id in kept_file_ids:
    print(file_id)
