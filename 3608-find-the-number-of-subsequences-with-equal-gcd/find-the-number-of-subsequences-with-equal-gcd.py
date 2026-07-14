class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        dp = defaultdict(lambda: defaultdict(int))
        dp[0][0] = 1
        
        for num in nums:
            new_dp = defaultdict(lambda: defaultdict(int))
            
            for g1 in dp:
                for g2 in dp[g1]:
                    count = dp[g1][g2]
                   
                    new_dp[g1][g2] = (new_dp[g1][g2] + count) % MOD
                    
                    ng1 = num if g1 == 0 else gcd(g1, num)
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + count) % MOD
                    
                    ng2 = num if g2 == 0 else gcd(g2, num)
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + count) % MOD
            
            dp = new_dp
        
        ans = 0
        for g in dp:
            if g > 0 and g in dp[g]:
                ans = (ans + dp[g][g]) % MOD
        
        return ans



