from queue import Queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = Queue()
        self.queue2 = Queue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue2.put(x)
        while (not self.queue1.empty()):
            self.queue2.put(self.queue1[0])
            self.queue1.get()
        temp = self.queue1 
        queue1 = self.queue2
        queue2 = temp
        return queue2

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if (not self.queue1.empty()):
            return 
        else:
            removed = self.queue1.get()
            return removed
        
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.queue1.empty():
            top = self.queue1.queue[0]
            return top
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue1.empty()


# Your MyStack object will be instantiated and called as such:
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())
myStack.top()
myStack.pop()
print(myStack.top())
print(myStack.empty())
