class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        queue = [pRoot]
        res = []
        num  = 0
        while queue:
            now_res = []
            n = len(queue)
            for i in range(n):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                now_res.append(cur.val)
            res.append(now_res)
        return res
                