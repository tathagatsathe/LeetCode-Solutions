class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count_map = {0: 1}
        for num in nums:
            temp_map = {}
            for k in count_map:
                if k+num not in temp_map:
                    temp_map[k+num] = 0
                if k-num not in temp_map:
                    temp_map[k-num] = 0
                temp_map[k+num]+=count_map[k]
                temp_map[k-num]+=count_map[k]
            count_map = temp_map

        if target in count_map:
            return count_map[target]
        return 0
        