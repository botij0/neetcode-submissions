# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        aux = []
        self.serDfs(root, aux)
        return ",".join(aux)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0
        return self.desDfs(values)


    def serDfs(self, node: Optional[TreeNode], result: List[str]):
        if not node:
            result.append("N")
            return
            
        result.append(str(node.val))
        self.serDfs(node.left, result)
        self.serDfs(node.right, result)
    
    def desDfs(self, values: List[str]) -> Optional[TreeNode]:
        if values[self.i] == "N":
            self.i += 1
            return None
        
        newNode = TreeNode(int(values[self.i]))
        self.i += 1

        newNode.left = self.desDfs(values)
        newNode.right = self.desDfs(values)
        
        return newNode
