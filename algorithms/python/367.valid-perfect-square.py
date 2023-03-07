#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            mid_square = mid * mid
            if mid_square == num:
                return True
            elif mid_square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
# @lc code=end

