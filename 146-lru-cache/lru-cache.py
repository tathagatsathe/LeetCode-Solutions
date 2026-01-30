from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.dq = deque([])
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.dq.remove(key)
        self.dq.appendleft(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.dq.remove(key)
            del self.cache[key]

        if len(self.dq) >= self.capacity:
            removed_key = self.dq.pop()
            del self.cache[removed_key]

        self.dq.appendleft(key)
        self.cache[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)