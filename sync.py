import os

class Synchronizer:

    def __init__(self, source, destination):
        self._source = source
        self._destination = destination

    @property
    def source(self):
        return self._source
    
    @property
    def destination(self):
        return self._destination
    
    def sync_folders(self):
        pass

    def _check_paths(self, source, destination):
        pass