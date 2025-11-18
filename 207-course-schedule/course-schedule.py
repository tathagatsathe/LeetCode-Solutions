class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False]*numCourses
        completed = [False]*numCourses
        adj = [[] for _ in range(numCourses)]

        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])

        # print(adj)
        def dfs(i):
            if completed[i] == True:
                return completed[i]
            if visited[i] == True:
                return False

            visited[i] = True
            for ad in adj[i]:
                temp = dfs(ad)
                if temp == False:
                    return False
            visited[i] = False
            completed[i] = True
            return True

            
        for i in range(numCourses):
            temp = dfs(i)
            if temp == False:
                return False

        return True
