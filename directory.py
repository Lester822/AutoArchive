import os

class Directory:
    def __init__(self, path):
        self._path = path
    
    def path(self):
        return self._path
    
    def files(self):
        return os.listdir(self._path)


class Active_Directory(Directory):
    def __init__(self, path, archive_path):
        Directory.__init__(self, path)
        self._archive_path = archive_path
    
    def archive_path(self):
        return self._archive_path