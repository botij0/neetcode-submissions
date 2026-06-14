# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root: Optional[TreeNode], values: List[int], targetSume: int):
            if not root:
                return False
            
            current_sum = sum(values)
            aux = current_sum + root.val

            if aux == targetSum and root.left is None and root.right is None:
                return True

            values.append(root.val)
            left = dfs(root.left, values, targetSum)
            right =  dfs(root.right, values, targetSum)

            if not left and not right:
                values.pop()
                return False

            return True

        v = []
        return dfs(root, v, targetSum)

