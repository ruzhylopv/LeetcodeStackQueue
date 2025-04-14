from collections import deque as Queue
from collections import defaultdict


class MyStack:

    def __init__(self):
        self.queue_in = Queue()
        self.queue_2 = Queue()
        

    def push(self, x: int) -> None:
        for i in range(len(self.queue_in)):
            self.queue_2.append(self.queue_in.popleft())
        self.queue_in.append(x)
        for i in range(len(self.queue_2)):
            self.queue_in.append(self.queue_2.popleft())
        

    def pop(self) -> int:
        return self.queue_in.popleft()


    def top(self) -> int:
        if self.queue_in:
            return self.queue_in[0]

    def empty(self) -> bool:
        return len(self.queue_in) == 0
