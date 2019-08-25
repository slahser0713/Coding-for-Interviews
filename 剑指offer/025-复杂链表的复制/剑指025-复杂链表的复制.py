class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        # 第一步，建立新链表，每个新节点在旧节点的后面一个
        cur = pHead
        while cur:
            newnode = RandomListNode(cur.label)
            nextnode = cur.next
            cur.next = newnode
            newnode.next = nextnode
            cur = nextnode
        # 第二步，将复制的结点的random指针指向被复制结点的random指针的下一个结点
        cur = pHead
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 第三步，分开新旧列表，返回新列表
        cur = pHead
        new_head = pHead.next
        while cur:
            copynode = cur.next
            nextcur = copynode.next
            cur.next = nextcur
            cur = nextcur
            if nextcur:
                copynode.next = nextcur.next
            else:
                copynode.next = None
        return new_head