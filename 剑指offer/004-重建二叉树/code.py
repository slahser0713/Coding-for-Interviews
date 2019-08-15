class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return
        root = TreeNode(pre[0])
        for i in range(len(tin)):
            if tin[i] == root.val:
                break
        root.left = self.reConstructBinaryTree(pre[1:i+1],tin[:i])#pre的1到i个数为左子树的先序遍历，tin的0到i-1个数为左子树的中序遍历
        root.right = self.reConstructBinaryTree(pre[i+1:],tin[i+1:])#pre的i+1到最后一个数为左子树的先序遍历，tin的i+1到最后一个数为左子树的中序遍历
        return root

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
        
def breadth_travel(root):
    if not root:
        return
    queue = [root]
    result = []
    while queue:
        cur = queue.pop(0)
        result.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return result

a = Solution()
preorder(a.reConstructBinaryTree([1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7]))
print(breadth_travel(a.reConstructBinaryTree([1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7])))
