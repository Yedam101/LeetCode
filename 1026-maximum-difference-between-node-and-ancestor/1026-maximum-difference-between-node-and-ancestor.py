# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, ancestor):
        
        if not node:
            return -1
        if not ancestor:
            current = 0
        else:
            current = max([abs(node.val - max(ancestor)), abs(node.val - min(ancestor))])

        leftmax = self.dfs(node.left, ancestor + [node.val])
        rightmax = self.dfs(node.right, ancestor + [node.val])
        
        return max([current, leftmax, rightmax])


    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, [])
        

   
