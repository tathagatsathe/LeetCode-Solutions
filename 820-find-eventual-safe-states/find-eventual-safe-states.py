class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [False]*len(graph)

        def dfs(i):
            # print('i: ',i)
            if visited[i] == True:
                # print('visited[i]: ',visited[i], visited[i]==True, i)
                return

            if graph[i] == []:
                visited[i] = 'Y'
            # print('i: ',i, 'visited[i]: ',visited[i])
            if visited[i] == 'Y':
                return visited[i]

            visited[i] = True

            for g in graph[i]:
                temp = dfs(g)
                if temp !='Y':
                    return 

            visited[i] = temp
            return visited[i]

            

        for i in range(len(graph)):
            if visited[i] == False:
                dfs(i)
                # print(visited)
                # print('_____')

        # print(visited)
        ans = []
        for i in range(len(visited)):
            if visited[i] == 'Y':
                ans.append(i)

        return ans

        