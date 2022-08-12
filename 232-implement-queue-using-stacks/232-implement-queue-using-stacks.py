class MyQueue:
    def __init__(self):
        self.Q = []

    def push(self, x):
        self.Q.append(x)

    def pop(self):
        temp = []
        while len(self.Q) > 1:
            temp.append(self.Q.pop())
        ret = self.Q.pop()
        while temp:
            self.Q.append(temp.pop())
        return ret

    def peek(self):
        return self.Q[0]

    def empty(self):
        if len(self.Q) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()