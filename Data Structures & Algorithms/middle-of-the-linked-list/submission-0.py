# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowP, fastP = head, head

        while fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next

        return slowP
