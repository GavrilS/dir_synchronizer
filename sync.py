import os

class Synchronizer:

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, source):
        if not os.path.isdir(source):
            raise Exception('The provided source directory does not exist...')
        
        self._source = source
    
    @property
    def destination(self):
        return self._destination
    
    @destination.setter
    def destinaiton(self, destination):
        if not os.path.isdir(destination):
            os.makedirs(destination)
        
        self._destination = destination
    
    def sync_folders(self):
        pass
