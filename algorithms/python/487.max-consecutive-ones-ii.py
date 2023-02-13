#
# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][0]表示该位置不翻转的结果
        # dp[i][1]表示该位置翻转的结果
        dp = [[0]*2 for _ in range(n+1)]
        if nums[0] == 1:
            dp[1] = [1, 1]
        else:
            dp[1] = [0, 1]
        for k in range(2,n+1):
            if nums[k-1]==1:
                dp[k][0] = dp[k-1][0] + 1
                dp[k][1] = dp[k-1][1] + 1
            else:
                dp[k][0] = 0
                dp[k][1] = dp[k-1][0] + 1
        res = 0
        for x in dp:
            res = max(res, x[1])
        return res
# @lc code=end

