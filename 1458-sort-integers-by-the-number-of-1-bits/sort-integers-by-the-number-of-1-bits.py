class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countOfOne(n):
            res = 0
            while n:
                if n%2:
                    res+=1
                n = n>>1

            return res

        l = [[countOfOne(i), i] for i in arr]
        l.sort()

        ans = [i for count, i in l]
        return ans