class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        remainder0 = remainder1 = remainder2 = 0
        n = len(stones)

        for val in stones:
            if val%3 == 0:
                remainder0+=1
            elif val%3 == 1:
                remainder1+=1
            else:
                remainder2+=1

        if remainder0 % 2 == 0:
            return remainder1 > 0 and remainder2 > 0
        else:
            return abs(remainder1 - remainder2) > 2

        