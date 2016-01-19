# simplest hashtable, cannot deal with collisions

class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        

class HashTable:
    size = 20
    def __init__(self):
        self.list = [0] * self.size
    
    def hash(self, key):
        index = key % self.size
        return index
                
    def set(self, key, value):
        index = self.hash(key) 
        self.list[index] = KeyValue(key, value)
        
    def get(self, key):
        index = self.hash(key)
        return self.list[index].value
        
        
        