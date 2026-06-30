class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        map_ = [0, 0, 0]

        start = 0
        end = 1
        map_[ord(s[0]) - ord('a')]+=1
        map_[ord(s[1]) - ord('a')]+=1

        def checkAllchars(map_):
            for val in map_:
                if val <= 0:
                    return False
            return True

        while start < n :
            if checkAllchars(map_):
                ans+= n - end
                map_[ord(s[start]) - ord('a')]-=1
                start+=1
            else:
                if end < n - 1:
                    end+=1
                    map_[ord(s[end]) - ord('a')]+=1
                else:
                    map_[ord(s[start]) - ord('a')]-=1
                    start+=1

        return ans
