# Rules:
# We have three attributes here: create, edit and view
# If at least one attribute is within the time threshold, then keep it.

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
            doc_id_times[doc_id] = {'create_time': None, 'edit_time': None, 'view_time': None}
        if name.lower() == 'create':
            doc_id_times[doc_id]['create_time'] = id_time
        elif name.lower() == 'edit':
            if not doc_id_times[doc_id]['edit_time'] or id_time > doc_id_times[doc_id]['edit_time']:
                doc_id_times[doc_id]['edit_time'] = id_time
                # also print an output line here
        elif name.lower() == 'view':
            if not doc_id_times[doc_id]['view_time'] or id_time > doc_id_times[doc_id]['view_time']:
                doc_id_times[doc_id]['view_time'] = id_time
                # print an output line here

print("docs keep: ")
for doc_id, times in doc_id_times.items():
    create_time = times['create_time']
    edit_time = times['edit_time']
    view_time = times['view_time']

    if (
        (create_time and create_time >= time_threshold) or
        (edit_time and edit_time >= time_threshold) or
        (view_time and view_time >= time_threshold)
    ):
        print(f"doc_id: {doc_id}")

