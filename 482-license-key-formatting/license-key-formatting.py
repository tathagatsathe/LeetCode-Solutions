class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.split('-')
        s = ''.join(s).upper()[::-1]
        count = 0
        ans = []
        temp = ''
        for i in s:
            temp+=i
            count+=1
            if(count==k):
                ans.append(temp)
                temp = ''
                count=0

        if(count!=0):
            ans.append(temp)

        ans = '-'.join(ans)
        return ans[::-1]
        