class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        i, j = 0, 1
        n, m = len(nums1), len(nums2)

        while i < n:
            if j <= i:
                j = i+1
            while j < m and nums2[j] >= nums1[i]:
                j+=1
            if j-1<m and nums2[j-1] >= nums1[i]:
                ans = max(ans, j - i - 1)
            i+=1

        return ans
