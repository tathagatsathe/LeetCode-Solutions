class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        def binarySearch(start, end):
            if start > end:
                return float("inf")

            if start == end:
                return nums[start]

            if nums[end] > nums[start]:
                return nums[start]

            mid = (start+end)//2

            return min(binarySearch(start, mid), binarySearch(mid+1, end))

        ans = binarySearch(0, n-1)

        return ans