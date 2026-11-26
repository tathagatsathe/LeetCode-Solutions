class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        stones_to_rem = 10
        
        for i in range(5):
            if n < stones_to_rem:
                return False
            n-=stones_to_rem
            stones_to_rem-=1
            if n < stones_to_rem:
                return True
            n-=stones_to_rem
            stones_to_rem-=1

        return False