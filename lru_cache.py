class LRUCache:

    def __init__(self, size):
        self.cache_size = size
        self.double_end_queue = []
        self.hash_map = {}

    def refer(self, x):

        if x not in self.hash_map.keys():

            if len(self.hash_map) == self.cache_size:
                last_element = self.double_end_queue[-1]

                self.double_end_queue.pop()
                del self.hash_map[last_element]

        else:
            # previous code del self.double_end_queue[self.hash_map[x]]
            del self.double_end_queue[self.double_end_queue.index(x)]

        self.double_end_queue.insert(0, x)
        self.hash_map[x] = 0

    def display(self):
        print(self.double_end_queue)


cache = LRUCache(3)
cache.refer(1)
cache.refer(2)
cache.refer(3)
cache.refer(1)
cache.display()