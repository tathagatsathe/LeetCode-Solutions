class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        k = arr[0]
        f = 0

        for val in arr:
            if(k==val):
                f+=1
            else:
                if(k==f):
                    return k
                else:
                    k = val
                    f=1

        if(k==f):
            return k

        return -1
        