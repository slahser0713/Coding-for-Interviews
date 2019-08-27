class Solution:
    def GetUglyNumber_Solution(self, index):
        if not index:
            return 0
        res = [1]
        i2 = i3 = i5 = 0
        while len(res) < index:
            u2,u3,u5 = res[i2]*2,res[i3]*3,res[i5]*5
            if u2 <= u3 and u2 <= u5:  #  选择其中最小的一个入列，并且向下遍历
                min = u2
                i2 += 1
            elif u3<= u2 and u3 <= u5:
                min = u3
                i3 += 1
            else:
                min = u5
                i5 += 1
            if min != res[-1]: #  去重操作，同样的数不多次入队
                res.append(min)
        return res[-1]

a = Solution()
print(a.GetUglyNumber_Solution(1))



