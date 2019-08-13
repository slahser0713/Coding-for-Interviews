class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:#无左节点就意味着左边不存在叶子节点了，就在右节点下面找叶子节点
            return self.minDepth(root.right)+1 #返回右边叶子节点的最小深度再+1（1是根节点本身）
        if not root.right:
            return self.minDepth(root.left) +1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1#若左右两边都有子节点，代表最小路径的叶子节点在两边最小深度小的那一边
