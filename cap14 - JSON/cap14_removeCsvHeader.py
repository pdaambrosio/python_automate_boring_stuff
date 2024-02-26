#!/home/pdajgs/python_labs/py3.7/bin/python3

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

path = os.path.basename('cap14 - JSON')

for csvFilename in os.listdir(path):
    if not csvFilename.endswith('.csv'):
        continue
    print('Removing header from ' + csvFilename + '...')
    csvRows = []
    with open(os.path.join(path, csvFilename)) as csvFileObj:
        readerObj = csv.reader(csvFileObj)
        for row in readerObj:
            if readerObj.line_num == 1:
                continue
            csvRows.append(row)
    with open(os.path.join('headerRemoved', csvFilename), 'w', newline='') as csvFileObj:
        csvWriter = csv.writer(csvFileObj)
        for row in csvRows:
            csvWriter.writerow(row)
print('Done!')