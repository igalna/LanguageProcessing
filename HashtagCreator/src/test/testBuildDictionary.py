import pytest

from HashtagCreator.FileOpener import get_filename_strings_from_directory
from HashtagCreator.BuildDictionary import build_dictionary_from_files_in_directory, sort_dictionary

class Test():
    
    @pytest.fixture
    def get_test_files(self):
        DIRECTORY_LOCATION = '/home/ijohnson/workspace/HashtagCreator/src/data/unitTestingData/'
        test = get_filename_strings_from_directory(DIRECTORY_LOCATION)
        value = build_dictionary_from_files_in_directory(test)
        
        return value
    
    def test_build_dictionary_from_files_in_directory(self):
        value = Test.get_test_files(self)
        assert value['am'].count == 4
            
    def test_get_files_from_build_dictionary(self):
        value = Test.get_test_files(self)
        
        assert value['with'].file[1] == 'doc2.txt'
        
    def test_get_sentences_from_build_dictionary(self):
        value = Test.get_test_files(self)
        
        assert value['I'].sentence[0] == "I am a file with a number of sentences in."
        
    def test_sort_dictionary(self):
        value = Test.get_test_files(self)
        sort = sort_dictionary(value)
        assert sort[0].word == 'the'