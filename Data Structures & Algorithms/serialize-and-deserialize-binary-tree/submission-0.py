# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        self.serializeDfs(root, result)
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0
        return self.deserializeDfs(values)

    def serializeDfs(self, node: Optional[TreeNode], result: List[str]):
        if not node:
            result.append("N")
            return
        
        result.append(str(node.val))
        self.serializeDfs(node.left, result)
        self.serializeDfs(node.right, result)

    def deserializeDfs(self, values: List[str]) -> Optional[TreeNode]:
        if values[self.i] == "N":
            self.i += 1
            return None
        
        node = TreeNode(int(values[self.i]))
        self.i += 1
        node.left = self.deserializeDfs(values)
        node.right = self.deserializeDfs(values)

        return node
