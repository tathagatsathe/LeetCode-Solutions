class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(start, end):
            if start > end:
                return -1

            mid = (start + end)//2

            if nums[mid] == target:
                return mid
            
            if start == end:
                return -1

            if nums[start] <= nums[end] and nums[start] <= target <= nums[end]:
                if nums[mid] == target:
                    return mid
                elif nums[start] <= target <= nums[mid]:
                    return binarySearch(start, mid)
                else:
                    return binarySearch(mid+1, end)

            left = binarySearch(start, mid)
            if left != -1:
                return left
            right = binarySearch(mid+1, end)
            return right


        return binarySearch(0, len(nums)-1)
