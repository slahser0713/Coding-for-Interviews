class Solution:
    def jumpFloorII(self, number):
        res = [0,1,0]
        if number < 2:
            return res[number]
        else:
            for i in range(2,number+1):
                res[2] = 2*res[1]
                res[1] = res[2]
            return res[2]
    
