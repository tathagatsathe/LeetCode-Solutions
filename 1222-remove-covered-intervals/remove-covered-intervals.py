class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        ans = 0
        n = len(intervals)
        parent = list(range(n))

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    parent[j] = i

        def getParent(idx):
            if idx != parent[idx]:
                return getParent(parent[idx])
            return idx

        set_of_parents = set()

        for i in range(n):
            set_of_parents.add(getParent(i))

        return len(set_of_parents)




