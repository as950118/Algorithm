class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        self.cache = {}

    def get(self, key: int) -> int:
        ret = self.cache.get(key, -1)
        if ret != -1:
            del self.cache[key]
            self.cache[key] = ret
        return ret

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        elif self.used < self.capacity:
            self.used += 1
        else:
            last_key = list(self.cache.keys())[0]
            del self.cache[last_key]
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)