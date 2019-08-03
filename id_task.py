import json
import csv

csv_filename = 'id_task.csv'
csv_file = open(csv_filename, 'w')
csv_writer = csv.writer(csv_file)

id_list = []

with open('data (1).json', 'r') as f:
	data_list = json.load(f)

for nested_dict in data_list:
	id_list.append(nested_dict['id'])

csv_writer.writerow(id_list)
csv_file.close()

print(f'The data has been saved to {csv_filename}')
