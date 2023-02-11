#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[k]: 偷前k个房子的时候的最大盗窃价值
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, n+1):
            dp[k] = max(dp[k-1], dp[k-2] + nums[k-1])
        return dp[n]
        
# @lc code=end

