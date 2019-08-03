import json
import csv

csv_filename = 'id_task.csv'
csv_file = open(csv_filename, 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['ID Number'])

with open('data (1).json', 'r') as f:
	data_list = json.load(f)

for nested_dict in data_list:
	for key in nested_dict:
		if "id" in key:
			csv_writer.writerow([nested_dict['id']])

csv_file.close()

print(f'The data has been saved to {csv_filename}')
