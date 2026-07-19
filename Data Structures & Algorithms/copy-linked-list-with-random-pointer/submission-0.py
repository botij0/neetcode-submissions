"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        newHead = None
        previous = None

        randomPointers = {}
        aux = head
        while aux:
            clone = Node(aux.val, None, None)
            if aux:
                randomPointers[aux] = clone

            if not newHead:
                newHead = clone
            
            if previous:
                previous.next = clone

            previous = clone
            aux = aux.next

        aux = head
        aux2 = newHead
        while aux:
            if aux.random:
                randomTarget = randomPointers[aux.random]
                aux2.random = randomTarget

            aux = aux.next
            aux2 = aux2.next
        
        return newHead
