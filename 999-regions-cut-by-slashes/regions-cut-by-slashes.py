class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n*n*4))
        self.n = n

    def find(self, x: int):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX!=rootY:
            self.parent[rootY] = rootX

    def idx(self, r, c, k):
        return (self.n * r + c)*4 + k


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(n)

        regions = 0

        for i in range(n):
            for j in range(n):
                root = uf.idx(i, j, 0)

                if grid[i][j] == " ":
                    uf.union(root, root+1)
                    uf.union(root+1, root+2)
                    uf.union(root+2, root+3)
                elif grid[i][j] == "/":
                    uf.union(root, root+3)
                    uf.union(root+1, root+2)
                elif grid[i][j] == "\\":
                    uf.union(root, root+1)
                    uf.union(root+2, root+3)

                if i+1<n:
                    uf.union(root+2, uf.idx(i+1,j,0))
                
                if j+1<n:
                    uf.union(root+1, uf.idx(i,j+1,3))

        for i in range(n*n*4):
            if uf.find(i)==i:
                regions+=1
                        

        return regions

