# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        
        if p.val < q.val < root.val or q.val < p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if root.val < p.val < q.val or root.val < q.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)