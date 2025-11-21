"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if node == None:
                return 
            if node.val in visited:
                return visited[node.val]

            newNode = Node(node.val)
            temp = []
            visited[newNode.val] = newNode
            for neighbor in node.neighbors:
                nei = dfs(neighbor)
                if nei != None and nei not in newNode.neighbors:
                    newNode.neighbors.append(nei)


            return newNode

        ans = dfs(node)

        

        return ans