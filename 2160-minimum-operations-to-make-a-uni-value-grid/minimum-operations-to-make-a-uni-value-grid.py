class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_list = [item for sublist in grid for item in sublist]

        flat_list.sort()
        
        # print(flat_list)
        n = len(flat_list)

        mid = n//2
        # print(n)
        # print(mid)
        # print(flat_list[mid])
        ans = 0
        for i in range(mid):
            diff = (flat_list[mid] - flat_list[i])
            if diff % x != 0:
                return -1
            ans+=(diff//x)

        for i in range(mid+1, n):
            diff = (flat_list[i] - flat_list[mid])
            if diff % x != 0:
                return -1
            ans+=(diff//x)

        return ans


# [57, 69, 105, 105, 141, 177, 273, 309, 345, 417, 429, 453, 465, 
# 609, 657, 657, 681, 681, 717, 801, 885, 897, 897, 921, 921, 933, 945]
