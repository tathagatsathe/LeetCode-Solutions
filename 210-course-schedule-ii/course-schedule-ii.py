from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites == []:
            return list(range(numCourses))
        prereq = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for i in range(len(prerequisites)):
            prereq[prerequisites[i][0]]+=1
            adj[prerequisites[i][1]].append(prerequisites[i][0])

        st = deque()

        for i in range(len(prereq)):
            if prereq[i]==0:
                st.append(i)

        # print(st)
        # print(adj)
        # print(prereq)
        ans = []
        while st:
            node = st.popleft()
            ans.append(node)
            # 0 -> 1
            # print('adj[node]: ',adj[node])
            # print('node: ',node)
            for i in adj[node]:
                prereq[i]-=1
                # print('prereq[i]: ',prereq[i])
                # print('i: ',i)
                if prereq[i] == 0:
                    st.append(i)

        if len(ans)<numCourses:
            return []

        return ans