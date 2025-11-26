class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = [[] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                parent[i].append((i,j))

        def find(a):
            if parent[a[0]][a[1]] != (a[0], a[1]):
                parent[a[0]][a[1]] = find(parent[a[0]][a[1]])

            return parent[a[0]][a[1]]

        def union(a, b):
            if grid[a[0]][a[1]] == "0" or grid[b[0]][b[1]] == "0":
                return False
            rootA = find(a)
            rootB = find(b)
            if rootA!=rootB:
                parent[rootB[0]][rootB[1]] = rootA


        for i in range(m):
            for j in range(n):
                if i+1<m:
                    union((i,j),(i+1,j))
                if j+1<n:
                    union((i,j),(i,j+1))

        parent_set = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and parent[i][j] not in parent_set:
                    parent_set.add(find((i,j)))

        return len(parent_set)

