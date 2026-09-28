# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -10000000

        def dfs(node: Optional[TreeNode]):
            nonlocal result

            if not node:
                return 0
            

            rigthVal = max(dfs(node.right), 0)
            leftVal = max(dfs(node.left), 0)
            result = max(result, node.val + rigthVal + leftVal)

            return node.val + max(rigthVal, leftVal)

        dfs(root)
        return result