class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        res = []
        windows = []
        sum  = 0
        for i in range(1,tsum // 2 + 2):
            windows.append(i)
            sum += i
            while sum > tsum:
                sum -= windows.pop(0)
            if sum == tsum:
                res.append(windows[:])
        return res
