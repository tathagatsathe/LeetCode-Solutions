class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        def fn(num):
            nonlocal ans
            if num > high:
                return False

            if low <= num <= high:
                ans.append(num)

            if num%10 != 9:
                fn(num*10 + (num%10+1))

        for i in range(1, 10):
            fn(i)

        ans.sort()
        
        return ans
