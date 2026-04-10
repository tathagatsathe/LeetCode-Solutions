class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        num_index = {}
        n = len(nums)
        ans = float("inf")

        for i in range(n):
            if nums[i] not in num_index:
                num_index[nums[i]] = []
            num_index[nums[i]].append(i)

        for num, indexes in num_index.items():
            for i in range(len(indexes) - 2):
                if 2 * (indexes[i+2] - indexes[i]) < ans:
                    ans = 2 * (indexes[i+2] - indexes[i])

        return ans if ans != float("inf") else -1