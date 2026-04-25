class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map_ = {}
        ans = [-1]*len(nums1)

        for idx, num in enumerate(nums2):
            if num not in map_:
                map_[num] = idx

        for idx, num in enumerate(nums1):
            for i in range(map_[num], len(nums2)):
                if nums2[i] > num:
                    ans[idx] = nums2[i]
                    break

        return ans
            