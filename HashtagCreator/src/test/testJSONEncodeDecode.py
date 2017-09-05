import pytest

import json

import HashtagCreator.creator.ModelJSONEncoder as ModelJSONEncoder
from HashtagCreator.Model import Model


class Test():

    @pytest.fixture
    def get_test_model(self):
        return Model('word', 1, ['document'], ['I am a sentence'])

    def test_serialize_Model_to_JSON(self):
        json_model = Model('word', 1, ['document'], ['I am a sentence'])
        test_json = json.dumps(json_model, cls=ModelJSONEncoder.ModelJSONEncoder)