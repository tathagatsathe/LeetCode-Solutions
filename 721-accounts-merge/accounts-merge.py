class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = {}
        graph = {}

        for i in range(n):
            k = len(accounts[i])
            if accounts[i][1] not in graph:
                graph[accounts[i][1]] = []
                parent[accounts[i][1]] = accounts[i][0]
            for j in range(2, k):
                if accounts[i][j] not in graph:
                    graph[accounts[i][j]] = []
                    parent[accounts[i][j]] = accounts[i][0]
                if accounts[i][j-1] not in graph:
                    graph[accounts[i][j-1]] = []
                    parent[accounts[i][j-1]] = accounts[i][0]
                graph[accounts[i][j]].append(accounts[i][j-1])
                graph[accounts[i][j-1]].append(accounts[i][j])

        ans = []
        visited = set()
        def dfs(node):
            if node in visited:
                return None
            temp = [node]
            visited.add(node)
            for nei in graph[node]:
                t = dfs(nei)
                if t!=None:
                    temp.extend(t)
            return temp


        for key in graph:
            temp = dfs(key)
            if temp!=None:
                temp.sort()
                l = [parent[key]]
                l.extend(temp)
                ans.append(l)

            
        return ans