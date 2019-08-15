class Solution:
    def reOrderArray(self, array):
        # write code here
        odd =[]
        even = []
        for i in array:
            if i % 2 ==1:
                even.append(i)
            else:
                odd.append(i)
        return even+odd


