map_ = {}
for i in range(31):
    map_[2**i] = True

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n in map_