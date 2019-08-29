class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution: #  计算两个链表长度，长链表先走k步（两个链表的长度差），然后两个链表开始同时走，当遇到第一个相同节点时即为第一个公共节点
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return
        if pHead1 == pHead2:
            return pHead1
        count1 = 1
        count2 = 1
        cur1 = pHead1
        cur2 = pHead2
        while cur1:
            cur1 = cur1.next
            count1 += 1
        while cur2:
            cur2 = cur2.next
            count2 += 1
        cur1 = pHead1
        cur2 = pHead2
        if count1 > count2:
            for i in range(count1 - count2):
                cur1 = cur1.next
        elif count1 < count2:
            for i in range(count2 - count1):
                cur2 = cur2.next
        while cur1:
            if cur2 == cur1: #  先判断公共节点，在同时后移
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
