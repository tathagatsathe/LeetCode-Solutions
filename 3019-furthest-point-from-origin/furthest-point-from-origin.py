class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        x = 0
        count_ = 0
        for move in moves:
            if move == "L":
                x-=1
            elif move == "R":
                x+=1
            else:
                count_+=1

        return abs(x) + count_


        