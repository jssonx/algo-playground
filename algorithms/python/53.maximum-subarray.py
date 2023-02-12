#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        dp[0] = nums[0]
        max_val = nums[0]
        for i in range(1, n):
            dp[i] = nums[i]
            dp[i] += max(dp[i-1], 0)
            max_val = max(max_val, dp[i])
        return max_val

        
# @lc code=end

