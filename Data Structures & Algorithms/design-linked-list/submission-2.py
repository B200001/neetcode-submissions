class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    

class MyLinkedList:

    def __init__(self):
        # self.node = ListNode(0)
        
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left


    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        first, second, third = self.left, self.left.next, self.left.next.next
        temp = ListNode(val)
        first.next = temp
        second.prev = temp
        temp.next = second
        temp.prev = first

    def addAtTail(self, val: int) -> None:
        first, second, third = self.right.prev.prev, self.right.prev, self.right
        temp = ListNode(val)
        second.next = temp
        temp.prev = second
        temp.next = third
        third.prev = temp

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            temp = ListNode(val)
            first, second = curr.prev, curr
            first.next = temp
            second.prev = temp
            temp.next = second
            temp.prev = first
        


    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right:
            first, second, third = curr.prev, curr, curr.next
            first.next = third
            third.prev = first
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)