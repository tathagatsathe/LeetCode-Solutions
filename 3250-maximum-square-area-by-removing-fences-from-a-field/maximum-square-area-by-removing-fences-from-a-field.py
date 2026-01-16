class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        ans = -1
        mod = 10**9 + 7
        hFences.sort()
        vFences.sort()
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]

        setH = set()
        setV = set()

        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                setH.add(hFences[j]-hFences[i])

        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                setV.add(vFences[j]-vFences[i])



        # print(setH)
        # print(setV)

        for i in setV:
            if i > ans and i in setH:
                ans = i

        if ans == -1:
            return ans

        return ((ans%mod)**2)%mod

