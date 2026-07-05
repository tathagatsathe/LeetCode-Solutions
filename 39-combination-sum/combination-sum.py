class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()

        def fn(i, target):
            if target == 0:
                return [[]]

            if target < 0 or i >= n or candidates[i] > target:
                return []

            res = []
            arr1 = fn(i, target - candidates[i])
            arr2 = fn(i+1, target)

            if arr1 != []:
                res.extend([[candidates[i]] + a for a in arr1])
            if arr2 != []:
                res.extend(arr2)

            return res

        ans = fn(0, target)

        return ans

