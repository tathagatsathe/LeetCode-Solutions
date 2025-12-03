from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        queue = deque([("", 0)])
        ans = []
        while queue:
            st, idx = queue.popleft()
            if idx == n:
                ans.append(st[1:])
            for word in wordDict:
                if s[idx:len(word)+idx] == word:
                    temp = st + " " + s[idx:len(word)+idx]
                    queue.append((temp, len(word)+idx))

        return ans