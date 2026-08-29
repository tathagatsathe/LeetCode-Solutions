class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()

        ans = []

        def fn(i, target, arr):
            nonlocal ans
            if target == 0:
                ans.append(arr)
                return

            if target < 0 or i >= n or candidates[i] > target:
                return 

            res = []
            fn(i, target - candidates[i], arr + [candidates[i]])
            fn(i+1, target, arr)
            return 


        fn(0, target, [])

        return ans

