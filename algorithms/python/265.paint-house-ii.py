#
# @lc app=leetcode id=265 lang=python3
#
# [265] Paint House II
#

# @lc code=start
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        n_color = len(costs[0])
        print(n_color)
        dp = [[0]*n_color for _ in range(n+1)]
        for j in range(0, n_color):
            dp[1][j] = costs[0][j]
        for k in range(2, n+1):
            for c in range(0, n_color):
                dp[k][c] = min(dp[k-1][0:c] + dp[k-1][c+1:]) + costs[k-1][c]
        return min(dp[n])
# @lc code=end

