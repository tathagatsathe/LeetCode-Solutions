class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ones = None

        for i in range(len(s)):
            if s[i] == "1":
                if ones == False:
                    return False
                ones = True
            else:
                ones = False

        return True