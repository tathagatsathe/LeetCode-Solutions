class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        m = len(nums1)
        n = len(nums2)
        dp = [[None]*n for _ in range(m)]

        def fn(i, j):
            if i >= m or j >= n:
                return float("-inf")

            if dp[i][j] != None:
                return dp[i][j]

            temp1 = fn(i+1, j)
            temp2 = fn(i, j+1)
            temp3 = fn(i+1, j+1)

            if temp3!=float("-inf"):
                temp3 = max(max(temp3, nums1[i]*nums2[j]), temp3 + nums1[i]*nums2[j])
            else:
                temp3 = nums1[i]*nums2[j]

            dp[i][j] = max(max(temp1, temp2), temp3)
            return dp[i][j]

        return fn(0, 0)
        