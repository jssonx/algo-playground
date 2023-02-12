#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        # 0: 这轮[结束时]，已持有第1股的最大收益
        # 1: 这轮[结束时]，已售出第1股的最大收益
        # 2: 这轮[结束时]，已持有第2股的最大收益
        # 3: 这轮[结束时]，已售出第2股的最大收益
        dp = [[0] * 4 for _ in range(n+1)]
        dp[1][0] = -prices[0]
        dp[1][1] = 0
        dp[1][2] = -prices[0]
        dp[1][3] = 0
        for k in range(2, n+1):
            dp[k][0] = max(dp[k-1][0], -prices[k-1]) # 这轮有1G: 上轮就有1G，或这轮买的1G
            dp[k][1] = max(dp[k-1][1], dp[k-1][0] + prices[k-1]) # 这轮没1G: 上轮已售出1G，或上轮持有1G然后这轮售出了1G
            dp[k][2] = max(dp[k-1][2], dp[k-1][1] - prices[k-1]) # 这轮有2G: 上轮已买入2G，或上轮卖出1G然后这轮买入2G
            dp[k][3] = max(dp[k-1][3], dp[k-1][2] + prices[k-1]) # 这轮没2G: 上轮已经卖出2G，或上轮买入了2G然后这轮卖出2G
        res = max(dp[n][0], dp[n][1], dp[n][2], dp[n][3])
        return res
# @lc code=end

