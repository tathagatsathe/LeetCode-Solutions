
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        ans = []
        n = len(s)
        freq = [0]*26

        def getNextGreaterChar(c):
            for i in range(ord(c)-ord('a')+1, 26):
                if freq[i] != 0:
                    freq[i]-=1
                    return chr(i+ord('a'))

            return ""

        for c in s:
            freq[ord(c) - ord('a')]+=1

        popped_char = ""
        i = 0
        while len(ans) < len(target):
            if freq[ord(target[i]) - ord('a')] != 0:
                ans.append(target[i])
                freq[ord(target[i]) - ord('a')]-=1
                i+=1
                if i == n:
                    popped_char = ans.pop()
                    freq[ord(popped_char) - ord('a')]+=1
                    next_char = getNextGreaterChar(popped_char)
                    i-=1
                    # print(next_char, freq, popped_char, i)
                    while next_char == "" and i > 0 and ans != []:
                        popped_char = ans.pop()
                        freq[ord(popped_char) - ord('a')]+=1
                        next_char = getNextGreaterChar(popped_char)
                        i-=1
                    if next_char != "":
                        ans.append(next_char)
                    break
            else:
                next_char = getNextGreaterChar(target[i])
                if next_char != "":
                    ans.append(next_char)
                    break
                else:
                    if ans == []:
                        break
                    popped_char = ans.pop()
                    freq[ord(popped_char) - ord('a')]+=1
                    next_char = getNextGreaterChar(popped_char)
                    i-=1
                    # print(next_char, freq, popped_char, i)
                    while next_char == "" and i > 0 and ans != []:
                        popped_char = ans.pop()
                        freq[ord(popped_char) - ord('a')]+=1
                        next_char = getNextGreaterChar(popped_char)
                        i-=1
                    if next_char != "":
                        ans.append(next_char)
                    break
            # else:
            #     next_char = getNextGreaterChar(popped_char)
            #     if next_char != "":
            #         ans.append(next_char)
            #         break
            #     else:
            #         if ans == []:
            #             break
            #         popped_char = ans.pop()
            #         freq[ord(popped_char) - ord('a')]-=1

            # print(ans)
            # print(freq)

        if ans != []:
            for i in range(26):
                while freq[i] != 0:
                    ans.append(chr(i + ord('a')))
                    freq[i]-=1

        ans = "".join(ans)

        # print(ans)

        if ans == target:
            return ""

        return ans


