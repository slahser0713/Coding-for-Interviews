class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count




# # -*- coding:utf-8 -*-
# class Solution:
#     def NumberOf1(self, n):
#         # write code here
#         return bin(n).replace("0b","").count("1") if n>=0 else bin(2**32+n).replace("0b","").count("1")
