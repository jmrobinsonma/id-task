import json
import csv
import sys
import argparse


parser = argparse.ArgumentParser(description='This function will copy all id numbers from an existing\
		user-defined .json input file.\
		and the results will be stored in a user-defined .csv file.')
parser.add_argument('in_file', type=str, help='enter the path to the existing .json file')
parser.add_argument('out_file', type=str,  help='enter a name to create or overwrite a file (<user_file_name>.csv)')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet',action='store_true')
group.add_argument('-v','--verbose',action='store_true')

args = parser.parse_args()

def id_extractor(in_file, out_file):
	try:
		with open(in_file, 'r') as json_file:
			data_list = json.load(json_file)
			with open(out_file, 'w') as csv_file:
				csv_writer = csv.writer(csv_file)
				csv_writer.writerow((key['id'] for key in data_list))
	except Exception as err:
		print(f"Sorry, there was an error while loading the input file:\
			\n{err}\
			\n-Specify a path to a valid .json file\
			\n-If the file is in the current directory use <filename>.json\
			-Please check to make sure there are no spelling errors")
		sys.exit()
	
	if args.verbose:
		return print(f"\nThe data was saved to {out_file}")

id_extractor(args.in_file, args.out_file)
