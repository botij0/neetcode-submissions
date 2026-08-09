# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbersRecursive(l1, l2, 0)
    
    def addTwoNumbersRecursive(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None
        
        if not l1 and not l2 and carry == 1:
            return ListNode(1)
        
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        value = v1 + v2 + carry
        carry = value // 10
        value = value % 10

        return ListNode(value, self.addTwoNumbersRecursive(l1.next if l1 else None, l2.next if l2 else None, carry))

