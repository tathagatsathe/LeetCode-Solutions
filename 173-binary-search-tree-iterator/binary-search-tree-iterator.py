# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.dq = deque([root])
        self.curr = None
        node = root
        
        while node.left:
            node = node.left
            self.dq.append(node)

    def next(self) -> int:
        node = self.dq.pop()
        ans = node.val
        self.curr = node
        if self.dq:
            self.curr = self.dq[-1]
        if node.right != None:
            self.dq.append(node.right)
            node = node.right
            while node.left:
                node = node.left
                self.dq.append(node)
        return ans

    def hasNext(self) -> bool:
        if self.curr == None:
            return True
        return len(self.dq) > 0 and self.curr != None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()