# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastP, slowP = head, head

        while fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next

            if fastP == slowP:
                return True
        
        return False