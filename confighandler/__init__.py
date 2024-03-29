import json
import os
from collections import ChainMap

class ConfigHandler(ChainMap):
    def __init__(self, *maps):
        map_values = []
        for entry in maps:
            if type(entry) == str:
                map_values.append(self.handle_str(entry))
            else:
                map_values.append(entry)

        super().__init__(*map_values)

    def get_list(self, key):
        val = self.get(key)
        if type(val) == list:
            return val
        elif type(val) in [str, bytes, bytearray]:
            return json.loads(val)
        return None

    def handle_str(self, val):
        if os.path.isfile(val):
            with open(val) as f:
                return json.load(f)

        return json.loads(val)
