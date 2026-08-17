# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = {}
        self.dfs(root, d, 0)
        return list(d.values())

    def dfs(self, node: Optional[TreeNode], d: dict, height: int):
        if not node:
            return
        
        if height not in d:
            d[height] = node.val
        
        self.dfs(node.right, d, height + 1)
        self.dfs(node.left, d, height + 1)

        

        
