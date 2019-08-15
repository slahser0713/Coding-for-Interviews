class Solution:
    def jumpFloor(self, number):
        res = [0,1,2]
        for i in range(3,number+1):
            res.append(res[i-1]+res[i-2])


        return res[number]
