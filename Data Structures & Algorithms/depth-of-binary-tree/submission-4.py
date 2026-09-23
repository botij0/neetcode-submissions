# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root:
            queue.append(root)

        result = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result += 1
        return result
        # return self.dfs(root)

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.dfs(root.right), self.dfs(root.left))