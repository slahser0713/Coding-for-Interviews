class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        def getfirstk(data,k):
            low = 0
            high = len(data) - 1
            while low < high:
                mid = (low + high) // 2
                if data[mid] < k - 0.5:
                    low = mid + 1
                else:
                    high = mid
            if data[low] == k:
                return low
            else: #  若是数组中没有k，则返回-1
                return -1
        def getlastk(data,k):
            low = 0
            high = len(data) - 1
            while low < high:
                mid = (low + high + 1) // 2
                if data[mid] > k + 0.5:
                    high = mid - 1
                else:
                    low = mid
            if data[high] == k:
                return high
            else:
                return -1
        if getlastk(data,k) == -1 and getfirstk(data,k) == -1:
             return 0
        else:
            return getlastk(data,k) - getfirstk(data,k) + 1