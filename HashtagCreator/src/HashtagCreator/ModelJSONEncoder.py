import json
from HashtagCreator.Model import Model

class ModelJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Model):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)