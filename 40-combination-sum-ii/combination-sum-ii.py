class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        dp = [[False]*(n+1) for _ in range(target+1)]

        def fn(idx, target):
            if target == 0:
                return [[]]

            if target < 0 or idx >= n or candidates[idx] > target:
                return False

            if dp[target][idx]!=False:
                return dp[target][idx]

            res = []
            for i in range(idx, n):
                temp = fn(i+1, target - candidates[i])
                # print('i: ',i, ' temp: ',temp, ' target: ', target - candidates[i])
                if temp != False:
                    for t in temp:
                        if [candidates[i]] + t not in res:
                            res.append([candidates[i]] + t)

            # print('candidates: ',candidates, ' target: ',target)
            # print('res: ', res)
            # print('__________________________________________________')
            dp[target][idx] = res

            return res

        # print('candidates: ',candidates)
        res = fn(0, target)
        # res.sort()
        if res == False:
            res = []

        return res