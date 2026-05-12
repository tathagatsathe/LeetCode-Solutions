class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: (x[1] - x[0], x[0]))
        ans = tasks[0][1]

        for actual, minimum in tasks[1:]:
            if ans + actual >= minimum:
                ans+=actual
            else:
                ans = minimum

        return ans