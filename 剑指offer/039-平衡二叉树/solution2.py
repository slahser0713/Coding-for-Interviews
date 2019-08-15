class Solution:#方法二，dfs
    def IsBalanced_Solution(self, pRoot):
        return self.dfs(pRoot) != -1
    def dfs(self, pRoot):
        if pRoot is None:
            return 0
        left = self.dfs(pRoot.left)
        if left == -1:
            return -1
        right = self.dfs(pRoot.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:#左右节点如果深度差大于1返回False
            return -1
        return max(left, right) + 1 #如果左右节点都不返回False，代表其为平衡二叉树，返回其深度
