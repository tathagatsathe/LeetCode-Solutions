class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        
        ans = 0

        for i, val1 in enumerate(arr1):
            for j, val2 in enumerate(arr2):
                if abs(val2 - val1) <= d:
                    break
                if j == len(arr2) - 1:
                    ans+=1
                    
        return ans