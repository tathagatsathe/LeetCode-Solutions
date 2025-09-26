# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(node,p,q):
            
            if(node == None):
                return False

            l1 = lca(node.left,p,q)
            l2 = lca(node.right,p,q)

            if type(l1) != bool:
                return l1
            elif type(l2) != bool:
                return l2

            if (l1 == True and l2 == True):
                return node
            elif ((l1 == True or l2 == True)):
                if(node.val==p.val or node.val==q.val):
                    return node
                return True
            elif((node.val==p.val) or (node.val==q.val)):
                return True

            return False

        ans = lca(root,p,q)

        return ans
