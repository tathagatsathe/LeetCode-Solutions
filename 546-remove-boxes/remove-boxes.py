class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[-1]*n for _ in range(n)] for _ in range(n)]
        
        def fn(i, j, k):
            if i > j:
                return 0

            if dp[i][j][k]!=-1:
                return dp[i][j][k]

            old_i, old_j, old_k = i, j, k

            while i<j and boxes[i]==boxes[i+1]:
                i+=1
                k+=1

            max_score = (k+1)**2 + fn(i+1, j, 0)
            score = 0
            for m in range(i+1, j+1):
                if boxes[i] == boxes[m]:
                    score = fn(i+1, m-1, 0) + fn(m, j, k+1)
                    max_score = max(max_score, score)

            dp[old_i][old_j][old_k] = max_score

            return dp[old_i][old_j][old_k]

        return fn(0, n-1, 0)
