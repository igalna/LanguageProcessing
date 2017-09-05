import pytest

from HashtagCreator.FileOpener import perform_function_on_file_from_string
from HashtagCreator.Output import build_list_from_file


class Test():

    @pytest.fixture
    def get_test_data(self):
        return '/home/ijohnson/workspace/HashtagCreator/src/data/testdata/doc1.txt'
    
    @pytest.fixture
    def get_expected_result(self):
        return "Let me begin by saying thanks to all you who've traveled, from far and wide, to brave the cold today."
    
    def test_get_tokens_from_file(self):
            test_data = perform_function_on_file_from_string(Test.get_test_data(self), build_list_from_file)
            assert test_data[0] == Test.get_expected_result(self)