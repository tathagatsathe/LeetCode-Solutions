class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        diff = float("inf")
        
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1]<diff:
                diff = arr[i] - arr[i-1]
                ans = [[arr[i-1],arr[i]]]
            elif arr[i] - arr[i-1]==diff:
                ans.append([arr[i-1],arr[i]])

        return ans