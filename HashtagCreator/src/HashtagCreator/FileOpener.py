import glob, os
from multiprocessing.dummy import Pool as ThreadPool

from HashtagCreator.Output import pretty_print_from_file


def perform_function_on_file_from_string(string, function=pretty_print_from_file):
    with open(string, 'r') as file:
        return function(file)

def get_filename_strings_from_directory(directory):
    os.chdir(directory)
    array = []
    for file in glob.glob("*.txt"):
        array.append(directory + file)
    return array

#pool = ThreadPool(2)
#pool.map(perform_function_on_file_f1rom_string, test)