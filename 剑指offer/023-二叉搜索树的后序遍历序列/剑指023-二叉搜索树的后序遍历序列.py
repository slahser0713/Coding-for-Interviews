class Solution:
    def VerifySquenceOfBST(self, sequence):
        if  not sequence:
            return False
        len_s = len(sequence)
        root = sequence[-1]
        for i in range(len_s):#找到第一个比根节点大的下标，跳出，此时坐标左边都应该比根节点大，右边比根节点小
            if sequence[i] > root:
                break
                print(i)
        for j in range(i+1,len_s):#一旦右边有一个比根节点大则False
            print(j)
            if sequence[j] < root:
                return False
        left  = True
        if i > 0:#当左子树不为空，则对左子树再次进行递归判断
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < len_s - 1::#当右子树不为空，则对右子树再次进行递归判断
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right#左右子树都为True则成立

