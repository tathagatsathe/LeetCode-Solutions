from collections import deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:


        def topological_sort(conditions):
            adj = [[] for _ in range(k+1)]
            indegree = [0]*(k+1)
            for row in conditions:
                adj[row[0]].append(row[1])
                indegree[row[1]]+=1

            queue = deque()

            for i in range(k+1):
                if indegree[i] == 0:
                    queue.append(i)

            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for ad in adj[node]:
                    indegree[ad]-=1

                    if indegree[ad] == 0:
                        queue.append(ad)

            return order

        c_order = topological_sort(rowConditions)
        r_order = topological_sort(colConditions)

        print('c_order: ',c_order)
        print('r_order: ',r_order)

        if len(c_order)<k+1 or len(r_order)<k+1:
            return []

        idx = [[0]*(k+1) for _ in range(2)]
        # print('idx: ',idx)
        count = 0
        for i in range(1, k+1):
            idx[0][c_order[i]] = count
            idx[1][r_order[i]] = count
            count+=1

        # print('idx: ',idx)
        ans = [[0]*k for _ in range(k)]
        for i in range(1, k+1):
            ans[idx[0][i]][idx[1][i]] = i

        return ans