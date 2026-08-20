# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [-1001]
        self.dfs(root, result)
        return result[0]

    def dfs(self, node: Optional[TreeNode], result: List[int]):
        if not node:
            return 0

        L = max(self.dfs(node.left, result), 0) 
        R =  max(self.dfs(node.right, result), 0)

        result[0] = max(result[0], node.val + L + R)

        return node.val + max(L, R)
        
