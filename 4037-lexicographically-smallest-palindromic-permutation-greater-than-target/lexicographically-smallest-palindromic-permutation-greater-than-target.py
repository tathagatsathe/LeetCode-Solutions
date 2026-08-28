class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(target)
        freq = [0]*26

        for c in s:
            freq[ord(c) - ord('a')]+=1

        odd_char = ""

        for i in range(26):
            if freq[i]%2 and odd_char != "":
                return ""
            if freq[i]%2:
                odd_char = chr(i + ord('a'))
                freq[i]-=1

        def getNextGreaterChar(c):
            for i in range(ord(c)-ord('a')+1, 26):
                if freq[i] > 0:
                    return chr(ord('a')+i)
            return ""
        
        ans = []
        i = 0
        while True:
            if i < n and freq[ord(target[i]) - ord('a')] > 1:
                ans.append(target[i])
                freq[ord(target[i]) - ord('a')]-=2
                i+=1
            else:
                if sum(freq) == 0:
                    temp = "".join(ans) + odd_char + "".join(ans[::-1])
                    if temp > target:
                        return temp
                nextChar = ""
                if i < n:
                    nextChar = getNextGreaterChar(target[i])
                while i >= 0 and nextChar == "" and ans!=[]:
                    popped_char = ans.pop()
                    freq[ord(popped_char)-ord('a')]+=2
                    nextChar = getNextGreaterChar(popped_char)
                break

        # print('ans, nextChar: ',ans, nextChar, freq)
        temp = []
        if nextChar != "":
            ans.append(nextChar)
            freq[ord(nextChar) - ord('a')]-=2

        # print('ans, temp: ',ans, temp)

        for i in range(26):
            while freq[i] > 1:
                ans.append(chr(i+ ord('a')))
                freq[i]-=2
        
        if ans == []:
            return ""

        # print('ans, temp: ', ans, temp)
        ans = "".join(ans + [odd_char] + ans[::-1])

        if sum(freq)!=0 or ans <= target:
            return ""

        return ans

                
