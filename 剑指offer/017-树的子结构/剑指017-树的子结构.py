class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:#p1：找到最后了都没找到为p2的子结构，p2：空节点不为任何树的子结构
            return False
        res = False
        if pRoot1.val == pRoot2.val:#找到值相等的节点
            res = self.DoesTree1haveTree2(pRoot1,pRoot2)#做子结构判断
        if res:#返回True则有子结构
            return res
        return self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)#否则往下寻找下一个节点值相等的点

    def DoesTree1haveTree2(self, pRoot1, pRoot2):
        if not pRoot2:#先判断p2，p2为None则子结构存在
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1haveTree2(pRoot1.left,pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right,pRoot2.right)#对左右子节点再次做p1与p2对应子结构判断，两边都满足才能返回True
