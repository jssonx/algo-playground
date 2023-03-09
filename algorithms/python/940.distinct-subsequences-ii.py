#
# @lc app=leetcode id=940 lang=python3
#
# [940] Distinct Subsequences II
#

# @lc code=start
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * 26
        M = 10**9 + 7
        for ch in s:
            sum = 0
            for i in range(26):
                sum = (sum + dp[i]) % M
            dp[ord(ch)-ord('a')] = sum + 1
            
        res = 0
        for i in range(26):
            res = (res + dp[i]) % M
        return res
# @lc code=end

