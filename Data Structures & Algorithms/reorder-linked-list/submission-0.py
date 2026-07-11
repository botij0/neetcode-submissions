# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # [0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
        if not head:
            return head

        h = head
        end = head
        bend = end
        i = 1
        while end.next is not None:
            bend = end
            end = end.next
            i += 1 
        
        n = math.ceil(i / 2) -1
        
        while n > 0:

            bend.next = None
            aux = h.next
            h.next = end
            end.next = aux

            h = aux
            while end.next is not None:
                bend = end
                end = end.next

            n -= 1
        










        
