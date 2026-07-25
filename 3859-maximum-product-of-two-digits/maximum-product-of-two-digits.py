class Solution:
    def maxProduct(self, n: int) -> int:
        arr = []

        while n:
            arr.append(n%10)
            n = n//10

        arr.sort(reverse=True)
        
        return arr[0]*arr[1]