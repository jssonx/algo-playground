#
# @lc app=leetcode id=256 lang=python3
#
# [256] Paint House
#

# @lc code=start
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0]*3 for _ in range(n+1)]
        # 0: 当前房子是红色 时的最低成本
        # 1: 当前房子是蓝色 时的最低成本
        # 2: 当前房子是绿色 时的最低成本
        dp[1][0] = costs[0][0]
        dp[1][1] = costs[0][1]
        dp[1][2] = costs[0][2]
        for k in range(2, n+1):
            red = costs[k-1][0]
            blue = costs[k-1][1]
            green = costs[k-1][2]
            dp[k][0] = min(dp[k-1][1] + red, dp[k-1][2] + red)
            dp[k][1] = min(dp[k-1][0] + blue, dp[k-1][2] + blue)
            dp[k][2] = min(dp[k-1][0] + green, dp[k-1][1] + green)
        return min(dp[n][0], dp[n][1], dp[n][2])
# @lc code=end

