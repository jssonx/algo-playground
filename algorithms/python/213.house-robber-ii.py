#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        nums_1 = nums[0:n-1]
        nums_2 = nums[1:n]
        max_val = max(self.rob_in_range(nums_1), self.rob_in_range(nums_2))
        return max_val

    def rob_in_range(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, n + 1):
            op_1 = dp[k-1]
            op_2 = dp[k-2] + nums[k-1]
            dp[k] = max(op_1, op_2)
        return dp[n]
        
# @lc code=end

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        n1 = nums[0:n-1]
        n2 = nums[1:n]
        res = max(self.rob_in_range(n1), self.rob_in_range(n2))
        return res
    
    def rob_in_range(self, nums):
        n = len(nums)
        res = 0 
        # 0: 本轮我抢的最大收益
        # 1: 本轮我不抢的最大收益
        dp = [[0] * 2 for _ in range(n+1)]
        dp[1][0] = nums[0]
        dp[1][1] = 0
        for k in range(2, n+1):
            dp[k][0] = dp[k-1][1] + nums[k-1]
            dp[k][1] = max(dp[k-1][0], dp[k-1][1])
        res = max(dp[n][0], dp[n][1])
        return res
"""