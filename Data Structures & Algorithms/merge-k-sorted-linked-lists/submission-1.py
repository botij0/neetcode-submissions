# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        heap = []

        for i,l in enumerate(lists):
            aux = 0
            while l:
                heapq.heappush(heap, (l.val, i, aux, l))
                l = l.next
                aux += 1
        
        aux = dummy
        while heap:
            _,_,_,current = heapq.heappop(heap)
            aux.next = current
            aux = current

        return dummy.next
