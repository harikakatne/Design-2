class myQueue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self,n):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(n)
    def pop(self):
        x = self.stack1[-1]
        self.stack1.pop()
        return x
    def peek(self):
        return self.stack1[-1]
    def empty(self):
        return len(self.stack1) == 0