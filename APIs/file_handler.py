import pickle, sys

class TextFileWriter:

    file_path = ""
    buffer = ""
    buffer_current_size = 0
    current_tell = 0
    buffer_max_size = 400000000                 # 400 MB
    file_handle = None

    def __init__(self,file_path):
        self.file_path = file_path
        self.__open_file()
    
    def __del__(self):
        if self.buffer_current_size > 0:
            self.file_handle.write(self.buffer)
        self.file_handle.close()

    def __open_file(self):
        self.file_handle = open(self.file_path,'w')
    
    def tell(self):
        return self.current_tell
    
    def write(self,str):
        str_byte_size = sys.getsizeof(str)
        if self.buffer_current_size + str_byte_size < self.buffer_max_size:
            self.buffer += str
            self.buffer_current_size += str_byte_size
        else:
            self.file_handle.write(self.buffer)
            self.buffer = str
            self.buffer_current_size = str_byte_size
            self.current_tell = self.file_handle.tell()
    
    def close(self):
        if self.buffer_current_size > 0:
            self.file_handle.write(self.buffer)
            self.buffer = ""
            self.buffer_current_size = 0
        self.file_handle.close()

class PickleFileWriter:

    file_path = ""
    buffer = []                                 # list of python objects
    buffer_current_size = 0
    current_tell = 0
    buffer_max_size = 400000000                 # 400 MB
    file_handle = None

    def __init__(self,file_path):
        self.file_path = file_path
        self.__open_file()
    
    def __del__(self):
        if self.buffer_current_size > 0:
            pickle.dump(self.buffer,self.file_handle,-1)
        self.file_handle.close()

    def __open_file(self):
        self.file_handle = open(self.file_path,'wb')
    
    def tell(self):
        return self.current_tell
    
    def write(self,obj):
        obj_byte_size = sys.getsizeof(obj)
        if self.buffer_current_size + obj_byte_size < self.buffer_max_size:
            self.buffer.append(obj)
            self.buffer_current_size = sys.getsizeof(self.buffer)
        else:
            pickle.dump(self.buffer,self.file_handle,-1)
            self.buffer = []
            self.buffer.append(obj)
            self.buffer_current_size = sys.getsizeof(self.buffer)
            self.current_tell = self.file_handle.tell()
    
    def close(self):
        if self.buffer_current_size > 0:
            pickle.dump(self.buffer,self.file_handle,-1)
            self.buffer = []
            self.buffer_current_size = 0
        self.file_handle.close()