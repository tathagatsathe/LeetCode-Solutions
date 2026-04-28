class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_list = [item for sublist in grid for item in sublist]
        flat_list.sort()
        n = len(flat_list)

        mid = n//2
        ans = 0
        
        for i in range(mid):
            diff = (flat_list[mid] - flat_list[i])
            if diff % x != 0:
                return -1
            ans+=(diff//x)

        for i in range(mid+1, n):
            diff = (flat_list[i] - flat_list[mid])
            if diff % x != 0:
                return -1
            ans+=(diff//x)

        return ans

