from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        item = self.cache.get(key, None)
        if not item: return -1
        self.cache.move_to_end(key)
        return item

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        self.cache.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    ob = LRUCache(2)
    ob.put(1, 1)
    ob.put(2, 2)
    ob.get(1)
    ob.put(3, 3)
    ob.get(2)
    ob.put(4, 4)
    ob.get(1)
    ob.get(3)
    ob.get(4)
