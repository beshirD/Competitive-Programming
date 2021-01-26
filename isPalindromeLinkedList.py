class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
def isPalindrome(self, head: ListNode) -> bool:
    # find the midpoint
    fast = head
    slow = head
    while fast and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    #reverse the seconde half
    prev = None
    while slow:
        slow.next, slow, prev = prev, slow.next, slow
    # compare teh two halves
    while prev:
        if prev.val != head.val:
            return False
            
        prev = prev.next
        head = head.next
    return True