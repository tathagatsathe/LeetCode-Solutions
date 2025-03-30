class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)-1
        i=0
        while(i+n<len(haystack)):
            if(haystack[i] == needle[0] and haystack[i+n]==needle[-1]):
                if(haystack[i:i+n+1]==needle):
                    return i
            i+=1
        
        return -1

        