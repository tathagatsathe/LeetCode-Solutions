class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr = ['abc', 'def', 'ghi', 'jkl', 'mno','pqrs','tuv','wxyz']
        ans = ['']
        if (digits == ""):
            return []
        for i in digits:
            t = []
            for j in arr[int(i)-2]:
                for k in range(len(ans)):
                    t.append(ans[k]+j)
            ans = t

        
        print(ans)

        return ans

            
        