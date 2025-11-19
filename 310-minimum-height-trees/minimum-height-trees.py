from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if edges == []:
            return [0]
        adj = [[] for _ in range(n)]
        visited = [False]*n
        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])

        count = [0]*n
        print(adj)
        st = deque([])
        for i in range(n):
            count[i] = len(adj[i])
            if len(adj[i]) == 1:
                st.append(i)

        rem_nodes = n
        while rem_nodes>2:
            leaf_c = len(st)
            rem_nodes-=leaf_c
            for i in range(leaf_c):
                node = st.popleft()
                for ad in adj[node]:
                    count[ad]-=1
                    if count[ad] == 1:
                        st.append(ad)

        print(count)
        print(st)

        return list(st)

                