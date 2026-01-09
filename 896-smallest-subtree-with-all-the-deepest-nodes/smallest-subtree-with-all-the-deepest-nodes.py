# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def fn(root, depth):
            if root == None:
                return root, depth

            left_node, left_depth = fn(root.left, depth + 1)
            right_node, right_depth = fn(root.right, depth + 1)

            if left_depth == right_depth:
                return root, left_depth
            elif left_depth > right_depth:
                return left_node, left_depth

            return right_node, right_depth

        ans, depth = fn(root, 0)

        return ans 

