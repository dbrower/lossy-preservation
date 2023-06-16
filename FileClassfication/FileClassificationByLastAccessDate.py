# Delete the file according to the last access time
# After sorting the access time from the oldest to the newest
# Add the file that has not been accessed within the time_step days into the delete_list
# time_step can be changed.

from datetime import datetime, timedelta
import csv

# Read the CSV file and store the file data in a list
file_list = []
with open("test_data_updated.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        access_times = row['access_times'].strip('[]').replace("'", "").split(", ")
        access_times = [datetime.strptime(time, "%Y-%m-%d %H:%M:%S") for time in access_times if time]
        row['access_times'] = access_times
        file_list.append(row)

file_list.sort(key=lambda x: x['access_times'][-1] if x['access_times'] else datetime.min)

time_step = 365*3
cutoff_date = datetime.now() - timedelta(days=time_step)
delete_files = []
kept_files = []
for file_data in file_list:
    last_accessed_date = file_data['access_times'][-1] if file_data['access_times'] else datetime.min

    if last_accessed_date < cutoff_date:
        delete_files.append(file_data)
    else:
        kept_files.append(file_data)

print("Files marked for deletion:")
for delete_file in delete_files:
    print("File ID:", delete_file['file_id'])
print("Total Deleted Files:", len(delete_files))

print("\nFiles marked to be kept:")
for kept_file in kept_files:
    print("File ID:", kept_file['file_id'])
print("Total Kept Files:", len(kept_files))






