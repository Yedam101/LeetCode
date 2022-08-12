class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        temp = []
        while len(self.stack) > 1:
            temp.append(self.stack.pop(0))
        ret = self.stack.pop(0)
        self.stack = temp
        return ret

    def top(self):
        return self.stack[-1]

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False