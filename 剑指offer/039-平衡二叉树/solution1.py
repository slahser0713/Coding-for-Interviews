class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:#方法一，对每个节点的左右子树求深度，深度差绝对值不超过1则为平衡二叉树
    def IsBalanced_Solution(self, pRoot:TreeNode):
        # write code here
        if not pRoot:
            return True
        if abs(self.depth(pRoot.left)-self.depth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)#对左右子节点继续进行对比

    def depth(self,root:TreeNode):#求该节点深度
        if not root:
            return 0
        ldepth = self.depth(root.left)
        rdepth = self.depth(root.right)
        return max(ldepth,rdepth)+1
