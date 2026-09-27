# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        
        queue = deque()
        queue.append(root)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if self.helper(node, subRoot):
                    return True
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return False
    
    def helper(self, node1: Optional[TreeNode], node2: Optional[TreeNode]):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False
        
        if node1.val != node2.val:
            return False
        
        return self.helper(node1.left, node2.left) and self.helper(node1.right, node2.right)

