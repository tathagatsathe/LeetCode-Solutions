"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([])
        if root!=None:
            queue.append(root)

        while queue:
            prev = None
            tempQ = deque([])
            while queue:
                node = queue.pop()
                if(node.right!=None):
                    tempQ.appendleft(node.right)
                if(node.left!=None):
                    tempQ.appendleft(node.left)

                node.next = prev
                prev = node

            queue.extend(tempQ)
        
        return root
        