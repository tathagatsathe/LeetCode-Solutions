import bisect

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        curr = [0,0]
        direction = "U"
        ans = 0
        obstacles.sort()
        max_possible_dist = sum(x for x in commands if x > 0) 

        filter(lambda x: x[0]<=max_possible_dist and x[1]<=max_possible_dist , obstacles)

        def rotate(direction, c):
            res = direction
            if c == -1:
                match direction:
                    case "U":
                        res = "R"
                    case "R":
                        res = "D"
                    case "D":
                        res = "L"
                    case "L":
                        res = "U"
            elif c == -2:
                match direction:
                    case "U":
                        res = "L"
                    case "R":
                        res = "U"
                    case "D":
                        res = "R"
                    case "L":
                        res = "D"

            return res

        def checkObstacle(curr, dest, direction):
            res = dest
            idx = 0
            if curr[0] == dest[0]:
                obs = obstacles
                if direction == "U":
                    idx = bisect.bisect_right(obstacles, curr)
                    obs = obstacles[idx:]
                elif direction == "D":
                    idx = bisect.bisect_left(obstacles, curr)
                    obs = obstacles[:idx][::-1]
                for ob in obs:
                    if ob[0] == curr[0]:
                        if direction == "U" and curr[1]<ob[1]<=dest[1]:
                            return [ob[0], ob[1]-1]
                        if direction == "D" and curr[1]>ob[1]>=dest[1]:
                            return [ob[0], ob[1]+1]
            elif curr[1] == dest[1]:
                obs = obstacles
                if direction == "L":
                    idx = bisect.bisect_left(obstacles, curr)
                    obs = obstacles[:idx][::-1]
                elif direction == "R":
                    idx = bisect.bisect_right(obstacles, curr)
                    obs = obstacles[idx:]
                for ob in obs:
                    if ob[1] == curr[1]:
                        if direction == "L" and curr[0]>ob[0]>=dest[0]:
                            return [ob[0]+1, ob[1]]
                        if direction == "R" and curr[0]<ob[0]<=dest[0]:
                            return [ob[0]-1, ob[1]]

            return res



        for c in commands:
            if c < 0:
                direction = rotate(direction, c)
                continue
            if direction == "D":
                temp = [curr[0], curr[1]-c]
            elif direction == "U":
                temp = [curr[0], curr[1]+c]
            elif direction == "L":
                temp = [curr[0]-c, curr[1]]
            elif direction == "R":
                temp = [curr[0]+c, curr[1]]

            # print(curr)
            curr = checkObstacle(curr, temp, direction)

            dist = (curr[0]**2 + curr[1]**2) 

            if dist > ans:
                ans = dist

        return ans
