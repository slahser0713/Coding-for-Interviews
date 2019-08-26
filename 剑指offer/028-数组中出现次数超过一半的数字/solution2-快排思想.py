class Solution:
    #  方法二，快排后，中位数的数量是否大于一半
    def MoreThanHalfNum_Solution(self, numbers):
        n = len(numbers)
        self.quick_sort(numbers,0,n-1)
        res = 0
        for i in numbers:
            if i == numbers[n//2]:
                res += 1
        if res > n / 2.0:
            return numbers[n//2]
        return 0
    def quick_sort(self,numbers,first,last):
        if first >= last:
            return
        low = first
        high = last
        mid_value = numbers[first]
        while low < high:
            while low < high and mid_value <= numbers[high]:
                high -= 1
            numbers[low] = numbers[high]
            while low < high and numbers[low] < mid_value:
                low += 1
            numbers[high] = numbers[low]
        numbers[low] = mid_value
        self.quick_sort(numbers,first,low-1)
        self.quick_sort(numbers,low+1,last)



A = Solution()
s = A.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2])
print(s)

