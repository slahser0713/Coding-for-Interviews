class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1]
        for i in range(1,len(nums)):
            dp.append(1) #  给每个位置结束的最长上升序列一个初始值，当这个位置的数很小时代表以这个数结束的上升序列为它本身（1）
            for j in range(i):
                if nums[i] > nums[j]:
                    #  dp[j] +1 代表当前点i接着以j这个点结束的最长上升序列，并且nums[i]比nums[j]大，
                    #  这个最长序列的长度能够再加一，再和之前最大的dp[i]做比较得到新的最大dp[i],即为以i这个点结束的最长上升序列
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp) #  返回以不同元素结尾的最长序列的最大值

#  对原序列进行遍历，将每位元素二分插入res中,如果res中元素都比它小，将它插到最后,否则，用它覆盖掉比它大的元素中最小的那个。
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = [nums[0]]
        for num in nums:
            if num > res[-1]:
                res.append(num)
            else:
                l = 0
                r = len(res) -1
                while l < r:
                    mid = (r+l) // 2
                    if num > res[mid]:
                        l = mid + 1
                    else:
                        r = mid
                res[l] = num
        return len(res)

