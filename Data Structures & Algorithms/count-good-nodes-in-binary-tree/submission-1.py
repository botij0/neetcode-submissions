# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, -200)
    
    def dfs(self, node: Optional[TreeNode], currentMax: int):
        if not node:
            return 0

        r = 0
        if node.val >= currentMax:
            r = 1
            currentMax = node.val

        return  r + self.dfs(node.left, currentMax) + self.dfs(node.right, currentMax)
