# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -100000000, 1000000000)


    def dfs(self, node: Optional[TreeNode], currentMin: int, currentMax: int):
        if not node:
            return True
        
        if node.val <= currentMin or node.val >= currentMax:
            return False
        
        return (
            self.dfs(node.left, currentMin, node.val) and
            self.dfs(node.right, node.val, currentMax)
        )
                
                
