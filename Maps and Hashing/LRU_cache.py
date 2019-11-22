
class LRU_Cache():

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        if key in self.cache.keys():
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        self.cache.update({key: value})


our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))
print(our_cache.get(2))
print(our_cache.get(3))
