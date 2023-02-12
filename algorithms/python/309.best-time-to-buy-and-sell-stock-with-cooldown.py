#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        # 0：手上持有股票的最大收益
        # 1：手上不持有股票，并且处于冷动期中的累计最大收益
        # 2：手上不持有股票，并且不处于冷冻期中的最大收益
        dp = [[0]*3 for _ in range(n+1)]
        dp[1][0] = -prices[0]
        dp[1][1] = 0
        dp[1][2] = 0
        for k in range(2, n + 1):
            dp[k][0] = max(dp[k-1][0], dp[k-1][2] - prices[k-1])
            dp[k][1] = dp[k-1][0] + prices[k-1]
            dp[k][2] = max(dp[k-1][2], dp[k-1][1])
        # return max(dp[n][0], dp[n][1], dp[n][2])
        return max(dp[n][1], dp[n][2])
# @lc code=end

