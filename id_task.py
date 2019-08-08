import json
import csv
import sys


try:
	with open('data.json', 'r') as f:
		data_list = json.load(f)

except Exception as err:
	print(f"\nSorry, there was an error while loading the input file: \n{err}\n-Please check to make sure there are no spelling errors\n-Make sure that the file is in the current directory")	
	sys.exit()

csv_filename = 'id_task.csv'
id_list = []

csv_file = open(csv_filename, 'w')
csv_writer = csv.writer(csv_file)


for nested_dict in data_list:
	id_list.append(nested_dict['id'])

csv_writer.writerow(id_list)

print(f"\nThe data was saved to {csv_filename}")

csv_file.close()
