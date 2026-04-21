from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(i):
            if parent[i]!=i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            
            if root_i != root_j:
                parent[root_i] = root_j

            
        for u, v in allowedSwaps:
            union(u, v)

        groups = defaultdict(list)

        for i in range(n):
            groups[find(i)].append(i)

        ans = 0

        for root in groups:
            indices = groups[root]

            source_counts = Counter(source[i] for i in indices)

            for i in indices:
                val = target[i]

                if source_counts[val] > 0:
                    source_counts[val]-=1
                else:
                    ans+=1

        return ans

        

