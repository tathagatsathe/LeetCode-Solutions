# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []

        dq = deque([root])
        while dq:
            for i in range(len(dq)):
                curr = dq.popleft()
                nodes.append(curr.val)
                if curr.left != None:
                    dq.append(curr.left)
                if curr.right != None:
                    dq.append(curr.right)

        nodes.sort()

        def createBST(arr):
            n = len(arr)
            if n == 0:
                return None

            mid = n//2

            left_subtree = createBST(arr[:mid])
            right_subtree = createBST(arr[mid+1:])

            node = TreeNode(arr[mid])
            node.left = left_subtree
            node.right = right_subtree

            return node

        ans = createBST(nodes)

        return ans
                