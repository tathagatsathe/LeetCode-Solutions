class Robot:

    def __init__(self, width: int, height: int):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.rotate = {"E": "N", "N": "W", "W": "S", "S": "E"}
        self.dir_mapping = {"E": "East", "W": "West", "N": "North", "S": "South"}
        self.direction = "E"
        self.P = 2*(width - 1) + 2*(height - 1)

    def step(self, num: int) -> None:
        num = num % self.P
        if num == 0:
            if self.x == 0 and self.y == 0:
                self.direction = "S"
        
        while num:
            match self.direction:
                case "E":
                    if self.x + num < self.width:
                        self.x+=num
                        num = 0
                    else:
                        num = self.x + num - (self.width - 1)
                        self.x = self.width - 1
                        self.direction = self.rotate[self.direction]
                case "N":
                    if self.y + num < self.height:
                        self.y+=num
                        num = 0
                    else:
                        num = self.y + num - (self.height - 1)
                        self.y = self.height - 1
                        self.direction = self.rotate[self.direction]
                case "W":
                    if self.x - num >= 0:
                        self.x-=num
                        num = 0
                    else:
                        num = num - self.x 
                        self.x = 0
                        self.direction = self.rotate[self.direction]
                case "S":
                    if self.y - num >= 0:
                        self.y-=num
                        num = 0
                    else:
                        num = num - self.y
                        self.y = 0
                        self.direction = self.rotate[self.direction]

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dir_mapping[self.direction]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()