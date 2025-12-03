from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        visited = set()
        queue = deque([s])
        visited.add(s)
        while queue:
            st = queue.popleft() 
            for word in wordDict:
                if word == st[:len(word)]:
                    if st[len(word):] == "":
                        return True
                    if st[len(word):] not in visited:
                        queue.append(st[len(word):])
                        visited.add(st[len(word):])

            
        return False