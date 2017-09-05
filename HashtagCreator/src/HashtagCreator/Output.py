import csv

from Tokenizing import get_sentence_tokens_from_string, split_with_contractions


def pretty_print_from_file(file):
    read_data = file.read()
        
    tokens = get_sentence_tokens_from_string(read_data)
    for token in tokens:
        print(token)
        words = split_with_contractions(token)
        for word in words:
            print(word)

def build_list_from_file(file):
    read_data = file.read()
    return get_sentence_tokens_from_string(read_data)

def results_to_console(results):
    print(results)
    
def results_to_csv(results, output, file_name="result"):
    with open(str(output) + str(file_name) + '.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for model in results:
            writer.writerow(model)