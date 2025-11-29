class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = list(range(n))

        def find(a):
            if parent[a]!=a:
                return find(parent[a])
            return parent[a]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA!=rootB:
                parent[rootB] = rootA

        for i in range(n):
            for j in range(i+1, n):
                if i!=j and (stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]):
                    union(i, j)

        p = set()
        for i in range(n):
            p.add(find(i))
        ans = n - len(p)

        return ans