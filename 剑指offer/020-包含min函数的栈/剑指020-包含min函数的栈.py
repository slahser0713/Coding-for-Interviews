class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, node):
        self.stack.append(node)
        if not self.min_stack:
            self.min_stack.append(node)
        else:#记录当前最小值的最小栈，每加入一个数最小栈内也加入一个最小值保持一致
            if self.min_stack[-1] < node:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(node)
    def pop(self):
        self.min_stack.pop()#当弹出一个数的时候，最小栈也弹出一个，回退到这个数进入之前的最小栈状态
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def min(self):
        return self.min_stack[-1]
