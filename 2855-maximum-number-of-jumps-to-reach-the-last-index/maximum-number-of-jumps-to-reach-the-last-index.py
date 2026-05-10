class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1]*n
        ans = -1

        def fn(i, step):
            nonlocal ans
            
            if i > n-1:
                return

            if step <= dp[i]:
                return dp[i]
            if i == n-1:
                dp[i] = max(dp[i], step)
                return 

            j = i+1

            for j in range(i+1, n):
                if nums[i] - target <= nums[j] <= nums[i] + target:
                    fn(j, step+1)

            dp[i] = max(dp[i], step)


        fn(0, 0)

        return dp[-1]

        

