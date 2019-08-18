class Solution:
    def Sum_Solution(self, n):
        res = n
        return res and res + self.Sum_Solution(n-1)#在python中，A and B如果A为True返回B,如果A为Faule返回A，这里递归到n = 0时，返回res = 0，完成累加