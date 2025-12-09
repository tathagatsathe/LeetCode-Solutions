import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        sub = [envelopes[0][1]]
        for i in range(1,n):
            idx = bisect.bisect_left(sub, envelopes[i][1])
            if idx == len(sub):
                sub.append(envelopes[i][1])
            else:
                sub[idx] = envelopes[i][1]

        return len(sub)