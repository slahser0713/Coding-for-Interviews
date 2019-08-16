class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        head = ListNode(0)
        cur = head
        while pHead2 and pHead1:
            if pHead2.val >= pHead1.val:
                cur.next = pHead1
                cur = cur.next
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                cur = cur.next
                pHead2 = pHead2.next
        if pHead1:
            cur.next = pHead1#cur,next接过来，后面的就全解上了
        if pHead2:
            cur.next = pHead2
        return head.next