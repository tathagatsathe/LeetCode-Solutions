class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        h = []
        n = len(grid)
        for i in range(n):
            idx = 0
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    break
                idx+=1
            h.append([i, idx])

        # print(h)
        ans = 0
        h_copy = [y for x, y in h]
        h_copy.sort()

        # print(h_copy)

        for i in range(n):
            if h_copy[i] < i:
                return -1

        for i in range(n):
            if n - i - 1 > h[i][1]:
                idx = None
                for j in range(i, n):
                    if n - i - 1 <= h[j][1]:
                        idx = j
                        break
                if idx != None:
                    while idx > i:
                        h[idx], h[idx-1] = h[idx - 1], h[idx]
                        ans+=1
                        idx-=1
                
                    


        return ans