class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        dp = [[False]*(n+1) for _ in range(target+1)]

        def fn(idx, target):
            if target == 0:
                return [[]]

            if target < 0 or idx >= n or candidates[idx] > target:
                return []

            if dp[target][idx]!=False:
                return dp[target][idx]

            res = []
            arr1 = fn(idx+1, target - candidates[idx])
            arr2 = fn(idx+1, target)

            res.extend(arr2)
            for arr in arr1:
                if [candidates[idx]] + arr not in res:
                    res.append([candidates[idx]] + arr)

            dp[target][idx] = res

            return res

        res = fn(0, target)

        return res