class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 层序遍历没啥好说的
    def PrintFromTopToBottom(self, root):
        if not root:
            return
        queue = [root]
        res = []
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.pop(0)
                res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return
