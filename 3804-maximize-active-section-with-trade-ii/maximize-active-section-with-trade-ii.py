class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        base = s.count('1')

        runStart, runEnd, runVal = [], [], []
        posRun = [0]*n
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            idx = len(runStart)
            runStart.append(i); runEnd.append(j-1); runVal.append(1 if s[i]=='1' else 0)
            for p in range(i, j): posRun[p] = idx
            i = j
        R = len(runStart)

        zeroRuns, zeroIdxOfRun = [], [-1]*R
        for idx in range(R):
            if runVal[idx] == 0:
                zeroIdxOfRun[idx] = len(zeroRuns); zeroRuns.append(idx)
        M = len(zeroRuns)
        zLen = [runEnd[zeroRuns[k]] - runStart[zeroRuns[k]] + 1 for k in range(M)]

        P = [zLen[k] + zLen[k+1] for k in range(M-1)]
        LP = len(P); logt = [0]*(LP+1); sparse = []
        if LP > 0:
            for x in range(2, LP+1): logt[x] = logt[x>>1] + 1
            sparse = [P[:]]; k = 1
            while (1 << k) <= LP:
                prev = sparse[k-1]; half = 1 << (k-1)
                sparse.append([max(prev[t], prev[t+half]) for t in range(LP-(1<<k)+1)])
                k += 1

        def range_max(lo, hi):
            if lo > hi: return 0
            kk = logt[hi-lo+1]
            return max(sparse[kk][lo], sparse[kk][hi-(1<<kk)+1])

        def inWinLen(zk, l, r):
            run = zeroRuns[zk]; s0, e0 = runStart[run], runEnd[run]
            return min(e0, r) - max(s0, l) + 1

        ans = []
        for l, r in queries:
            a, b = posRun[l], posRun[r]
            if a == b:
                ans.append(base); continue
            zlo = zeroIdxOfRun[a] if runVal[a]==0 else zeroIdxOfRun[a+1]
            zhi = zeroIdxOfRun[b] if runVal[b]==0 else zeroIdxOfRun[b-1]
            gain = 0
            if zhi >= zlo + 1:
                A, B = inWinLen(zlo, l, r), inWinLen(zhi, l, r)
                if zlo + 1 == zhi:
                    gain = A + B
                else:
                    gain = max(A + zLen[zlo+1], zLen[zhi-1] + B, range_max(zlo+1, zhi-2))
            ans.append(base + gain)
        return ans