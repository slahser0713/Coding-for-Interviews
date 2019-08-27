class Solution:
    def FindGreatestSumOfSubArray(self, array):
        sum_array = 0
        dp = array[0]
        for i in range(len(array)):
            sum_array = max(sum_array+array[i],array[i])  #  sum_array是array[i]为末尾元素的子数组的和的最大值，子数组的元素的相对位置不变
            dp = max(dp,sum_array) #  dp是当前以array[i]结尾的子数组和最大值和之前的子数组最大值做比较，谁大谁就是新的dp
        return dp


    def FindGreatestSumOfSubArray(self, array):
        dp = [0] * len(array)
        # 或者也可以存储每一个点结束时的最大子数组，最后在进行比较
        dp[0] = array[0] #  dp[i]代表以i为结尾的子数组最大和
        for i in range(1,len(array)):
            dp[i] = max(dp[i-1]+array[i],array[i])
        return max(dp) #  返回数组中的最大值，即为子数组最大和