class MyQueue:

    def __init__(self):
        self.stack = []
        print(self.stack)

    def push(self, x: int) -> None:
        self.stack.append(x)
        print(self.stack)

    def pop(self) -> int:
        x = self.stack.pop(0)
        return x

    def peek(self) -> int:
        print(self.stack)
        return self.stack[0]

    def empty(self) -> bool:
        print(self.stack)
        return len(self.stack)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()