class Solution:
    def Permutation(self, ss):
        if len(ss) <= 1:
            return ss
        res = []
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i]+ss[i+1:]): #  固定一个字符串中的元素，对其他元素递归的求全排列
                res.append(ss[i]+j)
        return sorted(list(set(res)))  #  最后对整个全排列字符串列表去重排序




