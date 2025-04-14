from collections import deque, defaultdict
class FreqStack:

    def __init__(self):
        self.counter = defaultdict(int)
        self.stacks = defaultdict(deque)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.max_frequency = max(self.max_frequency, self.counter[val])
        self.stacks[self.counter[val]].append(val)

    def pop(self) -> int:
        el = self.stacks[self.max_frequency].pop()
        self.counter[el] -= 1
        if not self.stacks[self.max_frequency]:
            del self.stacks[self.max_frequency]
            self.max_frequency -= 1
        return el


stk = FreqStack()
stk.push(5)
stk.push(7)
stk.push(5)
stk.push(7)
stk.push(4)
stk.push(5)
for i in range(4):
    print(stk.pop())

