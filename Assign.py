import json
import os
class DataStore(object):
    dictionary={}
    count=0
    def __init__(self,filepath):
        count = count + 1
        filename=filepath
        if(filename):
            directory = self.filepath
            os.mkdir(self.filepath)
        else:
            directory="sample"
            parent_dir = os.getcwd()
            filename = os.path.join(parent_dir, directory)
    def create(self):
        data={"filename":filename,"Id":count}
        obj=json.dump(data)
        dictionary[filename]=obj
    def read(self,key):
        return dictionary[key]
    def delete(self,key):
        del dictionary[key]
path=input("Please provide filepath: ")
if(len(path)>=32):
    print("Path should be less than 32 chars ")
else:
    dataStore=DataStore(path)
dataStore.create()
dataStore.read(filename)
dataStore.delete(filename)




