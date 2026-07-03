class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}

        for i, val in enumerate(nums):
            if target - val in map_:
                return [i, map_[target-val]]
            map_[val] = i

        return []