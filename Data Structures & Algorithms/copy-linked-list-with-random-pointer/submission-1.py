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
        
        randomPointers = {}
        newHead = Node(head.val)
        aux = head.next
        previous = newHead
        randomPointers[head] = newHead

        while aux:
            clone = Node(aux.val)
            randomPointers[aux] = clone
            previous.next = clone

            previous = previous.next
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
