class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        j = len(array[0])-1
        i = 0
        while i < len(array) and j >= 0:
            if target == array[i][j]:
                return True
            elif target > array[i][j]:#如果target更大，指针下移
                i += 1
            else:#如果target更小，指针左移
                j -= 1
        return False



if __name__ ==  "__main__":
    A = Solution()
    SS = A.Find(5,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
    print(SS)
