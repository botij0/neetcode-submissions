# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self.dfs(root, k, result)
        return result[k-1]

    def dfs(self, node: Optional[TreeNode], k:int, result: List[int]):
        if not node:
            return
        
        self.dfs(node.left, k, result)
        result.append(node.val)
        self.dfs(node.right, k, result)
