import operator

from HashtagCreator.FileOpener import perform_function_on_file_from_string
from HashtagCreator.Model import Model
from HashtagCreator.Output import build_list_from_file
from HashtagCreator.Tokenizing import split_with_contractions


def build_dictionary_from_files_in_directory(list_of_files):
    
    dict_values = {}
    
    for file in list_of_files:
        temp = build_dictionary_from_file_name(file)
        
        if not dict_values:
            dict_values = temp
        else:
            for key in temp.keys():
                if (key in dict_values.keys()):
                    dict_values[key].combine_models(temp[key])
                else:
                    dict_values[key] = temp[key]
    return dict_values


def build_dictionary_from_file_name(file_name):
    
    dict_values = {}
    
    doc_name = file_name.split("/")[-1]
    array = (perform_function_on_file_from_string(file_name, build_list_from_file))
    for sentence in array:
        for word in split_with_contractions(sentence):
            if word not in dict_values:
                dict_values[word] = Model(word, 1, [doc_name], [sentence])
            else:
                value = dict_values.get(word)
                value.count += 1
                if sentence not in value.sentence:
                    value.sentence.append(sentence)
                if doc_name not in value.file:
                    value.file.append(doc_name)
    return dict_values

def sort_dictionary(unsorted_dictionary):
    values = unsorted_dictionary.values()
    
    comparator = operator.attrgetter("count")
    
    return sorted(values, key=comparator, reverse=True)
