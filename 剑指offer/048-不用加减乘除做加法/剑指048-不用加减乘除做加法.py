class Solution:
    def Add(self, num1, num2):
        while num2:
            res = (num1 ^ num2)& 0xffffffff
            f = ((num1 & num2) << 1) & 0xffffffff
            num1 = res
            num2 = f
        if num1 > 0x7fffffff:
            res = ~(num1 ^ 0xffffffff)
        else:
            res = num1
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.Add(111,899))
