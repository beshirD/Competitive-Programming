    def middleNode(self, head: ListNode) -> ListNode:
        # i = 0 
        # curr = head
        # while curr != None:
        #     curr = curr.next
        #     i+=1
        # if i % 2 == 0:
        #     middle = math.ceil(i/2) + 1 
        # else:
        #     middle = math.ceil(i/2)
        # curr = head
        # for j in range(middle-1):
        #     curr = curr.next
        #     print(curr)
        # return curr
        # // using two pointers runner technique
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow