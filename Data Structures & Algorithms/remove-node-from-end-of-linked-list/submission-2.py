# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return None
       
        L = 0
        aux = head
        while aux:
            aux = aux.next
            L += 1
        
        target = head.next
        prev = head

        N = L - n

        if N == 0:
            aux = head.next
            head.next = None
            return aux

        while N > 1:
            prev = target
            target = target.next
            N -= 1        

        
        prev.next = target.next
        target.next = None

        return head
        

