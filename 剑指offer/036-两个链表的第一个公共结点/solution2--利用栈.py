class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        lst1 = []
        lst2 = []
        result = []

        if not pHead1 or not pHead2:
            return None

        p1 = pHead1
        p2 = pHead2
        #  将节点压入栈中
        while p1:
            lst1.append(p1)
            p1 = p1.next
        while p2:
            lst2.append(p2)
            p2 = p2.next
        #  将所有的相同节点加入一个栈中
        while lst1 and lst2:
            node1 = lst1.pop()
            node2 = lst2.pop()
            if node1 == node2:
                result.append(node1)

        if result: #  最后加入结果栈的节点弹出，即为第一个公共节点
            node = result.pop()
            return node
