class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 辅助列表result，达到栈的效果
    def printListFromTailToHead(self, listNode):
        # write code here
        node = listNode
        stack = []
        result = []
        while node:
            stack.append(node.val)
            node = node.next
        while stack:
            result.append(stack.pop())
        return result
