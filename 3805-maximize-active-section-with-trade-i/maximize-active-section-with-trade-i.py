class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        A = []
        count = 1
        for i in range(1, len(t)):
            if t[i] == t[i-1]:
                count += 1
            else:
                A.append(count)
                count = 1
        A.append(count)
        
        base_ones = s.count('1')
        
        k = (len(A) + 1) // 2
        if k <= 2:
            return base_ones
            
        Z = [A[2 * i + 1] for i in range(k - 1)]
        M = len(Z)
        
        pref = [0] * M
        pref[0] = Z[0]
        for i in range(1, M):
            pref[i] = max(pref[i - 1], Z[i])
            
        suff = [0] * M
        suff[-1] = Z[-1]
        for i in range(M - 2, -1, -1):
            suff[i] = max(suff[i + 1], Z[i])
            
        max_gain = 0
        for i in range(1, k - 1):
            merged = Z[i - 1] + A[2 * i] + Z[i]
            other_max = 0
            if i - 2 >= 0:
                other_max = max(other_max, pref[i - 2])
            if i + 1 < M:
                other_max = max(other_max, suff[i + 1])
                
            gain = max(merged, other_max) - A[2 * i]
            if gain > max_gain:
                max_gain = gain
                
        return base_ones + max_gain