class Solution:
    #  两个数排列，a1+ a2更小就将a1放在a2前面
    #  利用冒泡排序，将排列起来最小的a1冒到最前面
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        def compare(a1,a2): #  比较函数
            if a1+ a2 < a2 + a1:
                return 1
            else:
                return 0
        for j in range(len(numbers)-1): #  冒泡函数
            for i in range(len(numbers)-1,j,-1):
                if compare(str(numbers[i]),str(numbers[i-1])):
                    numbers[i-1],numbers[i] = numbers[i],numbers[i-1]
        return "".join([str(x) for x in numbers])

a = Solution()
print(a.PrintMinNumber([3,5,1,4,2]))