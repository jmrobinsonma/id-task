import json
import csv

json_filename = 'data.json'
csv_filename = 'id_task.csv'
id_list = []
exceptions = 0

csv_file = open(csv_filename, 'w')
csv_writer = csv.writer(csv_file)

try:
	with open(json_filename, 'r') as f:
		data_list = json.load(f)

except Exception as err:
	exceptions += 1
	print(f"\nSorry, there was an error while loading the input file: \n{err}\n")	

else:
	for nested_dict in data_list:
		id_list.append(nested_dict['id'])

csv_writer.writerow(id_list)

if exceptions == 1:
	pass

else:
	print(f"\nThe data was saved to {csv_filename}")

csv_file.close()
