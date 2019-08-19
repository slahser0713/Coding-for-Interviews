class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        while pushV:#当push不为空一直执行压栈操作
            stack.append(pushV.pop(0))
            while stack:#当栈内不为空，循环判断栈内最后一个入栈元素是否和出栈列表第一个元素相等
                if stack[-1] == popV[0]:#相等则弹出
                    stack.pop()
                    popV.pop(0)
                else:#直到一个不等，跳出循环，继续压栈
                    break
        return True if stack == [] else False#最后栈内空了代表popv符合出栈顺序
