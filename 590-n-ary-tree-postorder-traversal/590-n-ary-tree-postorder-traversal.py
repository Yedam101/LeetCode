"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        self.answer = []
        self.post(root)
        
        return self.answer
    
    def post(self, Node):
        
        if Node is None:
            return
        
        for i in Node.children:
            self.post(i)
            
        self.answer.append(Node.val)
            
        