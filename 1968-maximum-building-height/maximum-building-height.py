class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if len(restrictions) == 0:
            return n - 1

        restrictions.sort()
        # print('restrictions: ', restrictions)
        ans = 0
        
        if restrictions[0][0] != 1:
            restrictions = [[1,0]] + restrictions
        if restrictions[-1][0] != n:
            restrictions = restrictions + [[n, n]]
        
        dp = [0]*(len(restrictions))
        # print('restrictions: ', restrictions)
        prev_idx, prev_height = restrictions[0][0], restrictions[0][1]
        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            if height > prev_height:
                height = min(prev_height + (idx - prev_idx), height)
            prev_idx, prev_height = idx, height
            dp[i] = height

        prev_idx, prev_height = restrictions[-1][0], restrictions[-1][1]
        for i in range(len(restrictions)-2,-1,-1):
            idx, height = restrictions[i]
            if height > prev_height:
                height = min(prev_height + (prev_idx - idx), height)
            prev_idx, prev_height = idx, height
            dp[i] = min(dp[i], height)

        # print(dp)
        ans = max(dp)
        for i in range(1,len(restrictions)):
            if abs(dp[i] - dp[i-1]) < restrictions[i][0] - restrictions[i-1][0]:
                ans = max(ans, (dp[i] + dp[i-1]+restrictions[i][0] - restrictions[i-1][0])//2)

        return ans