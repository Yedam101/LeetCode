"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        self.Answer = []
        self.dfs(root)
        
        return self.Answer
        
    
    def dfs(self, Node):
        if Node is None:
            return
            
        self.Answer.append(Node.val)
        
        for child in Node.children:
            self.dfs(child)
    
    
