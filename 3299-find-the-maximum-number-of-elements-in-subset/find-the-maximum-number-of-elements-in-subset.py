from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        count_one = nums.count(1)
        if count_one:
            ans = count_one if count_one % 2 else count_one - 1

        c = Counter(nums)
        sorted_c = sorted(list(set(nums)))

        def isPerfectSquare(n):
            return n**0.5 == int(n**0.5)

        map_ = {}

        for val in sorted_c:
            if val == 1:
                continue

            map_[val] = 1
            sqrt = int(val**0.5)
            if isPerfectSquare(val) and sqrt in c and c[sqrt] > 1:
                map_[val] = map_[sqrt] + 2
            ans = max(ans, map_[val])
            
        return ans