'''Just a thing'''
import os
import json

class SavedDict(dict):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

        if os.path.isfile(filename):
            self.load()

    def load(self):
        with open(self._filename) as f:
            self.update(json.load(f))

    def save(self):
        with open(self._filename, 'w') as f:
            json.dump(self, f)

    def __del__(self):
        self.save()
