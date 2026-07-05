# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def serialize(root):
            """Converts a binary tree into a string expression."""
            if not root:
                return "#"
            return f",{root.val},{serialize(root.left)},{serialize(root.right)}"

        root = serialize(root)
        subRoot = serialize(subRoot)

        return subRoot in root