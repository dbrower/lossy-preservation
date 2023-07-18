from datetime import datetime, timedelta
from faker import Faker
import uuid
import random
import csv
from operator import itemgetter

fake = Faker()


def generate_random_file():
    dt = datetime.now()
    timestamp = datetime.timestamp(dt)
    # Generate unique id
    file_id = str(uuid.uuid4())
    file_size = random.randint(1, 1000000000)  # in KB
    # random date between 1900 till now
    start_date = datetime(1900, 1, 1)
    end_date = datetime.now()
    created_date = fake.date_time_between(start_date=start_date, end_date=end_date).strftime("%Y-%m-%d %H:%M:%S")
    owner = fake.name()
    parent_folder = fake.file_path(depth=1)
    file_data = {
        "timestamp": timestamp,
        "file_id": file_id,
        "size": file_size,
        "created_date": created_date,
        "owner": owner,
        "parent_folder": parent_folder,
        "access_times": [],  # List to store access times for the file
    }
    return file_data

file_list = []
# Change number of fake file data here
for _ in range(1000):
    file_data = generate_random_file()
    # Random number of accesses
    num_accesses = random.randint(0, 200)
    # Get the access_times and access_users lists
    access_times = file_data["access_times"]

    # Number of days ago (1 to 10,000)
    days_ago = random.randint(1, 10000)
    dt_access = datetime.now() - timedelta(days=days_ago)

    for _ in range(num_accesses):
        # random_offset = random.randint(0, 86400 * days_ago)
        random_offset = random.expovariate(1/20)
        access_time = (dt_access + timedelta(days=random_offset)).strftime("%Y-%m-%d %H:%M:%S")
        # access_times.append(access_time)
        file_list.append((access_time,file_data))
        dt_access -= timedelta(days=random_offset)
    # file_list.append(file_data)
file_list.sort(key=itemgetter(0))


output_file_name = "test_data_updated.csv"
with open(output_file_name, "w", newline="") as file:
    headerName = ["timestamp", "file_id", "size", "created_date", "owner", "parent_folder", "access_times"]
    writer = csv.DictWriter(file, fieldnames=headerName)
    writer.writeheader()
    for access, file_name in file_list:
        file_name["access_times"] = access
        writer.writerow(file_name)
    file.close()
