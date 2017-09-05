import argparse
import sys
sys.path.append('../')

from HashtagCreator import *
from HashtagCreator.BuildDictionary import build_dictionary_from_files_in_directory, \
    sort_dictionary
from HashtagCreator.FileOpener import get_filename_strings_from_directory
from HashtagCreator.Output import results_to_console, results_to_csv

parser = argparse.ArgumentParser()

parser.add_argument("-d" ,
                    "--directory",
                    help="The Directory of files to parse",
                    type=str)

parser.add_argument("-n",
                    "--number",
                    help="The 'n' most common ocurring words",
                    type=int)

parser.add_argument("-f",
                    "--format",
                    help="The format to output the results in",
                    default="print",
                    type=str)

parser.add_argument("-o",
                    "--output",
                    help="Location to send output",
                    type=str)

parser.add_argument("-r",
                    "--result",
                    help="Name of results file",
                    type=str)

args = parser.parse_args()

file_names = get_filename_strings_from_directory(args.directory)
files = build_dictionary_from_files_in_directory(file_names)
sorted_results = sort_dictionary(files)

if (args.format is "print"):
    results_to_console(sorted_results[:args.number])
if (args.format == 'csv'):
    if ('format' in args and 'output' not in args):
        parser.error("To output to CSV you must include an directory path to output to. Use '-o' or '--output' to provide an output path.")
    if ('format' in args and 'output' not in args and 'result' not in args):
        parser.error("To output to CSV you must include a filename for the results. Use '-r' or '--result' to provide a file name.")
    elif ('format' in args and 'output' in args):
        results_to_csv(sorted_results[:args.number], args.output, args.result)
        