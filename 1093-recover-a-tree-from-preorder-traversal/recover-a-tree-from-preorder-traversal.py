# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        count=0
        arr = []
        edge = []
        i=0
        while(i<len(traversal)):
            if(traversal[i]=="-"):
                count+=1
            else:
                num=''
                while(i<len(traversal) and traversal[i]!='-'):
                    num+=traversal[i]
                    i+=1
                arr.append(int(num))
                edge.append(count)
                count=1
            i+=1
        
        # print(arr)
        # print(edge)
        prev = TreeNode(arr[0])
        st = deque([{'e': edge[0], 'nd': prev}])
        # print(st[0]['nd'])
        i=1
        while(i<len(arr)):
            while(st[-1]['e']>=edge[i]):
                temp = st.pop()

            curr = TreeNode(arr[i])
            prev = st[-1]['nd']
            if(prev.left==None):
                prev.left = curr
            else:
                prev.right = curr
            
            st.append({'e': edge[i], 'nd': curr})
            i+=1
        # print(st)
        return st[0]['nd']
        # [1, 2, 3, 4, 5, 6, 7]
        # [0, 1, 2, 2, 1, 2, 2]
        