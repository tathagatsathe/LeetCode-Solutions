class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        n = len(s)
        def allValEqual(map_):
            all_equal = True
            temp = None
            for key in map_:
                if temp == None:
                    temp = map_[key]
                elif temp!=map_[key]:
                    all_equal = False
                    break

            return all_equal

        for i in range(n):
            map_ = {}
            for j in range(i, n):
                if s[j] not in map_:
                    map_[s[j]] = 0
                map_[s[j]]+=1
                if allValEqual(map_) and j - i + 1 > ans:
                    ans = j - i + 1


        return ans