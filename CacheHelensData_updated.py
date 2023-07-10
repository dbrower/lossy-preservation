import csv
from datetime import datetime, timedelta

filename = 'helen-test-data-20230608.csv'

time_threshold = datetime.now() - timedelta(days=60)
doc_id_times = {}

with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    index_doc_id = header.index('doc_id')
    index_name = header.index('name')
    index_id_time = header.index('id.time')

    for row in csv_reader:
        doc_id = row[index_doc_id]
        name = row[index_name]
        id_time_str = row[index_id_time]
        id_time = datetime.strptime(id_time_str, '%Y-%m-%dT%H:%M:%SZ')

        if doc_id not in doc_id_times:
            doc_id_times[doc_id] = {'views': 0, 'edits': 0, 'create_time': None}

        if name.lower() == 'create' and id_time >= time_threshold:
            doc_id_times[doc_id]['create_time'] = id_time
        elif name.lower() == 'view' and id_time >= time_threshold:
            doc_id_times[doc_id]['views'] += 1
        elif name.lower() == 'edit' and id_time >= time_threshold:
            doc_id_times[doc_id]['edits'] += 1

print("docs keep:")
for doc_id, activities in doc_id_times.items():
    views = activities['views']
    edits = activities['edits']
    create_time = activities['create_time']
    if views > 0 or edits > 0 or (create_time and create_time >= time_threshold):
        info = f"doc_id: {doc_id}"
        if views > 0:
            print("\t It has been viewed for " +  str(views) + " time(s).")
        if edits > 0:
            print("\t It has been edited " + str(edits) + " time(s).")
        #print(info)
