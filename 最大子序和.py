#用动态规划做，刚刚上课才学过嘿嘿
class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        dp =[0]*len(nums)
        dp[0] = nums[0]
        dp_max = nums[0]
        for i,a in enumerate(nums):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            dp_max = max(dp_max,dp[i])
        return dp_max
