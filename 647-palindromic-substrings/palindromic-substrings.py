class Solution:
    def countSubstrings(self, s: str) -> int:
        i = 0
        ans = 0
        while(i<len(s)):
            j=i
            while(j<len(s)):
                temp = s[i:j+1]
                if(temp==temp[::-1]):
                    ans+=1
                j+=1
            i+=1

        return ans