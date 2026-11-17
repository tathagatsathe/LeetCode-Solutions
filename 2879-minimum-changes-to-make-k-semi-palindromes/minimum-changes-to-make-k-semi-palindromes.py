class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n + 1):
            for L in range(d * 2, n + 1, d):
                divisors[L].append(d)
                

        cost = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = float('inf')
                
                for d in divisors[length]:
                    current_changes = 0
                    
                    for start in range(d):
                        left = i + start
                        right = i + start + ((length - start - 1) // d) * d
                        
                        while left < right:
                            if s[left] != s[right]:
                                current_changes += 1
                            left += d
                            right -= d
                            
                    min_changes = min(min_changes, current_changes)
                
                cost[i][j] = min_changes
                

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for parts in range(1, k + 1):
                for j in range(i - 1):
                    if dp[j][parts - 1] != float('inf'):
                        dp[i][parts] = min(dp[i][parts], dp[j][parts - 1] + cost[j][i - 1])
                        
        return dp[n][k]
