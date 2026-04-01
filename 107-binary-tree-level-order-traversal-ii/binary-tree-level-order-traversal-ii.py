# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        dq = deque([])
        if root:
            dq.append(root)

        while dq:
            temp = []
            for node in range(len(dq)):
                node = dq.popleft()
                if node.left != None:
                    dq.append(node.left)
                if node.right != None:
                    dq.append(node.right)

                temp.append(node.val)
            ans.append(temp)

        ans.reverse()

        return ans
        
