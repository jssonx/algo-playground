#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#

# @lc code=start
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if (k == 1): return 0 if n > 2 else 1
        if (n <= 2): return pow(k, n)
        dp = [[0]*2 for _ in range(n+1)]
        # 0：连续一个，与上一个颜色不同
        # 1：连续两个，与上一个颜色相同
        dp[1][0] = k
        dp[1][1] = 0
        for i in range(2, n+1):
            dp[i][0] = (k-1)*(dp[i-1][0] + dp[i-1][1])
            dp[i][1] = dp[i-1][0]
        return dp[n][0]+dp[n][1]
# @lc code=end

