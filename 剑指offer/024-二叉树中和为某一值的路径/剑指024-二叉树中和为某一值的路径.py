class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        result = []
        path = []
        def currentpath(node,path,currentnumber):
            currentnumber += node.val
            path.append(node)
            if currentnumber == expectNumber and not node.left and not node.right:
                pathnum = []
                for i in path:
                    pathnum.append(i.val)
                result.append(pathnum)
            if currentnumber < expectNumber:
                if node.left:
                    currentpath(node.left,path,currentnumber)
                if node.right:
                    currentpath(node.right,path,currentnumber)
            path.pop()#路径path退回到上一层的父节点上（左节点不满足，退到父节点，再看右节点满不满足）
        currentpath(root,[],0)
        return result
#没有做长度判断
