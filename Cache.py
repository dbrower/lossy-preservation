# Delete criterias:
# 1. files have not been accessed within delete_number days
# 2. files have not been accessed for minimum_access times
# 3. file have  been  created for more than 2 years.
import csv
from datetime import datetime, timedelta
import timeit

cache_size = 1000
delete_number = 60
minimum_access = 10

def delete_files():
    cache_list = []
    file_list = []

    with open("CreateFileDataUpdated/test_data_updated.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            access_times = row["access_times"].strip("[]").split(", ")
            access_times = [time.strip("'") for time in access_times if time.strip()]  # Strip single quotes and skip empty times
            file_data = dict(row)
            file_data["access_times"] = access_times
            file_list.append(file_data)

    current_datetime = datetime.now()

    for file_data in file_list:
        created_date = datetime.strptime(file_data["created_date"], "%Y-%m-%d %H:%M:%S")
        access_times = file_data["access_times"]
        access_count = len(access_times)
        last_access = max([datetime.strptime(time, "%Y-%m-%d %H:%M:%S") for time in access_times], default=created_date)

        # Check the created data
        if (
            created_date < (current_datetime - timedelta(days=365 * 5)) and
            access_count < minimum_access and
            (current_datetime - last_access).days > delete_number
        ):
            cache_list.append(file_data)

    print("Files in the cache_list:")
    for file_data in cache_list:
        print("K: " + file_data["file_id"])

    deleted_files = [file_data for file_data in file_list if file_data not in cache_list]

    print("\nDeleted Files:")
    for file_data in deleted_files:
        print("D: " + file_data["file_id"])

    print()

    print("number of files in cache list: " + str(len(cache_list)))
    print("number of files in delefe list: " + str(len(deleted_files)))

# execution time
execution_time = timeit.timeit(delete_files, number=1)

print()
print("Execution Time:", execution_time)
