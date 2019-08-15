class Solution:
    def Power(self, base, exponent):
        if base == 0 and exponent is not 0:#指数不为0，底为o一定为0
            return 0
        if exponent == 0:#指数为0一定为1
            return 1
        e = abs(exponent)
        tmp = base
        res = 1
        while e > 0:#利用快速幂，二进制转化
            #如果最后一位为1，那么给res乘上这一位的结果
            if e & 1 == 1:
                res =res * tmp
            e = e >> 1#二进制向右移一位
            tmp = tmp * tmp#当前的底变成2次方
        return res if exponent > 0 else 1/res
