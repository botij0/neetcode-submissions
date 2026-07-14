# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()

        if root:
            queue.append(root)
        
        while len(queue) > 0:
            curr = queue.popleft()

            aux = curr.right
            curr.right = curr.left
            curr.left = aux

            if curr.right:
                queue.append(curr.right)
            
            if curr.left:
                queue.append(curr.left)

        return root