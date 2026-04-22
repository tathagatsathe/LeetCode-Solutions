class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for query in queries:
            for word in dictionary:
                res = 0
                for i in range(len(query)):
                    if query[i] != word[i]:
                        res+=1

                if res <= 2:
                    ans.append(query)
                    break

        return ans