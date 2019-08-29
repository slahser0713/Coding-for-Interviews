class Solution:
    #  将链表1接到列表2后面，将链表2接到链表1后面，使其长度一样，最终遇到的第一个相同节点即为第一个公共节点
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        p1,p2= pHead1,pHead2
        while p1 != p2:
            if p1:
                p1=p1.next
            else:
                p1=pHead2
            if p2:
                p2 = p2.next
            else:
                p2 = pHead1
        return p1