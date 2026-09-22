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

        newHead = Node(head.val, None, None)

        aux = head.next
        prev = newHead
        d = {}
        d[head] = newHead

        while aux:
            current = Node(aux.val, None, None)
            prev.next = current

            d[aux] = current

            aux = aux.next
            prev = prev.next
        
        aux = head
        aux2 = newHead

        while aux:
            aux2.random = d[aux.random] if aux.random else None

            aux = aux.next
            aux2 = aux2.next

        return newHead