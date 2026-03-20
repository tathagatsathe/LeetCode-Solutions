class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        ans = [[0]*(n-k+1) for _ in range(m-k+1)]

        for i in range(m-k+1):
            for j in range(n-k+1):
                max_, min_ = float("-inf"), float("inf")
                l = []
                for i1 in range(i, i+k):
                    l.extend(grid[i1][j:j+k])

                l = list(set(l))
                l.sort()
                # print(l)
                
                for i1 in range(1, len(l)):
                    if abs(l[i1] - l[i1-1]) < min_:
                        min_ = abs(l[i1] - l[i1-1])

                # print(ans, ans[0][0], min_)
                if min_ == float("inf"):
                    min_ = 0

                ans[i][j] = min_

        return ans
