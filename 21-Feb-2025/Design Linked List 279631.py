# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/


class Node:

    def __init__(self,val,next=None):
        self.val = val
        self.next= next
       
class MyLinkedList:
    def __init__(self, head=None):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.size+=1
       

    def addAtTail(self, val: int) -> None:
        
        new_node = Node(val, None) 
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1
        return 

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return 
        if index == 0:
            self.addAtHead(val)
            return 
        elif index == self.size:
            self.addAtTail(val)
            return 
        curr = self.head
        for _  in range(index-1):
            curr = curr.next
        curr.next = Node(val, curr.next)
        self.size+=1
        
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.head
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
       
        for _ in range(index-1):
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
        self.size -= 1
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)