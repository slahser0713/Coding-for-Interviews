class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#利用队列的特性，层次遍历每一层的节点，deep深度+1
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        queue = [pRoot]
        deep = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                # 将这一层的节点从队列中全部弹出
                node = queue.pop(0)
                # 将下一层的节点全部加入队列中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            deep += 1
        return deep
