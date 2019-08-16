import json
import csv
import sys
import argparse


parser = argparse.ArgumentParser(description='This function will copy all id numbers\
		 from a .json input file which will be stored in a .csv file.')
parser.add_argument('in_file', type=str, help='enter an existing .json file')
parser.add_argument('out_file', type=str,  help='enter a name to create or overwrite a file (file_name.csv)')
args = parser.parse_args()

def id_extractor(in_file, out_file):
	try:
		with open(in_file, 'r') as json_file:
			data_list = json.load(json_file)

	except Exception as err:
		print(f"Sorry, there was an error while loading the input file:\
			\n{err}\
			\n-Specify a path to a valid .json file\
			\n-If the file is in the current directory use <filename>.json\
			-Please check to make sure there are no spelling errors")
		sys.exit()

	csv_file = open(out_file, 'w')
	csv_writer = csv.writer(csv_file)

	extractor = tuple((key['id'] for key in data_list))

	csv_writer.writerow(extractor)
	
	csv_file.close()
	json_file.close()
	
	return print(f"\nThe data was saved to {out_file}")
	 

id_extractor(args.in_file, args.out_file)
