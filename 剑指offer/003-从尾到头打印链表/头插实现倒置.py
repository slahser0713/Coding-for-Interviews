
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
         
        l = []
        node = listNode
        while node:
            l.insert(0,head.val)
            head = head.next
        return l


