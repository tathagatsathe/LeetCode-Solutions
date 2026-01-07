class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def firstNegIndex(arr, start, end):
            if start >= end:
                return start
            mid = start + (end - start)//2
            
            if arr[mid] >= 0:
                return firstNegIndex(arr, mid + 1, end)
            else:
                return firstNegIndex(arr, start, mid)

       
        ans = 0
        m = len(grid[0])
        for i in range(len(grid)):
            if grid[i][m-1]!=0:
                idx = firstNegIndex(grid[i], 0, m-1)
                if grid[i][idx]<0:
                    ans+= (m-idx)

        return ans