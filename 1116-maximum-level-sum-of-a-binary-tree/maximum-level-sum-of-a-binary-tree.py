# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        ans = 0
        mx = float("-inf")
        i = 1
        while dq:
            temp = 0
            for j in range(len(dq)):
                node = dq.popleft()
                temp+=node.val
                if node.left != None:
                    dq.append(node.left)
                if node.right != None:
                    dq.append(node.right)

            if temp > mx:
                mx = temp
                ans = i

            i+=1

        return ans