class Solution:
    def rectCover(self, number):
        res = [0,1,2,0]
        if number < 3:
            return res[number]
        else:
            for i in range(3,number+1):
                res[3] = res[1] + res[2]
                res[1] = res[2]
                res[2] = res[3]
            return res[3]
