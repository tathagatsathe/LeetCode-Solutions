import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h = []
        mx = float("-inf")
        for i in range(len(nums)):
            heapq.heappush(h, (nums[i][0], i, 0))
            if nums[i][0]>mx:
                mx = nums[i][0]

        ans = [h[0][0], mx]

        while h:
            if mx - h[0][0] < ans[1]-ans[0]:
                ans = [h[0][0], mx]

            num, list_no, idx = heapq.heappop(h)

            if idx + 1 >= len(nums[list_no]):
                break
            
            if nums[list_no][idx+1] > mx:
                mx = nums[list_no][idx+1]

            heapq.heappush(h, (nums[list_no][idx+1], list_no, idx+1))


        return ans