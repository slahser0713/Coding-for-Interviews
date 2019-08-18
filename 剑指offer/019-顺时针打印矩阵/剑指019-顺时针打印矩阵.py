class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)#弹出第一行
            if not matrix:
                break
            matrix = self.turn(matrix)#变为新的矩阵
        return res
    def turn(self,matrix):
        num_row = len(matrix[0])
        num_column = len(matrix)
        new_mat = []
        for j in range(num_row-1,-1,-1):
            new_mat1 = []
            for i in range(num_column):
                new_mat1.append(matrix[i][j])
            new_mat.append(new_mat1)
        return new_mat
