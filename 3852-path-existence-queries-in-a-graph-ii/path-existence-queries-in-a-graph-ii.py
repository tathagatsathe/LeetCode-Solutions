class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        vals = sorted(set(nums))
        val_to_idx = {v: i for i, v in enumerate(vals)}
        node_val_idx = [val_to_idx[x] for x in nums]
        M = len(vals)

        nxt = [0] * M
        j = 0
        for i in range(M):
            while j + 1 < M and vals[j+1] - vals[i] <= maxDiff:
                j += 1
            nxt[i] = j
        
        LOG = (M).bit_length() + 1
        up = [[0] * M for _ in range(LOG)]
        up[0] = nxt[:]
        for k in range(1, LOG):
            prev = up[k-1]
            curr = up[k]
            for i in range(M):
                curr[i] = prev[prev[i]]
        
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            if nums[u] == nums[v]:
                ans.append(1)
                continue
            
            i = node_val_idx[u]
            j = node_val_idx[v]
            if i > j:
                i, j = j, i
            
            if nxt[i] == i:
                ans.append(-1)
                continue
            
            cur = i
            steps = 0
            for k in range(LOG-1, -1, -1):
                if up[k][cur] < j:
                    cur = up[k][cur]
                    steps += (1 << k)
    
            if up[0][cur] >= j:
                ans.append(steps + 1)
            else:
                ans.append(-1)
        
        return ans
            