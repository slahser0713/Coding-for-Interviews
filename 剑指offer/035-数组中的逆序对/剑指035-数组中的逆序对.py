class Solution:
    #  整体思路是归并排序
    def __init__(self):
        self.count = 0
    def InversePairs(self, data):
        def merge_sort(data):
            if len(data) <= 1:
                return data
            mid = len(data) // 2
            left = merge_sort(data[:mid])
            right = merge_sort(data[mid:])
            left_point = 0
            right_point = 0
            res = []
            while len(left) > left_point and len(right) > right_point:
                if left[left_point] <= right[right_point]:
                    res.append(left[left_point])
                    left_point += 1
                else:
                    #  当右边的归并子列表中的数比左边子列表小时，对其进行归并排序，这时左子列表中还有多少数代表有多少个逆序对
                    res.append(right[right_point])
                    right_point += 1
                    self.count += len(left[left_point:])
            res += left[left_point:]
            res += right[right_point:]
            return res
        merge_sort(data)
        return self.count

if __name__ == '__main__':
    a = Solution()
    print(a.InversePairs([2,1,4,2,1,2,4,6,1]))