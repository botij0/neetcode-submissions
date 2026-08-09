# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:     
        L = 0
        aux = head
        while aux:
            aux = aux.next
            L += 1
        
        N = L - n

        if N == 0:
            return head.next

        target = head.next
        prev = head

        while N > 1:
            prev = target
            target = target.next
            N -= 1        

        prev.next = target.next
        target.next = None

        return head
        

