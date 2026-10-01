from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        for c in s:
            if len(stack) == 0:
                if c != "(" and c != "[" and c != "{":
                    return False
                stack.append(c)
            else:
                if c == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif c == "}":
                    if stack[-1] == "{": 
                        stack.pop()
                    else:
                        return False
                elif c == "]":
                    if stack[-1] == "[": 
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)

        return len(stack) == 0
                    
