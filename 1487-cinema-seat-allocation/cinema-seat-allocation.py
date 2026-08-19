class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        ans = 2*n
        prev_r = reservedSeats[0][0]
        groups = [1,1,1]

        for row, seat in reservedSeats:
            if prev_r != row:
                if sum(groups) == 0:
                    ans-=2
                elif groups[0] == 0 or groups[0] == groups[1] == 0:
                        ans-=1
                elif groups[2] == 0 or groups[2] == groups[1] == 0:
                    ans-=1
                groups = [1,1,1]
                prev_r = row
            if 2 <= seat <= 5:
                groups[0] = 0
            if 4 <= seat <= 7:
                groups[1] = 0
            if 6 <= seat <= 9:
                groups[2] = 0


        if sum(groups) == 0:
            ans-=2
        elif groups[0] == 0 or groups[0] == groups[1] == 0:
            ans-=1
        elif groups[2] == 0 or groups[2] == groups[1] == 0:
            ans-=1

        return ans