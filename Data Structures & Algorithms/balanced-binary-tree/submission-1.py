# Definition for :ary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), Tuple:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return (True, 0)          # (balanced, height)

            left_bal, left_h = dfs(root.left)
            right_bal, right_h = dfs(root.right)

            bal = left_bal and right_bal and abs(left_h - right_h) <= 1
            
            return (bal, 1 + max(left_h, right_h))
       
        return dfs(root)[0]