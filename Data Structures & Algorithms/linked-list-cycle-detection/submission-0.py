# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowP, fastP = head, head
        while fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next

            if slowP == fastP:
                return True
        
        return False