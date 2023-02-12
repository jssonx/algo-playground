#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*2 for _ in range(n+1)]
        # 0: 当前轮，以当前元素结尾且上升，的序列的最长长度
        # 1: 当前轮，以当前元素结尾且下降，的序列的最长长度
        dp[1][0] = 1
        dp[1][1] = 1
        for k in range(2, n+1):
            if (nums[k-1] < nums[k-2]):
                dp[k][1] = dp[k-1][0] + 1
                dp[k][0] = dp[k-1][0]
            if (nums[k-1] > nums[k-2]):
                dp[k][0] = dp[k-1][1] + 1
                dp[k][1] = dp[k-1][1]
            if (nums[k-1] == nums[k-2]):
                dp[k][0] = dp[k-1][0]
                dp[k][1] = dp[k-1][1]
        return max(dp[n][0], dp[n][1])
# @lc code=end

