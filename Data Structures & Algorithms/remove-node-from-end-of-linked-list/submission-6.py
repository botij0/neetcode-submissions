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
        
        ns = L - n
        # if L == 1:
        #     return None
        
        print(ns)
        current = head
        prev = current

        while current:
            if ns == 0:
                if current == head:
                    head = head.next
                    break

                prev.next = current.next

            prev = current
            current = current.next
            ns -= 1
        
        return head