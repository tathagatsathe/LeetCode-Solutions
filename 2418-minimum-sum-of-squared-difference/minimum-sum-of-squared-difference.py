class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        n = len(nums1)
        diff_arr = [abs(nums1[i] - nums2[i]) for i in range(n)]

        if sum(diff_arr) <= k:
            return 0

        max_diff = max(diff_arr)
        buckets = [0] * (max_diff + 1)
        for d in diff_arr:
            buckets[d] += 1
            
        for i in range(max_diff, 0, -1):
            if buckets[i] == 0:
                continue

            can_reduce = min(k, buckets[i])
            
            buckets[i] -= can_reduce
            buckets[i - 1] += can_reduce
            
            k -= can_reduce
            
            if k == 0:
                break
                
        ans = 0
        for i in range(max_diff, 0, -1):
            if buckets[i] > 0:
                ans += buckets[i] * (i ** 2)
                
        return ans
