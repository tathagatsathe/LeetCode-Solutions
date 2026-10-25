class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        arr = []
        directions = list(directions)
        n = len(directions)

        countR = 0
        for i in range(n):
            if directions[i] == 'R':
                countR+=1
            elif countR > 0:
                if directions[i] == 'L':
                    ans+=1 + countR
                    directions[i] = 'S'
                elif directions[i] == 'S':
                    ans+=countR
                countR = 0

        countL = 0
        for i in range(n-1, -1, -1):
            if directions[i] == 'L':
                countL+=1
            elif countL > 0:
                if directions[i] == 'R':
                    ans+=1 + countL
                    directions[i] = 'S'
                elif directions[i] == 'S':
                    ans+=countL
                countL = 0
        
        return ans
