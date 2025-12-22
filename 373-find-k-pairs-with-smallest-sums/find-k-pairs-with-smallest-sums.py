import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        ans = []
        if nums1 == [] or nums2 == []:
            return []

        for i in range(min(k, len(nums1))):
            heapq.heappush(h, (nums1[i]+nums2[0], i, 0))

        while h and len(ans)<k:
            sum_, i, j = heapq.heappop(h)
            ans.append([nums1[i], nums2[j]])

            if j+1<len(nums2):
                heapq.heappush(h, (nums1[i]+nums2[j+1], i, j+1))


        return ans
