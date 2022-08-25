"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        self.res = []
        self.dfs(root)
        
        return self.res
        
    
    def dfs(self, root):
        
        if root:
            self.res.append(root.val)
            for i in root.children:
                self.dfs(i)
        else:
            return

    
