class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        #  计算每一位上1出现的次数
        tmp = n
        res = 0
        base = 1
        while tmp: #  由个位起，依次计算
            last = tmp % 10
            tmp = tmp // 10
            res += tmp * base
            if last > 1:
                res += base
            elif last == 1: #等于1代表后面的数并没有走完一个完整的底，所以求一个特殊情况
                res += n % base + 1
            base *= 10
        return res




