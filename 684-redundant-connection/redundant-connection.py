class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = list(range(n+1))
        def find(a):
            if parent[a] != a:
                return find(parent[a])

            return parent[a]

        def union(a,b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return True

            parent[rootB] = rootA

            return False

        for edge in edges:
            if union(edge[0], edge[1]):
                return edge

        return -1
