# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break
        root.left = self.buildTree(preorder[1:i+1],inorder[:i])
        root.right = self.buildTree(preorder[i+1:],inorder[i+1:])
        return root

class Solution:#利用栈和字典
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        dicts= {val:i for i,val in enumerate(inorder)}#构建值和其在中序遍历的位置序号对应的字典
        stack= [root]
        for i in range(1,len(preorder)):
            num = preorder[i]
            idx = dicts[num]
            interval = TreeNode(num)
            #如果这个数的位置序号比栈中最后一个小，说明你是栈中最后一个的左子树，
            if idx < dicts[stack[-1].val]:
                stack[-1].left=interval
                stack.append(interval)
            #比最后一个大，说明此时是某个节点的右子树
            else:
                #出栈，使temp的val的index比idx小，idx作为temp的右子树
                while stack and idx > dicts[stack[-1].val]:#终止条件为栈为空，或者idx<栈顶元素序号，说明idx应该在栈顶元素的左子树中。
                    temp = stack.pop()
                temp.right = interval
                stack.append(interval)
        return root