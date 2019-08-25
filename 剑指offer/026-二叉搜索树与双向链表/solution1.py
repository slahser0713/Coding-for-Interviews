class Solution:
    def __init__(self):
        self.res = []
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        self.midtravel(pRootOfTree)
        for i in range(len(self.res)-1):
            self.res[i].right = self.res[i+1]
            self.res[i+1].left = self.res[i]
        return self.res[0]
    # 方法一，中序遍历将节点加入一个列表，再将列表中节点的right指向下一个节点，将下一个节点的left指向上一个节点
    def midtravel(self,pRootOfTree):
        if not pRootOfTree:
            return
        self.midtravel(pRootOfTree.left)
        self.res.append(pRootOfTree)
        self.midtravel(pRootOfTree.right)


