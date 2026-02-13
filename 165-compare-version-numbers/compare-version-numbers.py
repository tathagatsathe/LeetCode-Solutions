class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split("."), version2.split(".")

        n = min(len(v1), len(v2))
        m = max(len(v1), len(v2))

        i = 0
        while i < n:
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
            i+=1
            
        if len(v1) > len(v2):
            while i < m:
                if int(v1[i]) != 0:
                    return 1
                i+=1
        elif len(v2) > len(v1):
            while i < m:
                if int(v2[i]) != 0:
                    return -1
                i+=1

        return 0