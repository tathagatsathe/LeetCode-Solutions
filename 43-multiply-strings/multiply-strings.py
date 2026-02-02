class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def convertToInt(num):
            temp = 0
            n = len(num)
            order = 0
            for i in range(n-1, -1, -1):
                temp+= (ord(num[i]) - ord("0"))*10**order
                order+=1

            return temp

        return str(convertToInt(num1) * convertToInt(num2))