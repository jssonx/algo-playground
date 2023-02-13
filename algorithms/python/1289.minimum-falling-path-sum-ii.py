#
# @lc app=leetcode id=1289 lang=python3
#
# [1289] Minimum Falling Path Sum II
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, grid):
        n = len(grid)
        n_costs = len(grid[0])
        dp = [[0]*n_costs for _ in range(n+1)]
        for j in range(0, n_costs):
            dp[1][j] = grid[0][j]
        for k in range(2, n+1):
            for c in range(0, n_costs):
                dp[k][c] = min(dp[k-1][0:c] + dp[k-1][c+1:]) + grid[k-1][c]
        return min(dp[n])
# @lc code=end

