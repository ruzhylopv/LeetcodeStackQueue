class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class MyQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

        

    def pop(self) -> int:
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

        el = self.stack2.pop()

        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

        return el

    def peek(self) -> int:
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

        el = self.stack2.peek()

        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())


        return el

    def empty(self) -> bool:
        return self.stack1.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()