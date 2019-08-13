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

csv_file = open(csv_filename, 'w')
csv_writer = csv.writer(csv_file)

id_list = [key['id'] for key in data_list]

csv_writer.writerow(id_list)

print(f"\nThe data was saved to {csv_filename}")

csv_file.close()
