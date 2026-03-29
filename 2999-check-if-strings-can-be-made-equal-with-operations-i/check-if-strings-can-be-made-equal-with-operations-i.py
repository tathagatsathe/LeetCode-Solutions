class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        dont_move = set()
        
        for i in range(4):
            if s1[i] != s2[i]:
                if i < 2 and s2[i+2] == s1[i] and i not in dont_move:
                    temp = s2[i+2]
                    s2[i+2] = s2[i]
                    s2[i] = temp
                    dont_move.add(i+2)

        # print(s1)
        # print(s2)
        # print(dont_move)
                
        return s1 == s2