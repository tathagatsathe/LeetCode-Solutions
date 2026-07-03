class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        map_ = {}

        for i, val in enumerate(nums):
            if val not in map_:
                map_[val] = []
            map_[val].append(i)

        for i, val in enumerate(nums):
            if target - val in map_:
                for idx in map_[target-val]:
                    if i!= idx:
                        return [i, idx]

        return []