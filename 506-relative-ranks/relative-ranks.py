class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        score = [(score[i], i) for i in range(len(score))]

        score.sort(reverse=True)
        ans = [0]*n

        for i in range(n):
            if i == 0:
                ans[score[i][1]] = "Gold Medal"
            elif i == 1:
                ans[score[i][1]] = "Silver Medal"
            elif i == 2:
                ans[score[i][1]] = "Bronze Medal"
            else:
                ans[score[i][1]] = str(i+1)


        return ans
        