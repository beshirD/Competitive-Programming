class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        nextNode = None
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        head = prev
        return head
    
    
