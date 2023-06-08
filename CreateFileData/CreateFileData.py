from datetime import datetime
from faker import Faker
import uuid
import random
import csv

fake = Faker()

def generate_random_file():
    dt = datetime.now()
    timestamp = datetime.timestamp(dt)
    # Generate unique id
    file_id = str(uuid.uuid4())
    file_size = random.randint(1, 1024) # in KB
    # random date between 1900 till now
    start_date = datetime(1900, 1, 1)
    end_date = datetime.now()
    created_date = fake.date_time_between(start_date=start_date, end_date=end_date).strftime("%Y-%m-%d %H:%M:%S")
    owner = fake.name()
    parent_folder = fake.file_path(depth=1)

    file_data = {
        "timestamp" : timestamp,
        "file_id": file_id,
        "size": str(file_size) + "KB",
        "created_date": created_date,
        "owner": owner,
        "parent_folder": parent_folder
    }

    return file_data

file_list = []
for _ in range(1000):
    file_data = generate_random_file()
    print(file_data)
    file_list.append(file_data)

output_file_name = "test_data.csv"
with open(output_file_name,"w", newline="") as file:
    headerName = ["timestamp", "file_id", "size", "created_date", "owner", "parent_folder"]
    writer = csv.DictWriter(file, fieldnames=headerName)
    writer.writeheader()
    writer.writerows(file_list)
    file.close()




