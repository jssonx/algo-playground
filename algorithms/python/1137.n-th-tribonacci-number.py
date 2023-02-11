#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start

class Solution:
    def tribonacci(self, n: int) -> int:
        if (n == 0 or n == 1 or n == 2):
            return 1 if n == 2 else n
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
        
# @lc code=end

