class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        bottomRight = []
        topLeft = []
        ans = 0
        for i in range(n):
            bottomRight.append([topRight[i][0], bottomLeft[i][1]])
            topLeft.append([bottomLeft[i][0], topRight[i][1]])

        # print('bottomRight: ',bottomRight)
        # print('topLeft: ',topLeft)

        for i in range(n):
            for j in range(n):
                if i!=j:
                    if bottomLeft[j][1] < topRight[i][1] and topRight[i][0] > bottomLeft[j][0]:
                        # print(i, j)
                    # else:
                        y = min(min(topRight[j][1] - bottomLeft[j][1],topRight[i][1] - bottomLeft[i][1]), min(topRight[j][1] - bottomLeft[i][1], topRight[i][1] - bottomLeft[j][1]))
                        x = min(min(topRight[j][0] - bottomLeft[j][0],topRight[i][0] - bottomLeft[i][0]), min(topRight[j][0] - bottomLeft[i][0], topRight[i][0] - bottomLeft[j][0]))
                        side = min(x, y)
                        # print('side: ',side)
                        if side > 0 and side**2 > ans:
                            ans = side**2


                    # if bottomLeft[i][0] <= bottomLeft[j][0] <= topRight[i][0] and bottomLeft[i][1] <= bottomLeft[j][1] <= topRight[i][1]:
                    #     if topRight[j][0] <= topRight[i][0] and topRight[j][1] <= topRight[i][1]:
                    #         area = min(topRight[j][0] - bottomLeft[j][0], topRight[j][1] - bottomLeft[j][1])**2
                    #         print('1: ', i,j, min(topRight[j][0] - bottomLeft[j][0], topRight[j][1] - bottomLeft[j][1]))
                    #     else:
                    #         area = min(min(topRight[i][1] - bottomLeft[j][1], topRight[j][1] - bottomLeft[j][1]), min(topRight[i][0] - bottomLeft[j][0], topRight[j][0] - bottomLeft[j][0]))**2
                    #         print('2: ', i, j, min(topRight[i][1] - bottomLeft[j][1], topRight[i][0] - bottomLeft[j][0]))
                    #     if area > ans:
                    #         ans = area

                    # if topLeft[j][0] <= topLeft[i][0] <= bottomRight[j][0] and topLeft[j][1] >= topLeft[i][1] >= bottomRight[j][1]:
                    #     if bottomRight[i][0] <= bottomRight[j][0] and bottomRight[i][1] >= bottomRight[j][1]:
                    #         area = min(bottomRight[i][0]-topLeft[i][0], topLeft[i][1]- bottomRight[i][1])**2
                    #         print('3: ',i, j, min(bottomRight[i][0]-topLeft[i][0], topLeft[i][1]- bottomRight[i][1]))
                    #     else:
                    #         area = min(min(bottomRight[j][0] - topLeft[i][0], bottomRight[i][0] - topLeft[i][0]), min(topLeft[i][1] - bottomRight[j][1], topLeft[i][1] - bottomRight[i][1] ))**2
                    #         print('4: ',i, j, min(bottomRight[j][0] - topLeft[i][0], topLeft[i][1] - bottomRight[j][1]))

                        
                    #     if area > ans:
                    #         ans = area

        return ans