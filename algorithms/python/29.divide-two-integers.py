#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (17.16%)
# Likes:    4076
# Dislikes: 12955
# Total Accepted:    590.6K
# Total Submissions: 3.4M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.
# 
# The integer division should truncate toward zero, which means losing its
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335
# would be truncated to -2.
# 
# Return the quotient after dividing dividend by divisor.
# 
# Note: Assume we are dealing with an environment that could only store
# integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this
# problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31
# - 1, and if the quotient is strictly less than -2^31, then return -2^31.
# 
# 
# Example 1:
# 
# 
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# 
# 
# Example 2:
# 
# 
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0
# 
# 
#
    

# @lc code=start

# 难点在于：边界
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # 是否同号
        positive = (dividend >= 0) is (divisor >= 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        # 被除数，除数
        res = self.binarySearch(dividend, divisor)
        if not positive:
            res = -res
        return min(max(res, -2**31), 2**31 - 1)
    
    def binarySearch(self, dividend, divisor):
        res = 0
        left, right = -1, dividend + 1
        while left + 1 != right:
            mid = (left + right) // 2
            if divisor * mid <= dividend < divisor * (mid + 1):
                return mid
            elif divisor * mid > dividend:
                right = mid
            else:
                left = mid
        return res

# @lc code=end

'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        positive = (dividend >= 0) is (divisor >= 0) # 是否同号
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1 # 位运算的计算速度比逻辑运算更快
                temp <<= 1
        if not positive:
            res = -res
        return res if -2**31 <= res <= 2**31-1 else 2**31-1
'''