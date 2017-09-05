import pytest

from HashtagCreator.FileOpener import get_filename_strings_from_directory, perform_function_on_file_from_string
from HashtagCreator.Output import pretty_print_from_file


class Test():

    @pytest.fixture
    def directory_name(self):
        DIRECTORY = '/home/ijohnson/workspace/HashtagCreator/src/data/testdata/'
        return DIRECTORY

    @pytest.fixture
    def file_name(self):
        FILE_NAME = 'doc1.txt'
        return FILE_NAME

    def test_get_filename_strings_from_directory(self):
        file_names = get_filename_strings_from_directory(Test.directory_name(self))
        assert file_names[0] == Test.directory_name(self) + Test.file_name(self)

    def test_perform_function_on_file_from_string(self):
        array = perform_function_on_file_from_string(Test.directory_name(self) + Test.file_name(self), function=pretty_print_from_file)