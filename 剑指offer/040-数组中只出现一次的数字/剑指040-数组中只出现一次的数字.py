class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        dict1 = {}
        for i in array:
            if not dict1.__contains__(i):
                dict1[i] = 1
            else:
                dict1[i] += 1
        res = []
        for i in array:
            if dict1[i] == 1:
                res.append(i)
        return res