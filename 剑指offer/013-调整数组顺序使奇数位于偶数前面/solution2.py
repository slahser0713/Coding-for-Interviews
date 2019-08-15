#冒泡
class Solution:
    def reOrderArray(self, array):
        # write code here
        for i in range(1,len(array)):
            for j in range(0,len(array)-i):
                if array[j+1] % 2 ==1 and array[j] % 2==0:
                    array[j+1],array[j] = array[j],array[j+1]
        return array
