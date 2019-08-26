class Solution:
    #  方法一，利用字典存储每个数字出现的次数
    def MoreThanHalfNum_Solution(self, numbers):
        dict_res = {}
        for num in numbers:
            dict_res[num] = 0
            # if not dict_res. __contains__(num):
            #     dict_res[num] = 1
            # else:
            #     dict_res[num] += 1
        for num in numbers:
            dict_res[num] += 1
            if dict_res[num] / (len(numbers)) > 0.5:
                return num
        return 0


A = Solution()
s = A.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2])
print(s)

