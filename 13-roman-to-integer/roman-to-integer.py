class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M":1000}
        ans = 0
        temp = d[s[0]]

        for i in range(1,len(s)):
            if(d[s[i]]<d[s[i-1]]):
                ans+=temp
                temp=d[s[i]]
            elif(d[s[i]]>d[s[i-1]]):
                ans-=temp
                temp=d[s[i]]
            else:
                temp+=d[s[i]]

        ans+=temp

        return ans