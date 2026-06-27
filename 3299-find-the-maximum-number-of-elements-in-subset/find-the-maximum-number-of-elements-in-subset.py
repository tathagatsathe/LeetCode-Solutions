from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        count_one = nums.count(1)
        if count_one:
            if count_one % 2:
                ans = count_one
            else:
                ans = count_one - 1

        # print(nums)
        c = Counter(nums)
        sorted_c = sorted(list(set(nums)))
        # print(sorted(c.items()))

        def isPerfectSquare(n):
            return n**0.5 - int(n**0.5) == 0
        
        map_ = {1:0}

        for val in sorted_c:
            if val == 1:
                continue
            if c[val] >= 1 and val not in map_:
                sqrt = int(val**0.5)
                if isPerfectSquare(val) and sqrt in c and c[sqrt] > 1:
                    map_[sqrt]+=1
                    map_[val] = map_[sqrt] + 1
                else:
                    map_[val] = 1

        # print(max(map_.values()))
        ans = max(max(map_.values()),ans)
        # print(map_)
        return ans