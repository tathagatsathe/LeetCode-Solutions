# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if root == None:
            return 'None'
        s = [str(root.val)]
        dq = deque([root])

        while dq:
            curr = dq.popleft()
            if curr.left != None:
                if curr.left.val != None:
                    s.append(str(curr.left.val))
                dq.append(curr.left)
            else:
                s.append(str(curr.left))
            if curr.right != None:
                if curr.right.val != None:
                    s.append(str(curr.right.val))
                dq.append(curr.right)
            else:
                s.append(str(curr.right))

        joined_s = ",".join(s)

        return joined_s


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "None":
            return None
        s = data.split(',')

        i = 0
        j = 1
        root = TreeNode(s[0])
        dq = deque([root])
        while j<len(s):
            node = dq.popleft()
            if s[j]!='None':
                node.left = TreeNode(int(s[j]))
                dq.append(node.left)
            if s[j+1]!='None':
                node.right = TreeNode(int(s[j+1]))
                dq.append(node.right)
            j+=2


        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))