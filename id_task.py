import json
import csv
import sys
import argparse


parser = argparse.ArgumentParser(description='This function will copy all id numbers\
		 from a .json input file which will be stored in a .csv file.')
parser.add_argument('in_file', type=str, help='enter an existing .json file')
parser.add_argument('out_file', type=str,  help='enter a name to create or overwrite a file (file_name.csv)')
args = parser.parse_args()

def id_parser(in_file, out_file):
	try:
		with open(in_file, 'r') as f:
			data_list = json.load(f)

	except Exception as err:
		print(f"\nSorry, there was an error while loading the input file:\
			 \n{err}\
			 \n-Please check to make sure there are no spelling errors\
			 \n-Make sure that the file is in the current directory")	
		sys.exit()

	csv_file = open(out_file, 'w')
	csv_writer = csv.writer(csv_file)

	id_generator = tuple((key['id'] for key in data_list))

	csv_writer.writerow(id_generator)
	csv_file.close()

	return print(f"\nThe data was saved to {out_file}")
	 

id_parser(args.in_file, args.out_file)
