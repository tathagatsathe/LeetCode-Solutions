class Solution:
    def processStr(self, s: str) -> str:
        result = ""

        for i in s:
            match i:
                case "*":
                    result = result[:-1]
                case "#":
                    result = result + result
                case "%":
                    result = result[::-1]
                case _:
                    result+=i

        return result