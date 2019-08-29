class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        listcode = ['0','1','2','3','4','5','6','7','8','9'] #  将字符串和其下标一一对应
        label = 1
        a = 0
        res = 0
        if s[0] == "+":
            label = 1
            a = 1
        elif s[0] == "-":
            label = -1
            a = 1
        for i in s[a:]:
            if i in listcode:
                res = 10 * res + listcode.index(i) #  index能够返回listcode中的下标为整形
            else:
                return 0
        return res*label