class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i=0
        while(i<len(s)):
            if((ord('a')<=ord(s[i])<=ord('z')) or (ord('0')<=ord(s[i])<=ord('9'))):
                i+=1
            else:
                s = s[:i]+s[i+1:]
        
        return s==s[::-1]
        