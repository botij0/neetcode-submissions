# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes = []
        self.dfs(root, subRoot.val, nodes)

        for node in nodes:
            if self.aux(node, subRoot):
                return True

        return False

    def aux(self, node: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if not node and not subRoot:
            return True

        if not node and subRoot:
            print("not node")
            return False
        
        if not subRoot and node:
            print(not subRoot)
            return False

        if node.val != subRoot.val:
            return False

        return self.aux(node.left, subRoot.left) and self.aux(node.right, subRoot.right)
    
    def dfs(self, root: Optional[TreeNode], value: int, nodes: List[TreeNode]):
        if not root:
            return
        
        if root.val == value:
            nodes.append(root)
        
        self.dfs(root.left, value, nodes)
        self.dfs(root.right, value, nodes)