from collections import deque

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        obj = {}
        count = 0
        mx = -1
        while(r<len(fruits)):
            if(count>2):
                obj[fruits[l]]-=1
                if(obj[fruits[l]]==0):
                    obj.pop(fruits[l])
                    count-=1
                l+=1
            else:
                if fruits[r] not in obj:
                    obj[fruits[r]] = 0
                    count+=1
                obj[fruits[r]]+=1
                r+=1
                if(count<=2):
                    t = sum(obj.values())
                    if(t>mx):
                        mx = t

        return mx
        # [1,2,1,1,2,2,3,2,2,3,3]
        # {'1': 3, '2': 3}