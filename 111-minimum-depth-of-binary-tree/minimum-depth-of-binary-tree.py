# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        dq = deque([root])
        ans = 1

        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node.left == None and node.right == None:
                    return ans
                if node.left != None:
                    dq.append(node.left)
                if node.right != None:
                    dq.append(node.right)

            ans+=1

        return ans