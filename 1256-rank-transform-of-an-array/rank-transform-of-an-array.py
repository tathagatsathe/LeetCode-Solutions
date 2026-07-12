class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        arr = [(val, i) for i, val in enumerate(arr)]
        arr.sort()
        ans = [1]*n

        rank = 1
        for i in range(1, n):
            if arr[i][0] != arr[i-1][0]:
                rank+=1
            ans[arr[i][1]] = rank

        return ans