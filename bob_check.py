import csv
from datetime import datetime

with open('sample_label.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    sample_labels_from_db = set()
    for row in csvreader:
        #print(row)

        if row['sample_label'] != 'NULL':
            sample_labels_from_db.add(row['sample_label'].strip())

    print('Source Data Length is: ', len(sample_labels_from_db))

    #print(sample_labels_from_db)

        
with open('data.csv', 'rU') as csvfile:
    csvreader = csv.DictReader(csvfile)

    sample_labels_from_data = set()
    for row in csvreader:

        if row['Sample Name'] != 'NULL':
            sample_labels_from_data.add(row['Sample Name'].strip())

    print('Migration Data Length is: ', len(sample_labels_from_data))

    #print(sample_labels_from_data)

    sample_label_duplicate = sample_labels_from_data.intersection(sample_labels_from_db)

print(len(sample_label_duplicate))
print(sorted(sample_label_duplicate))
