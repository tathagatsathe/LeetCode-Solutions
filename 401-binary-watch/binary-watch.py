class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        def fn(arr, n):
            if n == 0:
                return [0]
            res = []
            for i in range(len(arr)):
                temp = fn(arr[:i] + arr[i+1:], n-1)
                for j in range(len(temp)):
                    res.append(temp[j] + arr[i])

            return res

        H = [1,2,4,8]
        M = [1,2,4,8,16,32]

        ans = []
        for i in range(turnedOn+1):
            if i == 0:
                temp1 = [0]
                temp2 = list(set(fn(M, turnedOn - i)))
            elif i == turnedOn:
                temp2 = [00]
                temp1 = list(set(fn(H, i)))
            else:
                temp1 = list(set(fn(H, i)))
                temp2 = list(set(fn(M, turnedOn - i)))
            temp1 = [val for val in temp1 if val < 12]
            temp2 = [val for val in temp2 if val < 60]

            if temp1 == [] or temp2 == []:
                continue
            
            for t1 in temp1:
                for t2 in temp2:
                    h = str(t1)
                    if t2 < 10:
                        m = '0' + str(t2)
                    else:
                        m = str(t2)
                    ans.append(h + ':' + m)

        return ans

