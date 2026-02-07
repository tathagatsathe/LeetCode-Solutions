class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        ans = float("inf")
        a_after = [0]*n
        b_before = [0]*n
        countA = countB = 0

        for i in range(n):
            b_before[i]=countB
            if s[i] == "b":
                countB+=1
            
        for i in range(n-1,-1,-1):
            a_after[i]=countA
            if s[i] == "a":
                countA+=1

            
        for i in range(n):
            if a_after[i] + b_before[i] < ans:
                ans = a_after[i] + b_before[i]

        return ans