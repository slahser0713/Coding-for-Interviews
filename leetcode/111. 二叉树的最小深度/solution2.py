class Solution:
    def minDepth(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return 0
        queue = [root]
        while queue:
            res += 1 # 队列不为空，则代表这层不为空，则深度+1
            n = len(queue)
            for i in range(n): # 遍历该层
                node = queue.pop(0) # 将这一层的节点从队列中全部弹出
                if not node.left and not node.right: # 当左右子节点都为空，则返回该层层数即为深度
                    return res
                if node.left: # 将下一层的节点全部加入队列中
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
