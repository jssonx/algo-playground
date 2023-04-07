#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (46.22%)
# Likes:    3192
# Dislikes: 1199
# Total Accepted:    350.7K
# Total Submissions: 758.8K
# Testcase Example:  '5'
#
# You have n coins and you want to build a staircase with these coins. The
# staircase consists of k rows where the i^th row has exactly i coins. The last
# row of the staircase may be incomplete.
# 
# Given the integer n, return the number of complete rows of the staircase you
# will build.
# 
# 
# Example 1:
# 
# 
# Input: n = 5
# Output: 2
# Explanation: Because the 3^rd row is incomplete, we return 2.
# 
# 
# Example 2:
# 
# 
# Input: n = 8
# Output: 3
# Explanation: Because the 4^th row is incomplete, we return 3.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
#

# @lc code=start
#  前k层需要的硬币总数为(1 + mid) * mid / 2
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n + 1
        while left + 1 != right:
            mid = (left + right) // 2
            if mid * (mid + 1) // 2 <= n:
                left = mid
            else:
                right = mid
        return left
# @lc code=end

