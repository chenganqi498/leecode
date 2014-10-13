# Design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key 
# if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. 
# When the cache reached its capacity, 
# it should invalidate the least recently used item before inserting a new item.

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cap = capacity 
        self.start = 0
        self.cache = {}
        self.index = {}

    # @return an integer
    def get(self, key):
        if key in self.cache: return self.cache[key]
        else: return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if len(self.cache) == self.cap:
           self.cache.pop(self.index[self.start])
           self.start += 1
        self.cache[key] = value
        self.index[len(self.index)] = key

if __name__ == '__main__':
   cache = LRUCache(3)
   cache.set(1,1)
   cache.set(2,2)
   cache.set(3,3)
   cache.set(4,4) 
   cache.set(5,5)  
 
