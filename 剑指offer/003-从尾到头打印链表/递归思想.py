class Solution:
    def printListFromTailToHead(self,listNode):
        # write code here
        result = []
        def printListnode(listNode):
            if listNode:
                printListnode(listNode.next)
                result.append(listNode.val)
        printListnode(listNode)
        return result
