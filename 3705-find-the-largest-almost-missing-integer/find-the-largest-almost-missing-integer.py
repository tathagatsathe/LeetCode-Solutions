class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n == k:
            return max(nums)

        d = {}
        for val in nums:
            if val not in d:
                d[val] = 0
            d[val]+=1

        if k == 1:
            set_ = set()
            ans = -1
            
            for num, count in d.items():
                if count == 1:
                    ans = max(ans, num)

            return ans

        l, r = nums[0], nums[n-1]

        for i in range(1, k):
            if nums[0] == nums[i] or d[nums[0]] != 1:
                l = -1
            if nums[n-1] == nums[n-i-1] or d[nums[n-1]] != 1:
                r = -1
            if i == k - 1 and l!=r:
                return max(l, r)

        return -1