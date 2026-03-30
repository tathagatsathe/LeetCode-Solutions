class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1, s2 = list(s1), list(s2)
        s1_odd, s1_even = [], []
        s2_odd, s2_even = [], []

        for i in range(n):
            if i % 2:
                s1_odd.append(s1[i])
                s2_odd.append(s2[i])
            else:
                s1_even.append(s1[i])
                s2_even.append(s2[i])

        s1_odd.sort()
        s2_odd.sort()
        s1_even.sort()
        s2_even.sort()
        
        return s1_odd == s2_odd and s1_even == s2_even