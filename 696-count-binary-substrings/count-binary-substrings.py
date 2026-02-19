class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        ans = 0
        temp = 0
        count0 = count1 = 0

        for i in range(len(s)):
            if s[i] == "0":
                count0+=1
                if count1 > 0:
                    temp = count1
                    count1 = 0
            else:
                count1+=1
                if count0 > 0:
                    temp = count0
                    count0 = 0

            if 0<count1<=temp:
                ans+=1
            if 0<count0<=temp:
                ans+=1

        return ans