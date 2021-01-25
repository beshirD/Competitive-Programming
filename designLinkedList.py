class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        
        currNode = self.head
        for i in range(index):
            currNode = currNode.next
        return currNode.val
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
    
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return  
        
        newNode = ListNode(val)
        currNode = self.head
        if index <= 0:
            newNode.next = currNode
            self.head = newNode
        else:
            for i in range(index-1):
                currNode = currNode.next
            newNode.next = currNode.next
            currNode.next = newNode
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        currNode = self.head
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index-1):
                currNode = currNode.next
            currNode.next = currNode.next.next
        self.length -= 1
            
