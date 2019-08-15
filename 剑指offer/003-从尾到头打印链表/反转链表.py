class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        result = []      
        cur = listNode
        pre = None
        #倒置链表
        while cur:
            nextnode = cur.next #找了第三个指针来记录，cur后面节点的位置，使cur后面的节点在扒断后不会丢失
            cur.next = pre
            pre = cur
            cur = nextnode
        #依次输出链表
        while pre:
            result.append(pre.val)
            pre = pre.next
        return result
