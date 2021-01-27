# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)
        s = node
        while l1 and l2:
            if l1.val <= l2.val:
                s.next = l1
                s = l1
                l1 = s.next
                
            else:
                s.next = l2
                s = l2
                l2 = s.next
                
        if l1 == None:
            s.next = l2
            
        elif l2 == None:
            s.next = l1
            
        return node.next
    