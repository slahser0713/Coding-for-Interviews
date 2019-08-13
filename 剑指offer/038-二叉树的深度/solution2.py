class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
递归的思想，pRoot为空返回0，否则对其子树继续进行深度遍历
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left_d  = self.TreeDepth(pRoot.left)
        right_d = self.TreeDepth(pRoot.right)
        return max(left_d,right_d)+1
