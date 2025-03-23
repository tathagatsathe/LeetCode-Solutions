import random
class RandomizedSet:

    def __init__(self):
        self.randomSet = {}

    def insert(self, val: int) -> bool:
        if val in self.randomSet.keys():
            return False
        self.randomSet[val] = True
        return True


    def remove(self, val: int) -> bool:
        if val in self.randomSet.keys():
            del self.randomSet[val]
            return True
        return False

    def getRandom(self) -> int:
        keys = list(self.randomSet.keys())
        idx = random.randint(0,len(keys)-1)
        return keys[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()