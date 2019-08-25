class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 方法二，对左右子树分别做递归处理
        self.Convert(pRootOfTree.left) #  对左子树做递归,使其成为一个双向链表
        left = pRootOfTree.left #  用一个left指针，找到左子树最右边的节点
        if left:
            while left.right:
                left = left.right #  找到左子树最右节点将left指针指向这个节点
            left.right = pRootOfTree
            pRootOfTree.left = left #  跳出循环后，找到最右节点，将最右节点的right指向根节点，将根节点的left指向这个节点
        self.Convert(pRootOfTree.right) #  同理，对右子树做递归,使其成为一个双向链表
        right = pRootOfTree.right
        if right:
            while right.left:
                right = right.left
            right.left = pRootOfTree
            pRootOfTree.right = right
        while pRootOfTree.left: #  找点最左节点，返回即为双向链表的头结点
            pRootOfTree  = pRootOfTree.left
        return pRootOfTree


