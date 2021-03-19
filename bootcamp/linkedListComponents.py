# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: ListNode, G) -> int:
        curr = head
        count = 0
        visited = set()
        set_G = set(G)
        while curr:
            if curr.val in set_G and curr.val not in visited:
                count += 1
                self.helper(curr,set_G,visited)
            curr = curr.next
        return count
    def helper(self,curr,set_G,visited):
        if curr and curr.val in set_G:
            visited.add(curr.val)
            self.helper(curr.next,set_G,visited)
        return 

            