# Delete files according to their created date
# There is a date threshold,
# if the file is created older than the date threshold,
# then add the file to the delete_file_list
# add the kept file to the kept_file_list

import csv
from datetime import datetime, timedelta
def delete_files(created_dates, time_step):
    created_dates = [datetime.strptime(date["created_date"], "%Y-%m-%d %H:%M:%S") for date in created_dates]
    created_dates.sort()
    # threshold
    threshold_date = datetime.now() - timedelta(days=time_step)

    delete_files_create_date = []
    kept_files_create_date = []

    for i in range(len(created_dates)):
        if created_dates[i] < threshold_date:
            delete_files_create_date.append(file_list[i]["file_id"])
        else:
            kept_files_create_date.append(file_list[i]["file_id"])

    return delete_files_create_date, kept_files_create_date

file_list = []
with open("test_data_updated.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        file_list.append(row)

# Specify the time step for deletion
# Keep the file within the recent three years
time_step = 365 * 3

delete_files_create_date, kept_files_create_date = delete_files(file_list, time_step)

print("Files to be deleted:")
for file_id in delete_files_create_date:
    print(file_id)

print("\nFiles to be kept:")
for file_id in kept_files_create_date:
    print(file_id)
