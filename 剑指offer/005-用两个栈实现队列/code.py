class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        #当stack2不为为空时才能从stack1往里面添加元素，否则先弹出stack2里面的元素
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())                
        return self.stack2.pop()
