class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        #  方法一，归并或者快排，排好序后输出前k个
        if k > len(tinput):
            return []
        def merge_sort(tinput):
            n = len(tinput)
            if n <= 1:
                return tinput
            mid = n // 2
            left = merge_sort(tinput[:mid])
            right = merge_sort(tinput[mid:])
            res = []
            left_point = 0
            right_point = 0
            while left_point < len(left) and right_point < len(right):
                if left[left_point] <= right[right_point]:
                    res.append(left[left_point])
                    left_point += 1
                else:
                    res.append(right[right_point])
                    right_point += 1
            res += left[left_point:]
            res += right[right_point:]
            return res
        new_tinput = merge_sort(tinput)
        return new_tinput[:k]
