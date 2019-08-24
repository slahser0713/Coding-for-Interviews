class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.same(pRoot.left,pRoot.right)
    def same(self,p1,p2):
        if not p1 and not p2:
            return True
        if not p1 or not p2:
            return False
        if p1.val == p2.val:
            return self.same(p1.left,p2.right) and self.same(p1.right,p2.left)
        return False

