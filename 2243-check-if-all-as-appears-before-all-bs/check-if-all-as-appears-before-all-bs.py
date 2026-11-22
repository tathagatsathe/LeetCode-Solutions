class Solution:
    def checkString(self, s: str) -> bool:
        checked_a = checked_b = False

        for c in s:
            if c == "a":
                if checked_b:
                    return False
                checked_a = True
            if c == "b":
                checked_b = True

        return True