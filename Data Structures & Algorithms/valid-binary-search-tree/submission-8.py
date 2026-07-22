# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:      
        return self.helper(root, -1001, 1001)

    def helper(self, node: Optional[TreeNode], leftLimit: int, rightLimit: int) -> bool:
        if not node:
            return True
        
        if node.val <= leftLimit or node.val >= rightLimit:
            return False

        
        return (self.helper(node.left, leftLimit, node.val) and
                self.helper(node.right, node.val, rightLimit)
        )

