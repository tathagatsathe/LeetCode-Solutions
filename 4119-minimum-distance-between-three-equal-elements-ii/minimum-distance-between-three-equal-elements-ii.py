class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = float("inf")

        prev_idx = {}

        for i, num in enumerate(nums):
            if num not in prev_idx:
                prev_idx[num] = []
            
            if len(prev_idx[num])>=2:
                ans = min(abs(i - prev_idx[num][-2]), ans)
            prev_idx[num].append(i)

        return -1 if ans == float("inf") else 2*ans