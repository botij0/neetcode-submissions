class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        r = self.head
        
        while r and i < index:
            r = r.next
            i+=1
        
        if r is None:
            return -1
        else:
            return r.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, self.head)
        self.head = newNode
        

    def addAtTail(self, val: int) -> None:
        r = self.head
        while r.next:
            r = r.next
        
        newNode = ListNode(val)
        r.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        r = self.head
        
        while r and i < index - 1:
            r = r.next
            i+=1
        
        if r is None:
            return
        
        aux = r.next
        newNode = ListNode(val, aux)
        r.next = newNode
        

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        r = self.head
        
        while r.next and i < index - 1:
            r = r.next
            i+=1
        
        if r.next is None:
            return

        aux = r.next.next
        r.next.next = None
        r.next = aux
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)